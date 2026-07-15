"""日志和测试报告中的敏感字段脱敏。"""
from __future__ import annotations

import re
from typing import Any

REDACTED = "***REDACTED***"
SENSITIVE_KEY_PARTS = {
    "authorization",
    "cookie",
    "password",
    "secret",
    "token",
    "webhook",
}


def redact_sensitive(value: Any) -> Any:
    """递归脱敏字典和列表，不修改原对象。"""
    if isinstance(value, dict):
        return {
            key: REDACTED if _is_sensitive_key(str(key)) else redact_sensitive(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [redact_sensitive(item) for item in value]
    if isinstance(value, tuple):
        return tuple(redact_sensitive(item) for item in value)
    return value


def redact_text(text: str) -> str:
    """脱敏无法解析为 JSON 的文本响应及常见认证头。"""
    redacted = re.sub(r"(?i)Bearer\s+[A-Za-z0-9._~+/=-]+", f"Bearer {REDACTED}", text)
    for key_part in SENSITIVE_KEY_PARTS:
        pattern = rf'(?i)(["\']?[^"\'\s:=]*{re.escape(key_part)}[^"\'\s:=]*["\']?\s*[:=]\s*["\']?)([^,"\'\s}}]+)'
        redacted = re.sub(pattern, rf"\1{REDACTED}", redacted)
    return redacted


def _is_sensitive_key(key: str) -> bool:
    normalized = key.lower().replace("-", "").replace("_", "")
    return any(part in normalized for part in SENSITIVE_KEY_PARTS)
