"""core.pipeline_executor 单元测试。

用 mock http_client，不依赖真实环境。
"""
from unittest.mock import MagicMock

import pytest

from core.pipeline_executor import (
    PipelineResult,
    StepResult,
    _extract_fields,
    _get_by_path,
    _resolve_params,
    _traverse,
    run_pipeline,
)
from core.pipeline_loader import PipelineConfig, StepConfig, StepExpect


class TestTraverse:
    def test_dict_path(self):
        assert _traverse({"a": {"b": 1}}, ["a", "b"]) == 1

    def test_list_index(self):
        assert _traverse({"items": [10, 20, 30]}, ["items", "1"]) == 20

    def test_missing_key(self):
        assert _traverse({"a": 1}, ["b"]) is None

    def test_out_of_range_index(self):
        assert _traverse({"items": [1]}, ["items", "5"]) is None

    def test_none_current(self):
        assert _traverse(None, ["a"]) is None

    def test_non_digit_index_on_list(self):
        assert _traverse({"items": [1]}, ["items", "abc"]) is None


class TestGetByPath:
    def test_dot_notation(self):
        data = {"result": {"items": [{"id": 42}]}}
        assert _get_by_path(data, "result.items.0.id") == 42

    def test_bracket_notation(self):
        data = {"result": {"items": [{"id": 42}]}}
        assert _get_by_path(data, "result.items[0].id") == 42

    def test_shorthand_with_result(self):
        """简写：自动尝试 result.<path>"""
        data = {"result": {"id": 42}}
        assert _get_by_path(data, "id") == 42

    def test_shorthand_without_result(self):
        """简写兜底：无 result 时尝试裸 <path>"""
        data = {"id": 42}
        assert _get_by_path(data, "id") == 42

    def test_missing_path(self):
        assert _get_by_path({"result": {}}, "missing") is None


class TestExtractFields:
    def test_extract_from_items(self):
        resp = {"result": {"items": [{"id": 1, "name": "x"}]}}
        extract_map = {"biz_id": "result.items.0.id"}
        assert _extract_fields(resp, extract_map) == {"biz_id": 1}

    def test_extract_multiple(self):
        resp = {"result": {"id": 1, "name": "x"}}
        extract_map = {"id": "id", "name": "name"}
        assert _extract_fields(resp, extract_map) == {"id": 1, "name": "x"}

    def test_extract_missing_returns_empty(self):
        resp = {"result": {}}
        assert _extract_fields(resp, {"x": "missing"}) == {}


class TestResolveParams:
    def test_resolve_cache_ref(self):
        cache = {"id": 52}
        params = {"id": "$cache.id", "Platform": "MyEhi"}
        result = _resolve_params(params, {}, cache)
        assert result == {"id": 52, "Platform": "MyEhi"}

    def test_resolve_ref(self):
        context = {"step1": {"biz_id": 100}}
        params = {"id": "$ref.step1.biz_id"}
        result = _resolve_params(params, context, {})
        assert result == {"id": 100}

    def test_missing_ref_dropped(self):
        """引用未命中的参数被丢弃（不传 None）"""
        params = {"id": "$ref.unknown.field", "Platform": "MyEhi"}
        result = _resolve_params(params, {}, {})
        assert "id" not in result
        assert result == {"Platform": "MyEhi"}

    def test_non_ref_values_preserved(self):
        params = {"Platform": "MyEhi", "SkipCount": 0, "MaxResultCount": 10}
        result = _resolve_params(params, {}, {})
        assert result == params


class TestRunPipeline:
    def _make_mock_response(self, status_code=200, json_data=None):
        resp = MagicMock()
        resp.status_code = status_code
        resp.text = str(json_data or {})
        resp.json.return_value = json_data or {}
        return resp

    def test_single_step_success(self):
        """单步骤流程成功"""
        mock_client = MagicMock()
        mock_client.get.return_value = self._make_mock_response(
            json_data={"isSuccess": True, "errorCode": 0, "result": {"id": 1}}
        )
        pipeline = PipelineConfig(
            name="test",
            module="Test",
            steps=[StepConfig(name="s1", endpoint="/api/Test/Get", expect=StepExpect(is_success=True))],
        )
        result = run_pipeline(pipeline, mock_client, {})
        assert result.success is True
        assert len(result.step_results) == 1
        assert result.step_results[0].success is True

    def test_multi_step_with_ref(self):
        """多步骤流程，步骤2引用步骤1提取的值"""
        mock_client = MagicMock()
        # 步骤1: 列表查询
        mock_client.get.side_effect = [
            self._make_mock_response(json_data={
                "isSuccess": True,
                "result": {"items": [{"id": 42, "name": "test"}]}
            }),
            # 步骤2: 详情查询
            self._make_mock_response(json_data={
                "isSuccess": True,
                "result": {"id": 42}
            }),
        ]
        pipeline = PipelineConfig(
            name="test",
            module="Test",
            steps=[
                StepConfig(
                    name="list",
                    endpoint="/api/Test/List",
                    step_type="list",
                    extract={"biz_id": "result.items.0.id"},
                    expect=StepExpect(is_success=True),
                ),
                StepConfig(
                    name="detail",
                    endpoint="/api/Test/Detail",
                    params={"id": "$ref.list.biz_id"},
                    expect=StepExpect(is_success=True, match_response=True),
                ),
            ],
        )
        result = run_pipeline(pipeline, mock_client, {})
        assert result.success is True
        # 验证步骤1提取了 biz_id
        assert result.step_results[0].extracted == {"biz_id": 42}
        # 验证步骤2收到了步骤1的值
        second_call_params = mock_client.get.call_args_list[1].kwargs.get("params", {})
        assert second_call_params.get("id") == 42

    def test_step_failure_stops_pipeline(self):
        """步骤失败则终止流程"""
        mock_client = MagicMock()
        mock_client.get.return_value = self._make_mock_response(
            status_code=500,
            json_data={"isSuccess": False, "errorCode": 1}
        )
        pipeline = PipelineConfig(
            name="test",
            module="Test",
            steps=[
                StepConfig(name="s1", endpoint="/api/Test/Get", expect=StepExpect(is_success=True)),
                StepConfig(name="s2", endpoint="/api/Test/Get2"),  # 不会执行
            ],
        )
        result = run_pipeline(pipeline, mock_client, {})
        assert result.success is False
        assert len(result.step_results) == 1  # 只执行了第一步
        assert "500" in result.error

    def test_is_success_mismatch_fails(self):
        """isSuccess 不匹配 → 失败"""
        mock_client = MagicMock()
        mock_client.get.return_value = self._make_mock_response(
            json_data={"isSuccess": False, "errorCode": 1, "message": "error"}
        )
        pipeline = PipelineConfig(
            name="test",
            module="Test",
            steps=[StepConfig(name="s1", endpoint="/api/Test/Get", expect=StepExpect(is_success=True))],
        )
        result = run_pipeline(pipeline, mock_client, {})
        assert result.success is False
        assert "isSuccess" in result.error

    def test_exception_handled(self):
        """异常被捕获，不传播"""
        mock_client = MagicMock()
        mock_client.get.side_effect = ConnectionError("network down")
        pipeline = PipelineConfig(
            name="test",
            module="Test",
            steps=[StepConfig(name="s1", endpoint="/api/Test/Get")],
        )
        result = run_pipeline(pipeline, mock_client, {})
        assert result.success is False
        assert "执行异常" in result.error
