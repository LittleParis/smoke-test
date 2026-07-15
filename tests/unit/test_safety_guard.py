"""core.safety_guard 单元测试。"""
import pytest

from core.pipeline_loader import PipelineConfig, StepConfig
from core.safety_guard import SafetyViolation, ensure_pipeline_safe


def _pipeline(method="GET", endpoint="/api/Test/Get"):
    return PipelineConfig(
        name="test",
        module="Test",
        steps=[StepConfig(name="step", endpoint=endpoint, method=method)],
    )


def test_allows_get_on_demo_host():
    ensure_pipeline_safe(
        _pipeline(),
        base_url="https://api.demo.example.com",
        environment="demo",
        allowed_hosts=["api.demo.example.com"],
    )


def test_rejects_production_environment():
    with pytest.raises(SafetyViolation, match="不允许在环境"):
        ensure_pipeline_safe(
            _pipeline(),
            base_url="https://api.example.com",
            environment="production",
            allowed_hosts=["api.example.com"],
        )


def test_rejects_host_outside_allowlist():
    with pytest.raises(SafetyViolation, match="主机不在"):
        ensure_pipeline_safe(
            _pipeline(),
            base_url="https://api.production.example.com",
            environment="demo",
            allowed_hosts=["api.demo.example.com"],
        )


def test_rejects_write_method():
    with pytest.raises(SafetyViolation, match="不允许执行 POST"):
        ensure_pipeline_safe(
            _pipeline(method="POST"),
            base_url="https://api.demo.example.com",
            environment="demo",
            allowed_hosts=["api.demo.example.com"],
        )


def test_rejects_side_effect_get():
    with pytest.raises(SafetyViolation, match="副作用接口黑名单"):
        ensure_pipeline_safe(
            _pipeline(endpoint="/api/Complaint/RemoveComplaintType"),
            base_url="https://api.demo.example.com",
            environment="demo",
            allowed_hosts=["api.demo.example.com"],
        )
