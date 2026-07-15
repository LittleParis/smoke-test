"""core.response_assert 单元测试。"""
import pytest

from core.response_assert import (
    _find_alt_value_in_result,
    _find_value_in_result,
    _locate_result_data,
    assert_params_match_response,
)


class TestLocateResultData:
    def test_items_dict(self):
        """result 是 dict 且含 items → 取 items[0]"""
        resp = {"result": {"items": [{"id": 1}, {"id": 2}]}}
        assert _locate_result_data(resp) == {"id": 1}

    def test_items_empty(self):
        """空列表 → None"""
        resp = {"result": {"items": []}}
        assert _locate_result_data(resp) is None

    def test_result_list(self):
        """result 直接是列表 → 取第一项"""
        resp = {"result": [{"id": 1}]}
        assert _locate_result_data(resp) == {"id": 1}

    def test_result_plain_dict(self):
        """result 是 dict 无 items → 原样返回"""
        resp = {"result": {"id": 1, "name": "x"}}
        assert _locate_result_data(resp) == {"id": 1, "name": "x"}

    def test_no_result_key(self):
        """无 result 键 → 返回整个 response"""
        resp = {"isSuccess": True, "errorCode": 0}
        assert _locate_result_data(resp) == resp

    def test_result_non_dict_non_list(self):
        """result 是标量 → 原样返回"""
        resp = {"result": 42}
        assert _locate_result_data(resp) == 42


class TestFindValueInResult:
    def test_exact_match(self):
        result = {"OrderNo": "A001"}
        assert _find_value_in_result(result, "OrderNo") == "A001"

    def test_case_insensitive(self):
        result = {"orderno": "A001"}
        assert _find_value_in_result(result, "OrderNo") == "A001"

    def test_no_match(self):
        result = {"OrderNo": "A001"}
        assert _find_value_in_result(result, "Unknown") is None


class TestFindAltValueInResult:
    def test_self_prefix_match(self):
        """OrderNo → selfOrderNo，值相等才算匹配"""
        result = {"selfOrderNo": "A001"}
        assert _find_alt_value_in_result(result, "OrderNo", "A001") == "A001"

    def test_self_prefix_value_mismatch(self):
        """别名存在但值不等 → None"""
        result = {"selfOrderNo": "B002"}
        assert _find_alt_value_in_result(result, "OrderNo", "A001") is None

    def test_no_alt_name(self):
        result = {"orderNo": "A001"}
        assert _find_alt_value_in_result(result, "OrderNo", "A001") is None


class TestAssertParamsMatchResponse:
    def test_match_passes(self):
        """入参出参一致 → 不抛异常"""
        resp = {"result": {"id": 52, "orderNo": "A001"}}
        # 不抛异常即通过
        assert_params_match_response({"id": 52, "orderNo": "A001"}, resp)

    def test_mismatch_fails(self):
        """入参出参不一致 → 抛 AssertionError"""
        resp = {"result": {"id": 999}}
        with pytest.raises(AssertionError, match="入参出参不一致"):
            assert_params_match_response({"id": 52}, resp)

    def test_ignores_common_params(self):
        """COMMON_PARAMS 不参与校验"""
        resp = {"result": {"id": 1}}
        # Platform 不在响应中也应通过
        assert_params_match_response({"Platform": "MyEhi", "id": 1}, resp)

    def test_ignores_underscore_params(self):
        """下划线开头参数不参与校验"""
        resp = {"result": {"id": 1}}
        assert_params_match_response({"_body": {"x": 1}, "id": 1}, resp)

    def test_self_alias_passes(self):
        """self 前缀别名匹配 → 通过"""
        resp = {"result": {"selfOrderNo": "A001"}}
        assert_params_match_response({"orderNo": "A001"}, resp)

    def test_empty_items_skipped(self):
        """空列表 → 不校验，直接通过"""
        resp = {"result": {"items": []}}
        assert_params_match_response({"id": 52}, resp)

    def test_missing_param_in_response_skipped(self):
        """响应中无该字段 → 跳过（不报错）"""
        resp = {"result": {"id": 1}}
        assert_params_match_response({"unknownField": "x"}, resp)
