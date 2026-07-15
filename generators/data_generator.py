import os

from allpairspy import AllPairs
from faker import Faker

from generators.data_prefetch import is_list_interface
from utils.boundary_rules import BOUNDARY_RULES, FIELD_KEYWORD_RULES

fake = Faker("zh_CN")

# 公共参数，不需要从缓存填充
COMMON_PARAMS = {"Platform", "SkipCount", "MaxResultCount", "IsTrack", "OperatorId", "QueryWriteDb"}

# 用例类型开关（可通过环境变量覆盖）
ENABLE_BOUNDARY_CASES = os.getenv("ENABLE_BOUNDARY_CASES", "false").lower() == "true"


def generate_test_cases(interfaces: list[dict], default_platform: str = "MyEhi") -> list[dict]:
    cases = []
    for iface in interfaces:
        # 只生成查询接口的用例
        if iface["operation_type"] != "read":
            continue

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
            "is_list": is_list_interface(iface),
        })

        # 列表接口：生成组合查询用例
        if is_list_interface(iface) and iface["method"] == "GET":
            combo_cases = _generate_combo_cases(iface, default_platform)
            cases.extend(combo_cases)

        # 边界值用例（默认关闭，通过环境变量启用）
        if ENABLE_BOUNDARY_CASES:
            boundary_cases = _generate_boundary_cases(iface, default_platform)
            cases.extend(boundary_cases)

    return cases


# 布尔型参数默认给 true（如 IsAuth、IncludeRs）
BOOL_DEFAULT_TRUE = {"IsAuth", "IncludeRs", "isAuth", "includeRs"}

# 可用于组合查询的缓存参数（运行时从预取缓存填值）
COMBO_CACHE_PARAMS = {
    "CarNo", "carNo", "OrderNo", "orderNo", "RepairId", "repairId",
    "AcctId", "acctId", "Id", "id", "UserPhone", "userPhone",
    "Phone", "phone", "AccidentId", "accidentId", "ItemId", "itemId",
}


def _generate_combo_cases(iface: dict, default_platform: str) -> list[dict]:
    """为列表接口生成 Pairwise 正交组合查询用例"""
    cases = []

    # 收集可用业务参数的候选值列表
    param_values = []
    for p in iface.get("query_params", []):
        name = p["name"]
        if name in COMMON_PARAMS or name in BOOL_DEFAULT_TRUE:
            continue
        schema = p.get("schema", {})
        ptype = schema.get("type", "string")

        candidates = []
        # 优先级1: 缓存参数（运行时从预取缓存填值，单值）
        if name in COMBO_CACHE_PARAMS:
            candidates.append((name, f"__cache__{name}"))
        # 优先级2: 枚举参数（取前2个有效值，Pairwise 可交互组合）
        elif "enum" in schema:
            valid = [v for v in schema["enum"] if isinstance(v, (str, int)) and not str(v).startswith("__")]
            for v in valid[:2]:
                candidates.append((name, v))
        # 优先级3: 布尔参数（True + False）
        elif ptype == "boolean":
            candidates.append((name, True))
            candidates.append((name, False))

        if candidates:
            param_values.append(candidates)

    if not param_values:
        return cases

    # 单参数：每个 candidate 包装成单元素列表，保持与 AllPairs 输出结构一致
    # 多参数：用 AllPairs 正交组合，每个 combo 是 [(name, value), ...] 列表
    if len(param_values) == 1:
        combos = [[c] for c in param_values[0]]
    else:
        combos = AllPairs(param_values)

    for combo in combos:
        params = {"Platform": default_platform, "SkipCount": 0, "MaxResultCount": 10}
        param_names = []
        for name, value in combo:
            params[name] = value
            param_names.append(name)
        cases.append({
            "name": f"{iface['summary']}-组合查询-{'+'.join(param_names)}",
            "feature": iface["feature"],
            "story": iface["operation_type"],
            "endpoint": iface["endpoint"],
            "method": iface["method"],
            "case_type": "pairwise",
            "params": params,
            "expect": {"status": 200},
            "is_list": True,
        })

    return cases


def _generate_positive_params(iface: dict, default_platform: str) -> dict:
    params = {}
    is_list = is_list_interface(iface)

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
        elif name in COMMON_PARAMS:
            continue
        elif name in BOOL_DEFAULT_TRUE:
            params[name] = True
        elif is_list:
            continue
        else:
            params[name] = _generate_value_by_type(name, ptype, schema)

    # Request body 参数（POST 查询接口）
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
    """从 schema 生成请求体。

    仅生成 required 字段，保证每次运行用例一致（避免随机性导致不可复现）。
    """
    properties = schema.get("properties", {})
    required_fields = schema.get("required", [])
    if not properties:
        return {}

    body = {}
    for prop_name in required_fields:
        if prop_name in properties:
            prop_schema = properties[prop_name]
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
