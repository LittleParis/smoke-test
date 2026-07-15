# YAML 查询业务流程配置

本目录中的 YAML 是 CI/CD 核心冒烟门禁。每个文件描述一条可独立运行的查询业务流程。

## 核心规则

- 新配置必须声明 `version: 1`。
- 发布门禁默认只允许 GET。
- 列表查询产生的数据通过 `$ref.<步骤>.<字段>` 传给后续步骤。
- 公共运行参数通过 `$var.<名称>` 注入，目前提供 `$var.platform`。
- 引用、提取字段或断言缺失时流程立即失败，不会静默删除参数。
- 新流程不要使用旧 `$cache`/`prefetch`；它们只保留给旧配置兼容。

## 示例

```yaml
version: 1
name: 示例查询冒烟
module: Example
enabled: true
tags: [gate, query]

steps:
  - name: query_list
    endpoint: /api/Example/GetItems
    method: GET
    type: list
    params:
      Platform: $var.platform
      SkipCount: 0
      MaxResultCount: 10
    extract:
      item_id: result.items.0.id
    expect:
      status: 200
      equals:
        isSuccess: true
        errorCode: 0
      not_empty:
        - result.items

  - name: query_detail
    endpoint: /api/Example/GetItem
    method: GET
    type: detail
    params:
      Platform: $var.platform
      id: $ref.query_list.item_id
    expect:
      status: 200
      equals:
        isSuccess: true
        errorCode: 0
        result.id: $ref.query_list.item_id
```

## 字段说明

### 流程级

| 字段 | 必填 | 说明 |
|---|---|---|
| `version` | 是 | 当前固定为 `1` |
| `name` | 是 | 流程显示名称 |
| `module` | 是 | 所属业务模块 |
| `enabled` | 否 | 默认启用 |
| `tags` | 否 | 推荐包含 `gate`、`query` |
| `steps` | 是 | 按顺序执行的非空步骤列表 |

### 步骤级

| 字段 | 必填 | 说明 |
|---|---|---|
| `name` | 是 | 流程内唯一，供 `$ref` 使用 |
| `endpoint` | 是 | 必须以 `/api/` 开头 |
| `method` | 否 | 默认 GET；门禁安全策略只放行安全查询 |
| `type` | 否 | `list`、`detail` 或 `aggregation` |
| `params` | 否 | 查询参数及引用 |
| `extract` | 否 | 上下文名称到响应 JSON 路径的映射 |
| `expect` | 否 | 状态码和 JSON 断言 |

### expect

| 字段 | 说明 |
|---|---|
| `status` | HTTP 状态码，默认 200 |
| `equals` | JSON 路径必须等于固定值、`$var` 或 `$ref` |
| `exists` | 指定 JSON 路径必须存在 |
| `not_empty` | 指定字符串、对象或列表必须非空 |

标准响应默认要求 `isSuccess=true`、`errorCode=0`。建议仍在 YAML 中显式声明，便于业务人员阅读。

## 新增流程检查

1. 先在 `response.md` 中确认 endpoint、HTTP 方法和参数名。
2. 从列表接口中选取稳定的业务主键。
3. 使用 `extract` 提取主键，并用 `$ref` 传给详情接口。
4. 为列表增加 `not_empty`，为详情增加主键相等断言。
5. 运行：

```bash
pytest tests/unit/test_pipeline_configs.py -o addopts=""
pytest tests/test_pipeline.py --collect-only -o addopts=""
pytest tests/test_pipeline.py -v
```
