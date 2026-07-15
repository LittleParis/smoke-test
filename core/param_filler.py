"""参数填充：用预取缓存替换占位参数。

从 tests/test_smoke.py 抽离，便于单元测试覆盖。
"""
from __future__ import annotations

from generators.data_generator import BOOL_DEFAULT_TRUE, COMMON_PARAMS
from generators.data_prefetch import get_param_value


def fill_params_from_cache(params: dict, module: str, cache: dict, case_type: str = "positive") -> dict:
    """用预取缓存替换占位参数（原地修改并返回 params）。

    正向详情接口：缓存无匹配则删除参数（避免传 Faker 假值）
    正向列表接口：只补充有缓存值的过滤参数，不删除已有参数
    组合查询：只替换 __cache__ 占位符，不修改枚举/布尔等已确定的值
    """
    is_list = "SkipCount" in params or "MaxResultCount" in params
    for name in list(params.keys()):
        if name in COMMON_PARAMS or name in BOOL_DEFAULT_TRUE:
            continue
        value = params[name]
        # __cache__ 占位符：替换为缓存值
        if isinstance(value, str) and value.startswith("__cache__"):
            cached_value = get_param_value(name, module, cache)
            if cached_value is not None:
                params[name] = cached_value
            else:
                print(f"[Warning] 缓存未命中，删除参数: {name} (module={module})")
                del params[name]
            continue
        # 非 __cache__ 参数：仅正向用例做缓存替换/删除
        if case_type == "positive":
            cached_value = get_param_value(name, module, cache)
            if cached_value is not None:
                params[name] = cached_value
            elif not is_list:
                del params[name]
    return params


def inject_list_filter_params(params: dict, module: str, cache: dict) -> dict:
    """正向列表接口：从缓存中注入过滤参数（如导出接口需要 CarNo 限制范围）。

    原地修改并返回 params。
    """
    if "CarNo" not in params:
        car_no = get_param_value("CarNo", module, cache)
        if car_no is not None:
            params["CarNo"] = car_no
    if "KeyNo" not in params:
        key_no = get_param_value("KeyNo", module, cache)
        if key_no is not None:
            params["KeyNo"] = key_no
    return params
