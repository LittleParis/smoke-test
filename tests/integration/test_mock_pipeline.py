"""使用真实 HTTP 客户端在本地 Mock 环境运行全部 YAML 流程。"""
from __future__ import annotations

import pytest

from config import settings
from core.pipeline_executor import run_pipeline
from core.pipeline_loader import load_all_pipelines
from tests.support.mock_after_sale_server import MockAfterSaleServer
from utils.http_client import HttpClient


@pytest.fixture
def mock_server():
    with MockAfterSaleServer() as server:
        yield server


@pytest.fixture
def mock_http_client(mock_server, monkeypatch):
    monkeypatch.setattr(settings, "TEST_ENVIRONMENT", "test")
    monkeypatch.setattr(settings, "ALLOWED_TEST_HOSTS", ("127.0.0.1",))

    client = HttpClient(
        base_url=mock_server.base_url,
        login_url=mock_server.login_url,
        login_return_url=mock_server.return_url,
        verify_ssl=False,
        timeout=2,
        retries=0,
    )
    assert client.login("mock-user", "mock-password") is True
    return client


@pytest.mark.integration
def test_all_yaml_pipelines_pass_against_mock_server(mock_server, mock_http_client):
    results = [
        run_pipeline(pipeline, mock_http_client, {"platform": "MyEhi"})
        for pipeline in load_all_pipelines()
    ]

    assert len(results) == 3
    assert all(result.success for result in results), [result.error for result in results]
    assert [request.path for request in mock_server.state.api_requests] == [
        "/api/Accident/GetAccidentInfos",
        "/api/Accident/GetAccidentInfo",
        "/api/Complaint/GetComplaints",
        "/api/Complaint/GetComplaintInfo",
        "/api/Repair/GetRepairInfos",
        "/api/Repair/GetRepairInfo",
    ]

    detail_queries = {
        request.path: request.query
        for request in mock_server.state.api_requests
        if request.path.endswith(("GetAccidentInfo", "GetComplaintInfo", "GetRepairInfo"))
    }
    assert detail_queries["/api/Accident/GetAccidentInfo"]["AccidentId"] == ["A-2001"]
    assert detail_queries["/api/Complaint/GetComplaintInfo"]["id"] == ["52"]
    assert detail_queries["/api/Repair/GetRepairInfo"]["repairId"] == ["R-1001"]


@pytest.mark.integration
def test_business_failure_interrupts_pipeline(mock_server, mock_http_client):
    mock_server.state.fail_endpoint = "/api/Repair/GetRepairInfo"
    repair_pipeline = next(pipeline for pipeline in load_all_pipelines() if pipeline.module == "Repair")

    result = run_pipeline(repair_pipeline, mock_http_client, {"platform": "MyEhi"})

    assert result.success is False
    assert result.error_type == "business_assertion"
    assert len(result.step_results) == 2
    assert result.step_results[0].success is True
    assert result.step_results[1].success is False
    assert "isSuccess" in result.error
