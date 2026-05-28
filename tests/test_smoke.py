import json

import allure
import pytest


def test_crud_smoke(case, http_client, prefetch_cache):
    params = dict(case["params"])
    body = params.pop("_body", None)

    # 用预取缓存替换占位参数（所有接口）
    _fill_params_from_cache(params, case["feature"], prefetch_cache, is_list=case.get("is_list", False))

    # 列表接口：补充缓存中的过滤参数（如 CarNo 给导出接口用）
    if case.get("is_list", False):
        _inject_list_filter_params(params, case["feature"], prefetch_cache)

    allure.dynamic.feature(case["feature"])
    allure.dynamic.story(case["story"])
    allure.dynamic.title(case["name"])

    with allure.step(f"{case['method']} {case['endpoint']}"):
        if case["method"] == "GET":
            response = http_client.get(case["endpoint"], params=params)
        elif case["method"] == "POST":
            kwargs = {"params": params}
            if body:
                kwargs["json"] = body
            response = http_client.post(case["endpoint"], **kwargs)
        else:
            response = http_client.request(case["method"], case["endpoint"], params=params)

    allure.attach(json.dumps(params, ensure_ascii=False), name="请求参数", attachment_type=allure.attachment_type.JSON)
    allure.attach(response.text, name="响应内容", attachment_type=allure.attachment_type.JSON)

    assert response.status_code == case["expect"]["status"], f"HTTP {response.status_code}, body={response.text[:200]}"
    body_json = response.json()
    assert "isSuccess" in body_json
    assert "errorCode" in body_json

    if case["case_type"] == "positive":
        assert body_json["isSuccess"] is True, f"message={body_json.get('message')}"
        assert body_json["errorCode"] == 0

        # 入参出参校验：请求中传的值 == 响应中同名字段的值
        _assert_params_match_response(params, body_json, case)


def _inject_list_filter_params(params: dict, module: str, cache: dict):
    """列表接口：从缓存中注入过滤参数（如导出接口需要 CarNo 限制范围）"""
    from generators.data_prefetch import get_param_value
    # 注入 CarNo
    if "CarNo" not in params:
        car_no = get_param_value("CarNo", module, cache)
        if car_no is not None:
            params["CarNo"] = car_no
    # 注入 KeyNo（GetActionLogs/GetOperationLogs）
    if "KeyNo" not in params:
        key_no = get_param_value("KeyNo", module, cache)
        if key_no is not None:
            params["KeyNo"] = key_no


def _fill_params_from_cache(params: dict, module: str, cache: dict, is_list: bool = False):
    """用预取缓存替换占位参数
    详情接口：缓存无匹配则删除参数（避免传 Faker 假值）
    列表接口：只补充有缓存值的过滤参数，不删除已有参数
    """
    from generators.data_prefetch import get_param_value
    COMMON_PARAMS = {"Platform", "SkipCount", "MaxResultCount", "IsTrack", "OperatorId", "QueryWriteDb"}
    BOOL_DEFAULTS = {"IsAuth", "IncludeRs", "isAuth", "includeRs"}
    for name in list(params.keys()):
        if name in COMMON_PARAMS or name in BOOL_DEFAULTS:
            continue
        cached_value = get_param_value(name, module, cache)
        if cached_value is not None:
            params[name] = cached_value
        elif not is_list:
            del params[name]


def _assert_params_match_response(params: dict, response_json: dict, case: dict):
    """入参出参校验：请求参数值 == 响应中同名字段值"""
    COMMON_PARAMS = {"Platform", "SkipCount", "MaxResultCount", "IsTrack", "OperatorId", "QueryWriteDb"}

    # 从响应中定位数据区域
    result = response_json.get("result", response_json)
    if isinstance(result, dict):
        # 列表接口：取 items 第一条
        if "items" in result:
            items = result["items"]
            if items and len(items) > 0:
                result = items[0]
            else:
                return  # 空列表，无法校验
    elif isinstance(result, list):
        if len(result) > 0:
            result = result[0]
        else:
            return

    if not isinstance(result, dict):
        return

    # 逐个校验传入的参数
    for param_name, param_value in params.items():
        if param_name in COMMON_PARAMS or param_name.startswith("_"):
            continue
        # 在响应中查找匹配值（同名 + 别名）
        resp_value = _find_value_in_result(result, param_name)
        if resp_value is not None:
            # 值匹配：直接相等或字符串比较
            if str(resp_value) != str(param_value):
                # 尝试别名匹配（如 OrderNo 可能对应 selfOrderNo）
                alt_value = _find_alt_value_in_result(result, param_name, param_value)
                if alt_value is None:
                    assert resp_value == param_value, (
                        f"入参出参不一致: {param_name} 请求={param_value}, 响应={resp_value}"
                    )


def _find_value_in_result(result: dict, param_name: str):
    """在响应结果中查找参数名对应的值（忽略大小写）"""
    param_lower = param_name.lower()
    for key, value in result.items():
        if key.lower() == param_lower:
            return value
    return None


def _find_alt_value_in_result(result: dict, param_name: str, param_value) -> any:
    """尝试 self 前缀匹配：OrderNo → selfOrderNo"""
    str_val = str(param_value)
    # 尝试 self + 首字母大写 的变体
    alt_name = "self" + param_name[0].upper() + param_name[1:]
    for key, value in result.items():
        if key.lower() == alt_name.lower() and str(value) == str_val:
            return value
    return None