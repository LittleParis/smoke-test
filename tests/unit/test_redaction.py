"""core.redaction 单元测试。"""
from core.redaction import REDACTED, redact_sensitive, redact_text


def test_redacts_nested_sensitive_keys():
    data = {
        "username": "user",
        "password": "secret",
        "nested": {"accessToken": "abc", "value": 1},
        "items": [{"Cookie": "session=x"}],
    }
    assert redact_sensitive(data) == {
        "username": "user",
        "password": REDACTED,
        "nested": {"accessToken": REDACTED, "value": 1},
        "items": [{"Cookie": REDACTED}],
    }


def test_redacts_bearer_token_in_text():
    assert "abc.def" not in redact_text("Authorization: Bearer abc.def")
