from config.test_data import TEST_DATA

# 各模块要从列表响应中提取的字段
# key: 缓存中存储的字段名, value: 列表响应中的字段名
MODULE_FIELD_MAPPING = {
    "Complaint": {
        "id": ["id"],
        "orderNo": ["selfOrderNo", "orderNo"],
        "complainantPhone": ["complainantPhone"],
        "complainantName": ["complainantName"],
    },
    "Accident": {
        "accidentId": ["accidentId"],
        "orderNo": ["orderNo"],
        "carNo": ["carNo"],
        "acctId": ["acctId"],
    },
    "AfterSaleSetting": {
        "id": ["id"],
        "itemId": ["itemId"],
    },
    "Repair": {
        "repairId": ["repairId"],
        "carNo": ["carNo"],
        "orderNo": ["orderNo", "selfOrderNo"],
        "id": ["id"],
        "userPhone": ["userPhone"],
        "ticketId": ["ticketId"],
        "key": ["key"],
        "keyNo": ["repairId"],  # GetActionLogs/GetOperationLogs 用
    },
    "Annual": {
        "carNo": ["carNo"],
        "orderNo": ["orderNo"],
    },
}


def is_list_interface(iface: dict) -> bool:
    """判断是否为列表接口（有分页参数）"""
    for p in iface.get("query_params", []):
        if p["name"] in ("MaxResultCount", "SkipCount"):
            return True
    return False


def prefetch_module_data(http_client, interfaces: list[dict], default_platform: str = "MyEhi") -> dict:
    """
    从列表接口预取业务数据

    返回: {模块名: {字段名: 值}}
    """
    cache = {}

    # 按模块分组列表接口
    list_interfaces = [i for i in interfaces if is_list_interface(i) and i["method"] == "GET"]

    for iface in list_interfaces:
        module = iface.get("feature", "")
        if module not in MODULE_FIELD_MAPPING:
            continue

        field_mapping = MODULE_FIELD_MAPPING.get(module, {})

        # 跳过已提取完所有字段的模块
        if module in cache:
            existing = set(cache[module].keys())
            needed = set(field_mapping.keys())
            if needed.issubset(existing):
                continue

        endpoint = iface["endpoint"]
        params = {"Platform": default_platform}

        try:
            if iface["method"] == "GET":
                resp = http_client.get(endpoint, params=params)
            else:
                continue

            if resp.status_code != 200:
                continue

            data = resp.json()
            if not data.get("isSuccess"):
                continue

            # 从响应中提取第一条数据的字段
            result = data.get("result", {})
            items = result.get("items", []) if isinstance(result, dict) else []

            if not items:
                # 有些接口 result 直接是列表
                items = result if isinstance(result, list) else []

            if items and len(items) > 0:
                first_item = items[0]
                module_cache = cache.get(module, {})
                for cache_key, response_keys in field_mapping.items():
                    if cache_key in module_cache:
                        continue  # 已有，跳过
                    for rk in response_keys:
                        if rk in first_item:
                            module_cache[cache_key] = first_item[rk]
                            break
                if module_cache:
                    cache[module] = module_cache
                    print(f"[Prefetch] {module}: {module_cache}")

        except Exception as e:
            print(f"[Prefetch] Failed {endpoint}: {e}")
            continue

    # 合并手动兜底数据
    for module, manual_data in TEST_DATA.items():
        if module not in cache:
            cache[module] = manual_data
            print(f"[Prefetch] Using manual data for {module}: {manual_data}")

    return cache


def get_param_value(param_name: str, module: str, cache: dict) -> any:
    """从缓存中获取参数值（忽略大小写）"""
    module_cache = cache.get(module, {})
    param_lower = param_name.lower()

    # 精确匹配
    if param_name in module_cache:
        return module_cache[param_name]

    # 忽略大小写匹配
    for key, value in module_cache.items():
        if key.lower() == param_lower:
            return value

    # 特殊映射：ComplaintId -> id, AccidentId -> accidentId
    if param_lower.endswith("id") and len(param_lower) > 2:
        base_id = param_lower.replace("id", "").replace("Id", "")
        for key in ["id", f"{base_id}id", f"{base_id}Id"]:
            if key in module_cache:
                return module_cache[key]
        # 最后兜底：任何以 id 结尾的参数尝试匹配 id 字段
        if "id" in module_cache:
            return module_cache["id"]

    return None