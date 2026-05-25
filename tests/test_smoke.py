import allure
import pytest


def test_crud_smoke(case, http_client):
    params = dict(case["params"])
    body = params.pop("_body", None)

    allure.dynamic.feature(case["feature"])
    allure.dynamic.story(case["story"])
    allure.dynamic.title(case["name"])

    with allure.step(f"{case['method']} {case['endpoint']}"):
        if case["method"] == "GET":
            response = http_client.get(case["endpoint"], params=params)
        elif case["method"] == "POST":
            kwargs = {"params": params}
            if body:
                kwargs["json"] = body
            response = http_client.post(case["endpoint"], **kwargs)
        else:
            response = http_client.request(case["method"], case["endpoint"], params=params)

    allure.attach(str(params), name="请求参数", attachment_type=allure.attachment_type.JSON)
    allure.attach(response.text[:2000], name="响应内容", attachment_type=allure.attachment_type.JSON)

    assert response.status_code == case["expect"]["status"]
    body_json = response.json()
    assert "isSuccess" in body_json
    assert "errorCode" in body_json

    if case["case_type"] == "positive":
        assert body_json["isSuccess"] is True, f"message={body_json.get('message')}"
        assert body_json["errorCode"] == 0
    elif case["case_type"] == "boundary":
        assert body_json["isSuccess"] is False, f"Boundary input accepted: {case['name']}"