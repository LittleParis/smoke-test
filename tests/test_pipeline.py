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
from utils.http_client import HttpClient


@pytest.fixture(scope="session")
def http_client():
    """登录后的 HTTP 客户端（session 级共享）"""
    client = HttpClient(
        base_url=settings.BASE_URL,
        login_url=settings.LOGIN_URL,
        login_return_url=settings.LOGIN_RETURN_URL,
        verify_ssl=settings.VERIFY_SSL,
    )
    assert client.login(settings.USERNAME, settings.PASSWORD), "Login failed"
    yield client


@pytest.fixture(scope="session")
def pipeline_configs():
    """加载所有启用的业务流程配置"""
    return load_all_pipelines()


@pytest.fixture(scope="session")
def prefetch_cache(http_client, pipeline_configs):
    """预取数据缓存。

    合并所有 pipeline 的 prefetch 配置，调用各自的列表接口提取字段。
    返回: {模块: {字段: 值}}
    """
    from generators.data_prefetch import MODULE_FIELD_MAPPING, prefetch_module_data
    from generators.swagger_parser import parse_swagger_file

    # 构建 prefetch 用的 interfaces 列表（从 pipeline 配置推导）
    interfaces = []
    for cfg in pipeline_configs:
        if cfg.prefetch.endpoint and cfg.module:
            interfaces.append({
                "endpoint": cfg.prefetch.endpoint,
                "method": "GET",
                "feature": cfg.module,
                "query_params": [
                    {"name": "MaxResultCount", "required": False, "schema": {}},
                    {"name": "SkipCount", "required": False, "schema": {}},
                ],
            })

    # 同时合并 swagger 中的列表接口（用于 MODULE_FIELD_MAPPING 驱动的预取）
    try:
        swagger_interfaces = parse_swagger_file(settings.SWAGGER_FILE)
        if settings.TEST_MODULES:
            swagger_interfaces = [i for i in swagger_interfaces if i["feature"] in settings.TEST_MODULES]
        interfaces.extend(swagger_interfaces)
    except Exception as e:
        print(f"[Prefetch] swagger 解析失败，仅用 pipeline 配置: {e}")

    return prefetch_module_data(http_client, interfaces, settings.DEFAULT_PLATFORM)


def _pipeline_test_id(cfg: PipelineConfig) -> str:
    """生成 pytest 的测试 ID"""
    return f"{cfg.module}-{cfg.name}"


@pytest.mark.parametrize(
    "pipeline",
    [pytest.param(cfg, id=_pipeline_test_id(cfg)) for cfg in load_all_pipelines()],
)
def test_pipeline(pipeline, http_client, prefetch_cache):
    """执行单个业务流程冒烟测试"""
    result: PipelineResult = run_pipeline(pipeline, http_client, prefetch_cache)

    # 附件：完整流程结果摘要
    summary = {
        "pipeline": pipeline.name,
        "module": pipeline.module,
        "success": result.success,
        "steps": [
            {
                "name": r.step_name,
                "success": r.success,
                "error": r.error,
                "extracted": r.extracted,
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
