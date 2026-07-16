"""售后系统本地 HTTP Mock 服务。

使用标准库启动真实 HTTP 服务，模拟 CSRF 登录、302 跳转、Cookie 会话和三条
查询业务流程所需的六个接口。
"""
from __future__ import annotations

import json
import threading
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import parse_qs, urlparse


@dataclass
class RecordedRequest:
    method: str
    path: str
    query: dict[str, list[str]] = field(default_factory=dict)


@dataclass
class MockServerState:
    api_requests: list[RecordedRequest] = field(default_factory=list)
    fail_endpoint: str = ""


class MockAfterSaleServer:
    """可作为上下文管理器使用的本地售后 API Mock 服务。"""

    def __init__(self) -> None:
        self.state = MockServerState()
        handler = _create_handler(self.state)
        self._server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        self._server.daemon_threads = True
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)

    @property
    def base_url(self) -> str:
        host, port = self._server.server_address
        return f"http://{host}:{port}"

    @property
    def login_url(self) -> str:
        return f"{self.base_url}/Account/Login"

    @property
    def return_url(self) -> str:
        return f"{self.base_url}/return"

    def start(self) -> "MockAfterSaleServer":
        self._thread.start()
        return self

    def stop(self) -> None:
        self._server.shutdown()
        self._server.server_close()
        self._thread.join(timeout=2)

    def __enter__(self) -> "MockAfterSaleServer":
        return self.start()

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.stop()


def _create_handler(state: MockServerState) -> type[BaseHTTPRequestHandler]:
    class MockHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
            parsed = urlparse(self.path)
            if parsed.path == "/Account/Login":
                self._send_html(
                    '<html><body><input name="__RequestVerificationToken" '
                    'value="mock-csrf-token"></body></html>'
                )
                return

            if parsed.path.startswith("/api/"):
                self._handle_api("GET", parsed.path, parse_qs(parsed.query))
                return

            self._send_json(404, {"isSuccess": False, "errorCode": 404, "message": "Not found"})

        def do_POST(self) -> None:  # noqa: N802 - BaseHTTPRequestHandler API
            parsed = urlparse(self.path)
            if parsed.path == "/Account/Login":
                self._handle_login()
                return
            if parsed.path.startswith("/api/"):
                self._handle_api("POST", parsed.path, parse_qs(parsed.query))
                return
            self._send_json(404, {"isSuccess": False, "errorCode": 404, "message": "Not found"})

        def _handle_login(self) -> None:
            length = int(self.headers.get("Content-Length", "0"))
            form = parse_qs(self.rfile.read(length).decode("utf-8"))
            valid = (
                form.get("username") == ["mock-user"]
                and form.get("plainPassword") == ["mock-password"]
                and form.get("__RequestVerificationToken") == ["mock-csrf-token"]
            )
            if not valid:
                self._send_json(401, {"isSuccess": False, "errorCode": 401, "message": "Login failed"})
                return

            self.send_response(302)
            self.send_header("Location", "/return")
            self.send_header("Set-Cookie", "mock_session=authenticated; Path=/; HttpOnly")
            self.send_header("Content-Length", "0")
            self.end_headers()

        def _handle_api(self, method: str, path: str, query: dict[str, list[str]]) -> None:
            state.api_requests.append(RecordedRequest(method=method, path=path, query=query))

            if "mock_session=authenticated" not in self.headers.get("Cookie", ""):
                self._send_json(401, {"isSuccess": False, "errorCode": 401, "message": "Unauthorized"})
                return

            if path == state.fail_endpoint:
                self._send_json(
                    200,
                    {"isSuccess": False, "errorCode": 9001, "message": "Mock business failure", "result": None},
                )
                return

            response = _api_response(path, query)
            if response is None:
                self._send_json(404, {"isSuccess": False, "errorCode": 404, "message": "Unknown API"})
                return
            self._send_json(200, response)

        def _send_html(self, content: str) -> None:
            body = content.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def _send_json(self, status: int, content: dict[str, Any]) -> None:
            body = json.dumps(content, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format: str, *args: Any) -> None:
            return

    return MockHandler


def _api_response(path: str, query: dict[str, list[str]]) -> dict[str, Any] | None:
    common = {"isSuccess": True, "errorCode": 0, "message": "OK"}

    if path == "/api/Complaint/GetComplaints":
        return {**common, "result": {"items": [{"id": 52, "selfOrderNo": "MOCK-C-001"}], "totalCount": 1}}
    if path == "/api/Complaint/GetComplaintInfo":
        complaint_id = int(_query_value(query, "id", "0"))
        return {**common, "result": {"id": complaint_id, "selfOrderNo": "MOCK-C-001"}}

    if path == "/api/Repair/GetRepairInfos":
        return {**common, "result": {"items": [{
            "repairId": "R-1001",
            "orderNo": "MOCK-ORDER-001",
            "carNo": "沪A00001",
            "acctId": "MOCK-ACCT-001",
            "extraProperties": {"OrderNo": {"encryptedContent": "MOCK-ENCRYPTED"}},
        }], "totalCount": 1}}
    if path == "/api/Repair/GetRepairInfo":
        repair_id = _query_value(query, "repairId")
        return {**common, "result": {"repairId": repair_id, "carNo": "沪A00001"}}

    # POST 解密脱敏字段：返回固定明文（mock 不做真实解密）
    if path == "/api/Common/ResolveSensitiveInfo":
        return {**common, "result": "MOCK-DECRYPTED-ORDER-NO"}

    if path == "/api/Accident/GetAccidentInfos":
        return {**common, "result": {"items": [{"accidentId": "A-2001", "carNo": "沪A00002"}], "totalCount": 1}}
    if path == "/api/Accident/GetAccidentInfo":
        accident_id = _query_value(query, "AccidentId")
        return {**common, "result": {"accidentId": accident_id, "carNo": "沪A00002"}}

    return None


def _query_value(query: dict[str, list[str]], name: str, default: str = "") -> str:
    values = query.get(name)
    return values[0] if values else default
