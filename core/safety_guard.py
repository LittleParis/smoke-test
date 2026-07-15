"""业务流程冒烟的环境与只读接口安全保护。"""
from __future__ import annotations

from collections.abc import Collection
from urllib.parse import urlparse

from config.modules import SAFE_QUERY_POST_WHITELIST, is_side_effect_get
from core.pipeline_loader import PipelineConfig

ALLOWED_ENVIRONMENTS = {"demo", "test", "testing", "qa", "staging"}


class SafetyViolation(RuntimeError):
    """流程可能修改数据或运行在非测试环境。"""


def ensure_pipeline_safe(
    pipeline: PipelineConfig,
    *,
    base_url: str,
    environment: str,
    allowed_hosts: Collection[str],
    safe_post_endpoints: Collection[str] | None = None,
) -> None:
    """验证运行环境和流程中的每一个接口都符合只读门禁要求。"""
    environment = environment.strip().lower()
    if environment not in ALLOWED_ENVIRONMENTS:
        raise SafetyViolation(f"不允许在环境 {environment!r} 执行查询冒烟")

    hostname = (urlparse(base_url).hostname or "").lower()
    normalized_hosts = {host.strip().lower() for host in allowed_hosts if host.strip()}
    if not hostname or hostname not in normalized_hosts:
        raise SafetyViolation(f"目标主机不在测试环境白名单: {hostname or base_url}")

    safe_posts = set(safe_post_endpoints or SAFE_QUERY_POST_WHITELIST)
    for step in pipeline.steps:
        if is_side_effect_get(step.endpoint):
            raise SafetyViolation(f"步骤 {step.name} 命中副作用接口黑名单: {step.endpoint}")
        if step.method == "GET":
            continue
        if step.method == "POST" and step.endpoint in safe_posts:
            continue
        raise SafetyViolation(f"步骤 {step.name} 不允许执行 {step.method} {step.endpoint}")
