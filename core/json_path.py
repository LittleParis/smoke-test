"""轻量 JSON 路径读取工具。

支持 ``result.items.0.id`` 和 ``result.items[0].id`` 两种写法，并能区分
“路径不存在”和“路径存在但值为 None”。
"""
from __future__ import annotations

import re
from typing import Any

MISSING = object()


def read_json_path(data: Any, path: str, *, result_shorthand: bool = False) -> tuple[bool, Any]:
    """读取 JSON 路径，返回 ``(是否存在, 值)``。"""
    parts = _path_parts(path)
    if not parts:
        return False, None

    if result_shorthand and parts[0] != "result":
        value = traverse_json(data, ["result", *parts])
        if value is not MISSING:
            return True, value

    value = traverse_json(data, parts)
    if value is MISSING:
        return False, None
    return True, value


def get_json_path(data: Any, path: str, *, result_shorthand: bool = False) -> Any:
    """读取 JSON 路径；路径不存在时返回 None（兼容旧调用方）。"""
    found, value = read_json_path(data, path, result_shorthand=result_shorthand)
    return value if found else None


def traverse_json(data: Any, parts: list[str]) -> Any:
    """按照拆分后的路径遍历字典和列表，缺失时返回 MISSING。"""
    current = data
    for part in parts:
        if isinstance(current, dict):
            if part not in current:
                return MISSING
            current = current[part]
        elif isinstance(current, list) and part.isdigit():
            index = int(part)
            if index < 0 or index >= len(current):
                return MISSING
            current = current[index]
        else:
            return MISSING
    return current


def _path_parts(path: str) -> list[str]:
    if not isinstance(path, str) or not path.strip():
        return []
    normalized = re.sub(r"\[(\d+)\]", r".\1", path.strip())
    return [part for part in normalized.strip(".").split(".") if part]
