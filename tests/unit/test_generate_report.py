"""generate_report 报告附件收集测试。"""
from generate_report import collect_result_details, generate_html, iter_allure_attachments


def test_iter_allure_attachments_recurses_steps():
    result = {
        "attachments": [{"name": "流程结果摘要", "source": "summary.json"}],
        "steps": [
            {
                "attachments": [{"name": "请求参数", "source": "request.json"}],
                "steps": [{"attachments": [{"name": "响应内容", "source": "response.json"}]}],
            }
        ],
    }
    assert [item["source"] for item in iter_allure_attachments(result)] == [
        "summary.json",
        "request.json",
        "response.json",
    ]


def test_collect_result_details_keeps_multiple_steps():
    result = {
        "attachments": [{"name": "流程结果摘要", "source": "summary.json"}],
        "steps": [
            {"attachments": [{"name": "请求参数", "source": "request1.json"}]},
            {"attachments": [{"name": "请求参数", "source": "request2.json"}]},
        ],
    }
    attachments = {
        "summary.json": {"success": True},
        "request1.json": {"id": 1},
        "request2.json": {"id": 2},
    }
    details = collect_result_details(result, attachments)
    assert details["pipeline_summary"] == {"success": True}
    assert len(details["requests"]) == 2


def test_generate_html_escapes_response_content(tmp_path):
    output = tmp_path / "report.html"
    results = [{
        "name": "<script>alert(1)</script>",
        "status": "failed",
        "labels": [{"name": "feature", "value": "Demo"}],
        "attachments": [{"name": "响应内容", "source": "response.json"}],
    }]
    generate_html(results, {"response.json": {"value": "<img src=x onerror=alert(1)>"}}, output)
    content = output.read_text(encoding="utf-8")
    assert "<script>alert(1)</script>" not in content
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in content
    assert "&lt;img src=x onerror=alert(1)&gt;" in content
