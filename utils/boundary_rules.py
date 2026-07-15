BOUNDARY_RULES = {
    "string": [
        "",
        " ",
        "a" * 256,
        "<script>alert(1)</script>",
        "'; DROP TABLE users--",
    ],
    "integer": [
        0,
        -1,
        999999999,
        1.5,
    ],
    "boolean": [],
    "email": [
        "",
        "notanemail",
        "a@b",
    ],
    "phone": [
        "",
        "abc",
        "123",
        "1" * 20,
    ],
}

# 字段名关键词 → 边界值类型的映射
FIELD_KEYWORD_RULES = {
    "email": "email",
    "phone": "phone",
    "mobile": "phone",
    "tel": "phone",
}

# .NET 枚举污染过滤
DOTNET_ENUM_BLACKLIST = {
    "HasFlag", "Equals", "GetHashCode", "CompareTo",
    "ToString", "GetTypeCode", "GetType", "value__",
}
