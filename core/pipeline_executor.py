"""业务流程执行器。

按顺序执行 PipelineConfig 中的步骤，支持：
- 参数引用解析（$cache / $ref）
- 响应字段提取到流程上下文（extract）
- 断言（HTTP 状态码、isSuccess、入参出参一致性）
- allure 附件记录
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

import allure
import requests

from core.pipeline_loader import PipelineConfig, StepConfig, resolve_value
from core.request_executor import execute_case
from core.response_assert import assert_params_match_response
from utils.http_client import HttpClient


@dataclass
class StepResult:
    """单个步骤的执行结果"""
    step_name: str
    success: bool
    response: requests.Response | None = None
    error: str = ""
    extracted: dict[str, Any] = field(default_factory=dict)


@dataclass
class PipelineResult:
    """整个流程的执行结果"""
    pipeline_name: str
    success: bool
    step_results: list[StepResult] = field(default_factory=list)
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
    cache: dict[str, Any],
) -> PipelineResult:
    """执行一个业务流程。

    按顺序执行 steps，每步：
    1. 解析参数引用（$cache / $ref）
    2. 发送请求
    3. 断言
    4. 提取字段到上下文（供后续步骤引用）

    任一步骤失败则终止流程，返回已执行的结果。
    """
    result = PipelineResult(pipeline_name=pipeline.name, success=True)
    context: dict[str, dict[str, Any]] = {}  # {step_name: {extracted_key: value}}

    with allure.step(f"业务流程: {pipeline.name}"):
        for step in pipeline.steps:
            step_result = _run_step(step, http_client, cache, context, pipeline.module)
            result.step_results.append(step_result)

            if not step_result.success:
                result.success = False
                result.error = f"步骤 {step.name} 失败: {step_result.error}"
                break

            # 提取字段存入上下文，供后续步骤 $ref 引用
            if step_result.extracted:
                context[step.name] = step_result.extracted

    return result


def _run_step(
    step: StepConfig,
    http_client: HttpClient,
    cache: dict[str, Any],
    context: dict[str, dict[str, Any]],
    module: str,
) -> StepResult:
    """执行单个步骤"""
    result = StepResult(step_name=step.name, success=False)

    try:
        # 解析参数引用
        params = _resolve_params(step.params, context, cache)

        allure.dynamic.feature(module)
        allure.dynamic.title(f"{pipeline_step_title(step)}")

        with allure.step(f"{step.method} {step.endpoint}"):
            response = execute_case(http_client, step.method, step.endpoint, params)

        allure.attach(
            json.dumps(params, ensure_ascii=False),
            name="请求参数",
            attachment_type=allure.attachment_type.JSON,
        )
        allure.attach(response.text, name="响应内容", attachment_type=allure.attachment_type.JSON)

        result.response = response

        # 断言 HTTP 状态码
        if response.status_code != step.expect.status:
            result.error = f"HTTP {response.status_code} != {step.expect.status}, body={response.text[:200]}"
            return result

        body_json = response.json()

        # 断言 isSuccess
        if step.expect.is_success is not None:
            if body_json.get("isSuccess") != step.expect.is_success:
                result.error = f"isSuccess={body_json.get('isSuccess')} != {step.expect.is_success}, message={body_json.get('message')}"
                return result

        # 断言入参出参一致性
        if step.expect.match_response:
            assert_params_match_response(params, body_json)

        # 提取字段到上下文
        if step.extract:
            result.extracted = _extract_fields(body_json, step.extract)

        result.success = True
        return result

    except AssertionError as e:
        result.error = f"断言失败: {e}"
        return result
    except Exception as e:
        result.error = f"执行异常: {e}"
        return result


def _resolve_params(
    params: dict[str, Any],
    context: dict[str, dict[str, Any]],
    cache: dict[str, Any],
) -> dict[str, Any]:
    """解析参数中的所有引用，未命中的引用参数删除（避免传 None）"""
    resolved: dict[str, Any] = {}
    for name, value in params.items():
        resolved_value, hit = resolve_value(value, context, cache)
        if hit and resolved_value is not None:
            resolved[name] = resolved_value
        elif not isinstance(value, str) or not (value.startswith("$cache.") or value.startswith("$ref.")):
            # 非引用值原样保留
            resolved[name] = value
        # 引用未命中 → 丢弃该参数
    return resolved


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
        val = _get_by_path(response_json, path)
        if val is not None:
            extracted[ctx_key] = val
    return extracted


def _get_by_path(data: Any, path: str) -> Any:
    """按点号路径从嵌套 dict/list 中取值。

    支持：
    - "result.items.0.id"   点号风格
    - "result.items[0].id"  括号风格
    简写：当 path 不以 "result" 开头时，自动先尝试 result.<path>，再尝试 <path>
    """
    # 标准化路径：items[0] → items.0
    normalized = path.replace("[", ".").replace("]", "")
    parts = normalized.split(".")

    # 简写兜底：不以 result 开头时，先尝试 result.<path>
    if parts[0] != "result":
        val = _traverse(data, ["result"] + parts)
        if val is not None:
            return val
        # 再尝试裸 <path>
        return _traverse(data, parts)

    return _traverse(data, parts)


def _traverse(data: Any, parts: list[str]) -> Any:
    """遍历嵌套结构取值"""
    current = data
    for part in parts:
        if current is None:
            return None
        # 尝试 dict 键
        if isinstance(current, dict):
            current = current.get(part)
        # 尝试 list 索引
        elif isinstance(current, list) and part.isdigit():
            idx = int(part)
            if 0 <= idx < len(current):
                current = current[idx]
            else:
                return None
        else:
            return None
    return current


def pipeline_step_title(step: StepConfig) -> str:
    """生成步骤的 allure 标题"""
    return f"[{step.name}] {step.method} {step.endpoint}"
