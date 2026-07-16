"""业务流程执行器。

按顺序执行 PipelineConfig 中的步骤，支持：
- 参数引用解析（$var / $ref，兼容旧 $cache）
- 响应字段提取到流程上下文（extract）
- 断言（HTTP 状态码、isSuccess、入参出参一致性）
- allure 附件记录
"""
from __future__ import annotations

import json
import time
from dataclasses import dataclass, field
from typing import Any

import allure
import requests

from config import settings
from core.assertion_engine import (
    HttpStatusAssertionError,
    JsonExpectationError,
    assert_http_status,
    assert_json_expectations,
)
from core.json_path import MISSING, get_json_path, traverse_json
from core.pipeline_loader import PipelineConfig, StepConfig, resolve_value
from core.redaction import redact_sensitive, redact_text
from core.request_executor import execute_case
from core.safety_guard import SafetyViolation, ensure_pipeline_safe
from utils.http_client import HttpClient


class ReferenceResolutionError(ValueError):
    """流程参数引用无法解析。"""


class FieldExtractionError(ValueError):
    """流程声明的必需响应字段不存在。"""


@dataclass
class StepResult:
    """单个步骤的执行结果"""
    step_name: str
    success: bool
    method: str = ""
    endpoint: str = ""
    response: requests.Response | None = None
    status_code: int | None = None
    duration_ms: int = 0
    error_type: str = ""
    error: str = ""
    request_params: dict[str, Any] = field(default_factory=dict)
    extracted: dict[str, Any] = field(default_factory=dict)


@dataclass
class PipelineResult:
    """整个流程的执行结果"""
    pipeline_name: str
    success: bool
    step_results: list[StepResult] = field(default_factory=list)
    duration_ms: int = 0
    error_type: str = ""
    error: str = ""

    @property
    def failed_step(self) -> StepResult | None:
        """第一个失败的步骤"""
        for r in self.step_results:
            if not r.success:
                return r
        return None


def run_pipeline(
    pipeline: PipelineConfig,
    http_client: HttpClient,
    variables: dict[str, Any] | None = None,
) -> PipelineResult:
    """执行一个业务流程。

    按顺序执行 steps，每步：
    1. 解析参数引用（$var / $ref）
    2. 发送请求
    3. 断言
    4. 提取字段到上下文（供后续步骤引用）

    任一步骤失败则终止流程，返回已执行的结果。
    """
    pipeline_started = time.perf_counter()
    result = PipelineResult(pipeline_name=pipeline.name, success=True)
    context: dict[str, dict[str, Any]] = {}  # {step_name: {extracted_key: value}}
    variables = variables or {}

    base_url = getattr(http_client, "base_url", None)
    if isinstance(base_url, str):
        try:
            ensure_pipeline_safe(
                pipeline,
                base_url=base_url,
                environment=settings.TEST_ENVIRONMENT,
                allowed_hosts=settings.ALLOWED_TEST_HOSTS,
            )
        except SafetyViolation as exc:
            result.success = False
            result.error_type = "safety"
            result.error = f"安全检查失败: {exc}"
            result.duration_ms = _elapsed_ms(pipeline_started)
            return result

    with allure.step(f"业务流程: {pipeline.name}"):
        for step in pipeline.steps:
            step_result = _run_step(step, http_client, variables, context, pipeline.module)
            result.step_results.append(step_result)

            if not step_result.success:
                result.success = False
                result.error_type = step_result.error_type
                result.error = f"步骤 {step.name} 失败: {step_result.error}"
                break

            # 提取字段存入上下文，供后续步骤 $ref 引用
            if step_result.extracted:
                context[step.name] = step_result.extracted

    result.duration_ms = _elapsed_ms(pipeline_started)
    return result


