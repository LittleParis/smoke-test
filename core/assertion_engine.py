"""YAML 业务流程使用的通用响应断言。"""
from __future__ import annotations

from typing import Any

from core.json_path import read_json_path
from core.pipeline_loader import StepExpect, resolve_value
from core.response_assert import assert_params_match_response


class HttpStatusAssertionError(AssertionError):
    """HTTP 状态码不符合预期。"""


class JsonExpectationError(AssertionError):
    """响应 JSON 不符合业务断言。"""


def assert_http_status(actual: int, expected: int, response_text: str = "") -> None:
    if actual != expected:
        raise HttpStatusAssertionError(
            f"HTTP 状态码不一致: 期望={expected}, 实际={actual}, body={response_text[:200]}"
        )


def assert_json_expectations(
    response_json: dict[str, Any],
    expect: StepExpect,
    *,
    context: dict[str, dict[str, Any]] | None = None,
    variables: dict[str, Any] | None = None,
    request_params: dict[str, Any] | None = None,
) -> None:
    """执行标准业务断言和 YAML 声明的通用断言。"""
    context = context or {}
    variables = variables or {}

    equals = _effective_equals(expect)
    for path, expected_value in equals.items():
        expected_value = _resolve_expected(expected_value, context, variables, path)
        found, actual_value = read_json_path(response_json, path)
        if not found:
            raise JsonExpectationError(f"字段不存在: {path}")
        if actual_value != expected_value:
            raise JsonExpectationError(f"字段值不一致: {path} 期望={expected_value!r}, 实际={actual_value!r}")

    for path in expect.exists:
        found, _ = read_json_path(response_json, path)
        if not found:
            raise JsonExpectationError(f"字段不存在: {path}")

    for path in expect.not_empty:
        found, value = read_json_path(response_json, path)
        if not found:
            raise JsonExpectationError(f"非空断言字段不存在: {path}")
        if _is_empty(value):
            raise JsonExpectationError(f"字段不能为空: {path}, 实际={value!r}")

    if expect.match_response:
        assert_params_match_response(request_params or {}, response_json)


def _effective_equals(expect: StepExpect) -> dict[str, Any]:
    """项目标准响应默认要求成功；显式配置可以覆盖默认值。"""
    equals: dict[str, Any] = {"isSuccess": True, "errorCode": 0}
    if expect.is_success is not None:
        equals["isSuccess"] = expect.is_success
        if expect.is_success is False and "errorCode" not in expect.equals:
            equals.pop("errorCode", None)
    equals.update(expect.equals)
    return equals


def _resolve_expected(
    value: Any,
    context: dict[str, dict[str, Any]],
    variables: dict[str, Any],
    path: str,
) -> Any:
    resolved, hit = resolve_value(value, context, variables)
    if not hit:
        raise JsonExpectationError(f"断言 {path} 的引用未命中: {value}")
    return resolved


def _is_empty(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple, dict, set)):
        return len(value) == 0
    return False
