"""HTTP 请求执行：按用例配置发送请求并返回响应。

从 tests/test_smoke.py 的请求分发逻辑抽离，便于后续在 pipeline 执行器中复用。
"""
from __future__ import annotations

import requests

from utils.http_client import HttpClient


def execute_case(
    http_client: HttpClient,
    method: str,
    endpoint: str,
    params: dict | None = None,
    body: dict | None = None,
) -> requests.Response:
    """按用例配置发送 HTTP 请求。

    GET  → params
    POST → params + json body（可选）
    其他 → params
    """
    params = params or {}
    method = method.upper()

    if method == "GET":
        return http_client.get(endpoint, params=params)
    if method == "POST":
        kwargs: dict = {"params": params}
        if body:
            kwargs["json"] = body
        return http_client.post(endpoint, **kwargs)
    return http_client.request(method, endpoint, params=params)
