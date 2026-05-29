# Pairwise 组合查询用例生成设计

## 背景

现有烟雾测试对列表接口的组合覆盖不足：
- 正向用例只传 `{Platform, SkipCount, MaxResultCount}`，不测业务查询条件
- 组合用例（`combo_single`/`combo_multi`）只取前 1~3 个参数，每个接口最多 2 条

但实际上很多接口有大量查询条件（如 `GetAccidentInfos` 有 30 个业务参数），当前覆盖太薄。

## 目标

对列表接口生成 Pairwise 正交组合用例，用较少用例数覆盖任意两参数的交互。

## 设计

### 参数分类与取值

对每个列表接口的 query 参数，按优先级分为 3 类取值来源：

| 参数类别 | 识别方式 | 取值来源 | 示例 |
|---------|---------|---------|------|
| 缓存参数 | 参数名在 `COMBO_CACHE_PARAMS` 中 | prefetch 缓存（运行时替换 `__cache__` 占位符） | CarNo, OrderNo, AccidentId |
| 枚举参数 | schema 有 `enum` 字段 | 取第一个有效枚举值 | StatusFlag, BizType |
| 布尔参数 | schema type = boolean | 取 `true` | IsAuth, IncludeRs |

其余参数（Platform/SkipCount/MaxResultCount 等通用参数、无枚举的字符串/整数参数）不参与组合，作为每条用例的固定基底。

### Pairwise 组合生成

用 `allpairspy.PairwiseIter` 生成正交组合：
- 输入：每个可用参数的取值列表（每个参数 1 个值，形如 `[CarNo_value]`）
- 输出：若干组参数组合，保证任意两个参数至少在一条用例中同时出现
- 每条组合用例的固定基底：`{Platform, SkipCount=0, MaxResultCount=10}`

### 用例结构

```python
{
    "name": f"{iface['summary']}-组合查询-{'+'.join(param_names)}",
    "feature": iface["feature"],
    "story": iface["operation_type"],
    "endpoint": iface["endpoint"],
    "method": iface["method"],
    "case_type": "pairwise",
    "params": {Platform, SkipCount, MaxResultCount, ...组合参数},
    "expect": {"status": 200},
    "is_list": True,
}
```

断言逻辑：与现有 `combo_` 用例一致——只校验 HTTP 200 + `isSuccess=True`，允许空结果。

### 对现有用例的影响

- 正向用例（`positive`）：不变
- 旧组合用例（`combo_single`/`combo_multi`）：删除，被 `pairwise` 替代
- 边界用例：未启用，不受影响

### 用例数量预估

| 接口 | 可用参数数 | 旧用例数 | Pairwise 用例数 |
|-----|----------|---------|---------------|
| GetAccidentInfos | ~15 | 2 | ~5 |
| GetComplaints | ~8 | 2 | ~4 |
| GetAnnualInspections | ~5 | 2 | ~3 |
| GetRepairInfos | ~5 | 2 | ~3 |

## 实现范围

| 文件 | 改动 |
|-----|------|
| `requirements.txt` | 新增 `allpairspy` |
| `generators/data_generator.py` | 重写 `_generate_combo_cases`，用 Pairwise 替换旧逻辑 |
| `tests/test_smoke.py` | `case_type` 判断适配 `pairwise`（复用 `combo_` 的断言逻辑） |
| `tests/conftest.py` | 无需改动 |

## 相关设计

- [[2026-05-27-expand-smoke-test-coverage-design]] - 扩展查询接口覆盖范围
- [[2026-05-26-smoke-test-read-interfaces-design]] - 烟雾测试基础框架设计