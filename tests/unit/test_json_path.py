"""core.json_path 单元测试。"""
from core.json_path import MISSING, get_json_path, read_json_path, traverse_json


def test_reads_dot_and_bracket_paths():
    data = {"result": {"items": [{"id": 42}]}}
    assert get_json_path(data, "result.items.0.id") == 42
    assert get_json_path(data, "result.items[0].id") == 42


def test_distinguishes_missing_from_none():
    data = {"result": {"value": None}}
    assert read_json_path(data, "result.value") == (True, None)
    assert read_json_path(data, "result.missing") == (False, None)


def test_result_shorthand():
    assert get_json_path({"result": {"id": 1}}, "id", result_shorthand=True) == 1


def test_traverse_missing_sentinel():
    assert traverse_json({"items": []}, ["items", "0"]) is MISSING
