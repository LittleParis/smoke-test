import json
from utils.boundary_rules import DOTNET_ENUM_BLACKLIST

# 操作类型识别关键词
CRUD_KEYWORDS = {
    "create": ["添加", "创建", "新增", "登记"],
    "delete": ["删除", "取消"],
    "update": ["修改", "更新", "保存", "配置"],
    "read": ["获取", "查询"],
}


def classify_operation(method: str, summary: str) -> str:
    if method == "GET":
        return "read"
    for op_type, keywords in CRUD_KEYWORDS.items():
        if any(kw in summary for kw in keywords):
            return op_type
    return "read"  # 默认归为查询


def parse_swagger_file(file_path: str) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as f:
        spec = json.load(f)

    schemas = spec.get("components", {}).get("schemas", {})
    enums = _extract_enums(schemas)
    paths = spec.get("paths", {})
    interfaces = []

    for endpoint, methods in paths.items():
        for method, detail in methods.items():
            if method not in ("get", "post", "put", "patch", "delete"):
                continue

            summary = detail.get("summary", "")
            operation_type = classify_operation(method, summary)
            tags = detail.get("tags", ["Unknown"])
            feature = tags[0] if tags else "Unknown"

            # 提取 query 参数
            query_params = []
            for p in detail.get("parameters", []):
                if p.get("in") == "query":
                    param_info = {
                        "name": p["name"],
                        "required": p.get("required", False),
                        "description": p.get("description", ""),
                        "schema": _resolve_schema(p.get("schema", {}), schemas),
                    }
                    query_params.append(param_info)

            # 提取 request body schema
            request_body_schema = {}
            request_body = detail.get("requestBody", {})
            if request_body:
                content = request_body.get("content", {})
                for ct, ct_detail in content.items():
                    schema_ref = ct_detail.get("schema", {})
                    request_body_schema = _resolve_schema(schema_ref, schemas)
                    break

            interfaces.append({
                "endpoint": endpoint,
                "method": method.upper(),
                "summary": summary,
                "feature": feature,
                "operation_type": operation_type,
                "query_params": query_params,
                "request_body_schema": request_body_schema,
                "enums": enums,
            })

    return interfaces


def _extract_enums(schemas: dict) -> dict[str, list[str]]:
    enums = {}
    for name, schema in schemas.items():
        if "enum" in schema:
            filtered = [v for v in schema["enum"] if v not in DOTNET_ENUM_BLACKLIST]
            if filtered:
                enums[name] = filtered
    return enums


def _resolve_schema(schema: dict, all_schemas: dict, depth: int = 0) -> dict:
    if depth > 5:
        return schema

    ref = schema.get("$ref", "")
    if ref:
        ref_name = ref.rsplit("/", 1)[-1]
        resolved = all_schemas.get(ref_name, {})
        return _resolve_schema(resolved, all_schemas, depth + 1)

    result = dict(schema)

    if "properties" in result:
        resolved_props = {}
        for prop_name, prop_schema in result["properties"].items():
            resolved_props[prop_name] = _resolve_schema(prop_schema, all_schemas, depth + 1)
        result["properties"] = resolved_props

    return result
