"""仓库内真实 YAML 流程与 OpenAPI 契约的一致性测试。"""
import json

from config import settings
from core.pipeline_loader import load_all_pipelines


def _swagger_spec():
    with open(settings.SWAGGER_FILE, encoding="utf-8") as file:
        return json.load(file)


def test_core_gate_modules_are_configured():
    pipelines = load_all_pipelines()
    modules = {pipeline.module for pipeline in pipelines}
    assert {"Complaint", "Repair", "Accident"}.issubset(modules)

    for pipeline in pipelines:
        assert pipeline.version == 1
        assert {"gate", "query"}.issubset(pipeline.tags)
        assert all(step.method == "GET" for step in pipeline.steps)


def test_pipeline_endpoints_and_query_params_exist_in_swagger():
    spec = _swagger_spec()
    paths = spec["paths"]

    for pipeline in load_all_pipelines():
        for step in pipeline.steps:
            assert step.endpoint in paths, f"Swagger 中不存在接口: {step.endpoint}"
            operation = paths[step.endpoint].get(step.method.lower())
            assert operation is not None, f"Swagger 中不存在方法: {step.method} {step.endpoint}"

            query_names = {
                param["name"]
                for param in operation.get("parameters", [])
                if param.get("in") == "query"
            }
            unknown_params = set(step.params) - query_names
            assert not unknown_params, (
                f"{pipeline.module}/{step.name} 含 Swagger 未声明的查询参数: {sorted(unknown_params)}"
            )
