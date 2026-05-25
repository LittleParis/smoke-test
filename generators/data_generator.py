from faker import Faker
from utils.boundary_rules import BOUNDARY_RULES, FIELD_KEYWORD_RULES

fake = Faker("zh_CN")


def generate_test_cases(interfaces: list[dict], default_platform: str = "MyEhi") -> list[dict]:
    cases = []
    for iface in interfaces:
        # 正向用例
        positive_params = _generate_positive_params(iface, default_platform)
        cases.append({
            "name": f"{iface['summary']}-正向",
            "feature": iface["feature"],
            "story": iface["operation_type"],
            "endpoint": iface["endpoint"],
            "method": iface["method"],
            "case_type": "positive",
            "params": positive_params,
            "expect": {"status": 200},
        })

        # 边界值用例（仅增删改）
        if iface["operation_type"] in ("create", "update", "delete"):
            boundary_cases = _generate_boundary_cases(iface, default_platform)
            cases.extend(boundary_cases)

    return cases


def _generate_positive_params(iface: dict, default_platform: str) -> dict:
    params = {}

    # Query 参数
    for p in iface.get("query_params", []):
        name = p["name"]
        schema = p.get("schema", {})
        ptype = schema.get("type", "string")

        if name == "Platform":
            params[name] = default_platform
        elif name in ("SkipCount",):
            params[name] = 0
        elif name in ("MaxResultCount",):
            params[name] = 10
        elif p.get("required", False):
            params[name] = _generate_value_by_type(name, ptype, schema)

    # Request body 参数（POST 接口）
    body_schema = iface.get("request_body_schema", {})
    if body_schema and iface["method"] == "POST":
        body = _generate_body_from_schema(body_schema)
        if body:
            params["_body"] = body

    return params


def _generate_value_by_type(field_name: str, field_type: str, schema: dict = None) -> any:
    schema = schema or {}
    name_lower = field_name.lower()

    # 枚举值
    if "enum" in schema:
        valid = [v for v in schema["enum"] if isinstance(v, (str, int)) and not str(v).startswith("__")]
        if valid:
            return valid[0]

    # 字段名关键词匹配
    for keyword, rule_type in FIELD_KEYWORD_RULES.items():
        if keyword in name_lower:
            if rule_type == "email":
                return fake.email()
            elif rule_type == "phone":
                return fake.phone_number()

    # 类型匹配
    if field_type == "integer":
        return fake.random_int(min=1, max=100)
    elif field_type == "boolean":
        return True
    elif field_type == "number":
        return round(fake.pyfloat(min_value=1, max_value=100), 2)
    elif field_type == "string":
        fmt = schema.get("format", "")
        if fmt == "date-time":
            return fake.date_time_this_year().isoformat()
        return fake.word()
    return fake.word()


def _generate_body_from_schema(schema: dict) -> dict:
    properties = schema.get("properties", {})
    required_fields = schema.get("required", [])
    if not properties:
        return {}

    body = {}
    for prop_name, prop_schema in properties.items():
        if prop_name in required_fields or fake.random_int(min=0, max=1):
            ptype = prop_schema.get("type", "string")
            body[prop_name] = _generate_value_by_type(prop_name, ptype, prop_schema)
    return body


def _generate_boundary_cases(iface: dict, default_platform: str) -> list[dict]:
    cases = []

    # 对必填 query 参数生成边界值
    for p in iface.get("query_params", []):
        if not p.get("required", False):
            continue
        schema = p.get("schema", {})
        ptype = schema.get("type", "string")
        name = p["name"]
        if name == "Platform":
            continue

        rule_type = FIELD_KEYWORD_RULES.get(name.lower(), ptype)
        boundary_values = BOUNDARY_RULES.get(rule_type, BOUNDARY_RULES.get(ptype, []))

        for bv in boundary_values:
            params = {"Platform": default_platform}
            params[name] = bv
            cases.append({
                "name": f"{iface['summary']}-边界-{name}={repr(bv)[:30]}",
                "feature": iface["feature"],
                "story": iface["operation_type"],
                "endpoint": iface["endpoint"],
                "method": iface["method"],
                "case_type": "boundary",
                "params": params,
                "expect": {"status": 200},
            })

    return cases
