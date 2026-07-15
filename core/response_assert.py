"""入参出参一致性校验。

从 tests/test_smoke.py 抽离，便于单元测试覆盖。
校验规则：请求参数值 == 响应中同名字段值（同名 + self 前缀别名，忽略大小写）。
"""
from __future__ import annotations

from typing import Any

from generators.data_generator import COMMON_PARAMS


def assert_params_match_response(params: dict, response_json: dict) -> None:
    """断言入参出参一致。

    定位响应数据区域（result → items[0] / result[0]），逐个校验传入参数在响应中同名字段的值。
    空列表或非 dict 结果直接跳过（无法校验）。
    """
    result = _locate_result_data(response_json)
    if not isinstance(result, dict):
        return

    for param_name, param_value in params.items():
        if param_name in COMMON_PARAMS or param_name.startswith("_"):
            continue
        resp_value = _find_value_in_result(result, param_name)
        if resp_value is not None:
            if str(resp_value) != str(param_value):
                # 尝试 self 前缀别名匹配（如 OrderNo → selfOrderNo）
                alt_value = _find_alt_value_in_result(result, param_name, param_value)
                if alt_value is None:
                    assert resp_value == param_value, (
                        f"入参出参不一致: {param_name} 请求={param_value}, 响应={resp_value}"
                    )


def _locate_result_data(response_json: dict) -> Any:
    """从响应 JSON 中定位数据区域。

    - {result: {items: [...]}} → items[0]
    - {result: [...]}          → result[0]
    - {result: {...}}          → result
    - 其他                      → response_json 本身
    """
    result = response_json.get("result", response_json)
    if isinstance(result, dict):
        if "items" in result:
            items = result["items"]
            if items:
                return items[0]
            return None  # 空列表，无法校验
        return result
    if isinstance(result, list):
        if result:
            return result[0]
        return None
    return result


def _find_value_in_result(result: dict, param_name: str) -> Any:
    """在响应结果中查找参数名对应的值（忽略大小写）"""
    param_lower = param_name.lower()
    for key, value in result.items():
        if key.lower() == param_lower:
            return value
    return None


def _find_alt_value_in_result(result: dict, param_name: str, param_value: Any) -> Any:
    """尝试 self 前缀匹配：OrderNo → selfOrderNo"""
    str_val = str(param_value)
    alt_name = "self" + param_name[0].upper() + param_name[1:]
    for key, value in result.items():
        if key.lower() == alt_name.lower() and str(value) == str_val:
            return value
    return None
