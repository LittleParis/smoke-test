"""core.pipeline_loader 单元测试。"""
from pathlib import Path

import pytest

from core.pipeline_loader import (
    PipelineConfig,
    PrefetchConfig,
    StepConfig,
    StepExpect,
    load_all_pipelines,
    load_pipeline,
    resolve_value,
)


class TestResolveValue:
    def test_resolves_cache_ref(self):
        cache = {"id": 52}
        assert resolve_value("$cache.id", {}, cache) == (52, True)

    def test_missing_cache_field(self):
        assert resolve_value("$cache.id", {}, {}) == (None, False)

    def test_resolves_ref(self):
        """$ref.<step>.<field> 引用前序步骤上下文"""
        context = {"query_list": {"complaint_id": 100}}
        assert resolve_value("$ref.query_list.complaint_id", context, {}) == (100, True)

    def test_missing_ref_step(self):
        assert resolve_value("$ref.unknown.field", {}, {}) == (None, False)

    def test_missing_ref_field(self):
        context = {"query_list": {}}
        assert resolve_value("$ref.query_list.missing", context, {}) == (None, False)

    def test_non_string_value(self):
        assert resolve_value(42, {}, {}) == (42, True)
        assert resolve_value(True, {}, {}) == (True, True)

    def test_plain_string(self):
        assert resolve_value("MyEhi", {}, {}) == ("MyEhi", True)

    def test_non_cache_non_ref_prefix(self):
        """$other 前缀不算引用，原样返回"""
        assert resolve_value("$other.id", {}, {}) == ("$other.id", True)


class TestLoadPipeline:
    def test_load_complaint_yaml(self):
        """加载示例 complaint.yaml，验证 v2 schema"""
        filepath = Path(__file__).resolve().parent.parent.parent / "config" / "pipelines" / "complaint.yaml"
        if not filepath.exists():
            pytest.skip("complaint.yaml 不存在")
        cfg = load_pipeline(filepath)
        assert cfg.module == "Complaint"
        assert cfg.enabled is True
        assert len(cfg.steps) == 2

        # 步骤1: query_list
        step1 = cfg.steps[0]
        assert step1.name == "query_list"
        assert step1.endpoint == "/api/Complaint/GetComplaints"
        assert step1.method == "GET"
        assert step1.step_type == "list"
        assert "complaint_id" in step1.extract
        assert step1.extract["complaint_id"] == "result.items.0.id"

        # 步骤2: query_detail，引用步骤1
        step2 = cfg.steps[1]
        assert step2.name == "query_detail"
        assert step2.params["id"] == "$ref.query_list.complaint_id"
        assert step2.expect.match_response is True

    def test_v1_cases_backward_compat(self, tmp_path):
        """v1 schema（cases）自动转换为 steps"""
        v1_yaml = tmp_path / "v1.yaml"
        v1_yaml.write_text("""
name: v1流程
module: Test
enabled: true
cases:
  - name: step1
    endpoint: /api/Test/Get
""", encoding="utf-8")
        cfg = load_pipeline(v1_yaml)
        assert len(cfg.steps) == 1
        assert cfg.steps[0].name == "step1"

    def test_step_expect_defaults(self):
        expect = StepExpect()
        assert expect.status == 200
        assert expect.is_success is None
        assert expect.match_response is False

    def test_pipeline_config_defaults(self):
        cfg = PipelineConfig(name="test", module="Test")
        assert cfg.enabled is True
        assert cfg.steps == []
        assert isinstance(cfg.prefetch, PrefetchConfig)

    def test_step_config_defaults(self):
        step = StepConfig(name="s1", endpoint="/api/X")
        assert step.method == "GET"
        assert step.step_type == "detail"
        assert step.params == {}
        assert step.extract == {}
        assert isinstance(step.expect, StepExpect)


class TestLoadAllPipelines:
    def test_loads_enabled_pipelines(self):
        pipelines = load_all_pipelines()
        assert len(pipelines) >= 1
        complaint = next((p for p in pipelines if p.module == "Complaint"), None)
        assert complaint is not None

    def test_skips_disabled(self, tmp_path):
        disabled_yaml = tmp_path / "disabled.yaml"
        disabled_yaml.write_text("""
name: 禁用流程
module: Test
enabled: false
steps:
  - name: x
    endpoint: /api/Test/GetX
""", encoding="utf-8")
        pipelines = load_all_pipelines(tmp_path)
        assert len(pipelines) == 0

    def test_nonexistent_dir_returns_empty(self):
        pipelines = load_all_pipelines(Path("/nonexistent/path"))
        assert pipelines == []