def _run_step(
    step: StepConfig,
    http_client: HttpClient,
    variables: dict[str, Any],
    context: dict[str, dict[str, Any]],
    module: str,
) -> StepResult:
    """执行单个步骤"""
    step_started = time.perf_counter()
    result = StepResult(
        step_name=step.name,
        success=False,
        method=step.method,
        endpoint=step.endpoint,
    )

    try:
        # 解析参数引用
        params = _resolve_params(step.params, context, variables)
        body = _resolve_body(step.body, context, variables) if step.body else {}
        result.request_params = redact_sensitive(
            {"params": params, "body": body} if body else params
        )

        allure.dynamic.feature(module)
        allure.dynamic.title(f"{pipeline_step_title(step)}")

        with allure.step(f"{step.method} {step.endpoint}"):
            response = execute_case(http_client, step.method, step.endpoint, params, body or None)

        allure.attach(
            json.dumps(
                redact_sensitive({"params": params, "body": body} if body else params),
                ensure_ascii=False,
            ),
            name="请求参数",
            attachment_type=allure.attachment_type.JSON,
        )
        allure.attach(
            _redacted_response_text(response),
            name="响应内容",
            attachment_type=allure.attachment_type.JSON,
        )

        result.response = response
        result.status_code = response.status_code

        assert_http_status(response.status_code, step.expect.status, response.text)

        body_json = response.json()
        assert_json_expectations(
            body_json,
            step.expect,
            context=context,
            variables=variables,
            request_params=params,
        )

        # 提取字段到上下文
        if step.extract:
            result.extracted = _extract_fields(body_json, step.extract)

        result.success = True
        return result

    except ReferenceResolutionError as e:
        result.error_type = "reference"
        result.error = f"引用解析失败: {e}"
        return result
    except HttpStatusAssertionError as e:
        result.error_type = "http_status"
        result.error = f"HTTP 断言失败: {e}"
        return result
    except JsonExpectationError as e:
        result.error_type = "business_assertion"
        result.error = f"业务断言失败: {e}"
        return result
    except FieldExtractionError as e:
        result.error_type = "extraction"
        result.error = f"数据提取失败: {e}"
        return result
    except AssertionError as e:
        result.error_type = "assertion"
        result.error = f"断言失败: {e}"
        return result
    except (requests.RequestException, ConnectionError, TimeoutError) as e:
        result.error_type = "network"
        result.error = f"网络请求失败: {e}"
        return result
    except Exception as e:
        result.error_type = "execution"
        result.error = f"执行异常: {e}"
        return result
    finally:
        result.duration_ms = _elapsed_ms(step_started)


def _resolve_params(
    params: dict[str, Any],
    context: dict[str, dict[str, Any]],
    variables: dict[str, Any],
) -> dict[str, Any]:
    """解析参数引用；引用缺失时明确失败，禁止发送缺少关键参数的请求。"""
    resolved: dict[str, Any] = {}
    for name, value in params.items():
        resolved_value, hit = resolve_value(value, context, variables)
        if hit and resolved_value is not None:
            resolved[name] = resolved_value
            continue

        is_reference = isinstance(value, str) and value.startswith(("$var.", "$ref.", "$cache."))
        if is_reference:
            raise ReferenceResolutionError(f"参数 {name} 的引用未命中: {value}")
        resolved[name] = value
    return resolved


def _resolve_body(
    body: dict[str, Any],
    context: dict[str, dict[str, Any]],
    variables: dict[str, Any],
) -> dict[str, Any]:
    """递归解析请求体中的引用（$var / $ref / $cache），支持嵌套 dict 和 list。

    body 常含数组结构（如 Ids: [$ref.xxx]），需递归解析才能替换列表元素中的引用。
    引用缺失时明确失败，禁止发送缺少关键参数的请求。
    """
    return _resolve_nested(body, context, variables)


def _resolve_nested(
    value: Any,
    context: dict[str, dict[str, Any]],
    variables: dict[str, Any],
) -> Any:
    if isinstance(value, dict):
        return {k: _resolve_nested(v, context, variables) for k, v in value.items()}
    if isinstance(value, list):
        return [_resolve_nested(item, context, variables) for item in value]
    if isinstance(value, str):
        resolved, hit = resolve_value(value, context, variables)
        if hit and resolved is not None:
            return resolved
        is_reference = value.startswith(("$var.", "$ref.", "$cache."))
        if is_reference:
            raise ReferenceResolutionError(f"请求体引用未命中: {value}")
        return value
    return value


def _extract_fields(response_json: dict, extract_map: dict[str, str]) -> dict[str, Any]:
    """从响应 JSON 中按路径提取字段。

    extract_map: {上下文键: 响应字段路径}
    路径格式：
    - "id"                → response_json["result"]["id"] 或 response_json["id"]
    - "result.items[0].id" → 精确路径
    - "result.items.0.id"  → 精确路径（点号风格）
    """
    extracted: dict[str, Any] = {}
    for ctx_key, path in extract_map.items():
        found, val = _read_compat_path(response_json, path)
        if not found:
            raise FieldExtractionError(f"提取字段失败: {ctx_key} <- {path}")
        extracted[ctx_key] = val
    return extracted


def _get_by_path(data: Any, path: str) -> Any:
    """兼容旧测试的 JSON 路径读取入口。"""
    return get_json_path(data, path, result_shorthand=True)


def _traverse(data: Any, parts: list[str]) -> Any:
    """兼容旧测试的拆分路径遍历入口。"""
    value = traverse_json(data, parts)
    return None if value is MISSING else value


def _read_compat_path(data: Any, path: str) -> tuple[bool, Any]:
    from core.json_path import read_json_path

    return read_json_path(data, path, result_shorthand=True)


def pipeline_step_title(step: StepConfig) -> str:
    """生成步骤的 allure 标题"""
    return f"[{step.name}] {step.method} {step.endpoint}"


def _redacted_response_text(response: requests.Response) -> str:
    try:
        return json.dumps(redact_sensitive(response.json()), ensure_ascii=False)
    except Exception:
        return redact_text(response.text)


def _elapsed_ms(started: float) -> int:
    return max(0, round((time.perf_counter() - started) * 1000))
