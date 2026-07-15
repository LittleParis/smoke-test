"""core.assertion_engine 单元测试。"""
import pytest

from core.assertion_engine import assert_http_status, assert_json_expectations
from core.pipeline_loader import StepExpect


def test_standard_success_response_passes():
    assert_json_expectations({"isSuccess": True, "errorCode": 0}, StepExpect())


def test_standard_business_failure_is_rejected():
    with pytest.raises(AssertionError, match="isSuccess"):
        assert_json_expectations({"isSuccess": False, "errorCode": 1}, StepExpect())


def test_equals_supports_step_reference():
    expect = StepExpect(equals={"result.id": "$ref.list.id"})
    assert_json_expectations(
        {"isSuccess": True, "errorCode": 0, "result": {"id": 42}},
        expect,
        context={"list": {"id": 42}},
    )


def test_exists_and_not_empty():
    expect = StepExpect(exists=["result.id"], not_empty=["result.items"])
    assert_json_expectations(
        {"isSuccess": True, "errorCode": 0, "result": {"id": None, "items": [1]}},
        expect,
    )


def test_not_empty_rejects_empty_list():
    expect = StepExpect(not_empty=["result.items"])
    with pytest.raises(AssertionError, match="不能为空"):
        assert_json_expectations(
            {"isSuccess": True, "errorCode": 0, "result": {"items": []}},
            expect,
        )


def test_http_status_message_contains_expected_and_actual():
    with pytest.raises(AssertionError, match="期望=200, 实际=500"):
        assert_http_status(500, 200, "server error")
