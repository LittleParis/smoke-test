"""业务流程冒烟测试入口（主入口）。

从 config/pipelines/*.yaml 加载业务流程，按顺序执行步骤，支持跨步骤数据传递。
这是冒烟测试的主入口，旧的 test_smoke.py（全量 swagger 扫描）默认禁用。

用法:
    pytest tests/test_pipeline.py -v          # 跑所有启用的 YAML 流程
    pytest tests/test_pipeline.py -k 投诉     # 只跑名称匹配的流程
"""
import json

import allure
import pytest

from config import settings
from core.pipeline_executor import PipelineResult, run_pipeline
from core.pipeline_loader import PipelineConfig, load_all_pipelines
from core.redaction import redact_sensitive


def _pipeline_test_id(cfg: PipelineConfig) -> str:
    """生成 pytest 的测试 ID"""
    return f"{cfg.module}-{cfg.name}"


@pytest.mark.parametrize(
    "pipeline",
    [pytest.param(cfg, id=_pipeline_test_id(cfg)) for cfg in load_all_pipelines()],
)
def test_pipeline(pipeline, http_client):
    """执行单个业务流程冒烟测试"""
    variables = {"platform": settings.DEFAULT_PLATFORM}
    result: PipelineResult = run_pipeline(pipeline, http_client, variables)

    allure.dynamic.feature(pipeline.module)
    allure.dynamic.story("query-pipeline")
    allure.dynamic.title(pipeline.name)

    # 附件：完整流程结果摘要
    summary = {
        "pipeline": pipeline.name,
        "module": pipeline.module,
        "success": result.success,
        "duration_ms": result.duration_ms,
        "error_type": result.error_type,
        "steps": [
            {
                "name": r.step_name,
                "method": r.method,
                "endpoint": r.endpoint,
                "success": r.success,
                "status_code": r.status_code,
                "duration_ms": r.duration_ms,
                "error_type": r.error_type,
                "error": r.error,
                "request_params": r.request_params,
                "extracted": redact_sensitive(r.extracted),
            }
            for r in result.step_results
        ],
    }
    allure.attach(
        json.dumps(summary, ensure_ascii=False, indent=2),
        name="流程结果摘要",
        attachment_type=allure.attachment_type.JSON,
    )

    assert result.success, (
        f"流程 {pipeline.name} 失败: {result.error}\n"
        f"步骤详情: {json.dumps(summary, ensure_ascii=False, indent=2)}"
    )
