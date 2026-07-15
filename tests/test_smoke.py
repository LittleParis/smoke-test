"""全量 Swagger 扫描冒烟测试（默认禁用）。

这是旧的冒烟测试模式：解析 swagger → 生成所有查询接口用例 → 白名单过滤 → 逐个执行。
默认不收集，通过环境变量 SMOKE_MODE=full 启用，作为兜底回归手段。

用法:
    SMOKE_MODE=full pytest tests/test_smoke.py -v   # 启用全量扫描
    pytest tests/test_pipeline.py -v                 # 默认走 YAML 流程（推荐）
"""
import json
import os

import allure
import pytest

from core.param_filler import fill_params_from_cache, inject_list_filter_params
from core.request_executor import execute_case
from core.response_assert import assert_params_match_response

# 默认禁用：只有 SMOKE_MODE=full 时才收集本模块的测试
pytestmark = pytest.mark.skipif(
    os.getenv("SMOKE_MODE", "").lower() != "full",
    reason="全量扫描模式默认禁用，设置 SMOKE_MODE=full 启用",
)


def test_crud_smoke(case, http_client, prefetch_cache):
    params = dict(case["params"])
    body = params.pop("_body", None)

    # 用预取缓存替换占位参数
    fill_params_from_cache(params, case["feature"], prefetch_cache, case_type=case["case_type"])

    # 正向列表接口：补充缓存中的过滤参数（如 CarNo 给导出接口用）
    if case.get("is_list", False) and case["case_type"] != "pairwise":
        inject_list_filter_params(params, case["feature"], prefetch_cache)

    allure.dynamic.feature(case["feature"])
    allure.dynamic.story(case["story"])
    allure.dynamic.title(case["name"])

    with allure.step(f"{case['method']} {case['endpoint']}"):
        response = execute_case(http_client, case["method"], case["endpoint"], params, body)

    allure.attach(json.dumps(params, ensure_ascii=False), name="请求参数", attachment_type=allure.attachment_type.JSON)
    allure.attach(response.text, name="响应内容", attachment_type=allure.attachment_type.JSON)

    assert response.status_code == case["expect"]["status"], f"HTTP {response.status_code}, body={response.text[:200]}"
    body_json = response.json()
    assert "isSuccess" in body_json
    assert "errorCode" in body_json

    if case["case_type"] in ("positive", "pairwise"):
        assert body_json["isSuccess"] is True, f"message={body_json.get('message')}"
        assert body_json["errorCode"] == 0

    # 正向用例：额外校验入参出参一致性
    if case["case_type"] == "positive":
        assert_params_match_response(params, body_json)

    # 边界用例：允许业务失败，只校验 HTTP 状态码（不校验 isSuccess）
