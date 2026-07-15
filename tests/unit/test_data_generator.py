"""generators.data_generator 单元测试。"""
from generators.data_generator import (
    BOOL_DEFAULT_TRUE,
    COMMON_PARAMS,
    _generate_body_from_schema,
    _generate_boundary_cases,
    _generate_combo_cases,
    _generate_positive_params,
    _generate_value_by_type,
    generate_test_cases,
)
from generators.data_prefetch import is_list_interface


def _make_iface(
    endpoint="/api/Test/Get",
    method="GET",
    summary="获取测试",
    feature="Test",
    operation_type="read",
    query_params=None,
    request_body_schema=None,
):
    """构造测试用 interface dict"""
    return {
        "endpoint": endpoint,
        "method": method,
        "summary": summary,
        "feature": feature,
        "operation_type": operation_type,
        "query_params": query_params or [],
        "request_body_schema": request_body_schema or {},
        "enums": {},
    }


class TestGenerateValueByType:
    def test_enum_returns_first_valid(self):
        schema = {"enum": ["A", "B", "C"]}
        assert _generate_value_by_type("field", "string", schema) == "A"

    def test_enum_filters_dotnet_pollution(self):
        """以 __ 开头的枚举值被过滤"""
        schema = {"enum": ["__invalid", "valid"]}
        assert _generate_value_by_type("field", "string", schema) == "valid"

    def test_integer(self):
        val = _generate_value_by_type("count", "integer", {})
        assert isinstance(val, int)
        assert 1 <= val <= 100

    def test_boolean(self):
        assert _generate_value_by_type("flag", "boolean", {}) is True

    def test_string(self):
        val = _generate_value_by_type("name", "string", {})
        assert isinstance(val, str)

    def test_email_keyword(self):
        """字段名含 email → 生成邮箱"""
        val = _generate_value_by_type("userEmail", "string", {})
        assert "@" in val

    def test_phone_keyword(self):
        """字段名含 phone → 生成电话"""
        val = _generate_value_by_type("userPhone", "string", {})
        assert isinstance(val, str)


class TestGeneratePositiveParams:
    def test_list_interface_only_common_params(self):
        """列表接口：只生成 Platform/SkipCount/MaxResultCount，不生成业务参数"""
        iface = _make_iface(query_params=[
            {"name": "Platform", "required": True, "schema": {"type": "string"}},
            {"name": "SkipCount", "required": False, "schema": {"type": "integer"}},
            {"name": "MaxResultCount", "required": False, "schema": {"type": "integer"}},
            {"name": "CarNo", "required": False, "schema": {"type": "string"}},
        ])
        params = _generate_positive_params(iface, "MyEhi")
        assert params["Platform"] == "MyEhi"
        assert params["SkipCount"] == 0
        assert params["MaxResultCount"] == 10
        assert "CarNo" not in params  # 列表接口不生成业务参数

    def test_detail_interface_generates_business_params(self):
        """详情接口：生成业务参数（Faker 占位值）"""
        iface = _make_iface(query_params=[
            {"name": "Platform", "required": True, "schema": {"type": "string"}},
            {"name": "id", "required": True, "schema": {"type": "integer"}},
        ])
        params = _generate_positive_params(iface, "MyEhi")
        assert params["Platform"] == "MyEhi"
        assert "id" in params

    def test_bool_default_true(self):
        """IsAuth/IncludeRs 默认 True"""
        iface = _make_iface(query_params=[
            {"name": "IsAuth", "required": False, "schema": {"type": "boolean"}},
        ])
        params = _generate_positive_params(iface, "MyEhi")
        assert params["IsAuth"] is True


class TestGenerateBodyFromSchema:
    def test_only_required_fields(self):
        """仅生成 required 字段"""
        schema = {
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "email": {"type": "string"},
            },
            "required": ["name", "age"],
        }
        body = _generate_body_from_schema(schema)
        assert "name" in body
        assert "age" in body
        assert "email" not in body  # 非必填不生成

    def test_empty_properties(self):
        assert _generate_body_from_schema({"properties": {}}) == {}

    def test_no_required(self):
        """无 required → 空 body"""
        schema = {
            "properties": {"name": {"type": "string"}},
            "required": [],
        }
        assert _generate_body_from_schema(schema) == {}

    def test_deterministic(self):
        """多次调用结果字段名一致（值可能因 Faker 不同，但字段集稳定）"""
        schema = {
            "properties": {
                "a": {"type": "string"},
                "b": {"type": "integer"},
            },
            "required": ["a", "b"],
        }
        b1 = _generate_body_from_schema(schema)
        b2 = _generate_body_from_schema(schema)
        assert set(b1.keys()) == set(b2.keys()) == {"a", "b"}


class TestGenerateBoundaryCases:
    def test_generates_for_required_params(self):
        """对必填参数生成边界值用例"""
        iface = _make_iface(query_params=[
            {"name": "Platform", "required": True, "schema": {"type": "string"}},
            {"name": "keyword", "required": True, "schema": {"type": "string"}},
        ])
        cases = _generate_boundary_cases(iface, "MyEhi")
        # Platform 被跳过，只对 keyword 生成
        assert len(cases) > 0
        for c in cases:
            assert c["case_type"] == "boundary"
            assert c["expect"]["status"] == 200
            assert "keyword" in c["params"]
            assert c["params"]["Platform"] == "MyEhi"

    def test_skips_optional_params(self):
        """非必填参数不生成边界用例"""
        iface = _make_iface(query_params=[
            {"name": "keyword", "required": False, "schema": {"type": "string"}},
        ])
        cases = _generate_boundary_cases(iface, "MyEhi")
        assert len(cases) == 0


class TestGenerateTestCases:
    def test_skip_non_read_operation(self):
        """非 read 接口不生成用例"""
        iface = _make_iface(operation_type="create")
        cases = generate_test_cases([iface], "MyEhi")
        assert len(cases) == 0

    def test_positive_case_generated(self):
        """read 接口生成正向用例"""
        iface = _make_iface()
        cases = generate_test_cases([iface], "MyEhi")
        assert len(cases) == 1
        assert cases[0]["case_type"] == "positive"

    def test_list_interface_generates_combo(self):
        """列表接口额外生成组合查询用例"""
        iface = _make_iface(query_params=[
            {"name": "Platform", "required": True, "schema": {"type": "string"}},
            {"name": "SkipCount", "required": False, "schema": {"type": "integer"}},
            {"name": "MaxResultCount", "required": False, "schema": {"type": "integer"}},
            # 用非 BOOL_DEFAULT_TRUE 的布尔参数，确保进入组合查询
            {"name": "IncludeDeleted", "required": False, "schema": {"type": "boolean"}},
        ])
        cases = generate_test_cases([iface], "MyEhi")
        # 1 正向 + 至少 1 组合查询（IncludeDeleted 是布尔参数）
        assert len(cases) >= 2
        case_types = {c["case_type"] for c in cases}
        assert "positive" in case_types
        assert "pairwise" in case_types


class TestIsListInterface:
    def test_with_pagination_params(self):
        iface = _make_iface(query_params=[
            {"name": "MaxResultCount", "required": False, "schema": {}},
        ])
        assert is_list_interface(iface) is True

    def test_without_pagination_params(self):
        iface = _make_iface(query_params=[
            {"name": "id", "required": True, "schema": {}},
        ])
        assert is_list_interface(iface) is False
