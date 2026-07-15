# 业务流程冒烟配置目录

本目录存放业务流程冒烟测试的 YAML 配置文件，每个文件描述一个业务流程。

## 使用方式

1. 复制 `complaint.yaml` 作为模板
2. 按业务流程修改内容
3. 设置 `enabled: true` 启用
4. 运行 `pytest tests/test_pipeline.py -v` 执行所有启用的流程

## Schema 字段说明

### 流程级配置

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | 流程名称，展示用 |
| `module` | string | 所属模块，用于预取缓存分组 |
| `enabled` | bool | 是否启用，`false` 时跳过整个流程 |
| `prefetch` | object | 数据预取配置 |
| `steps` | list | 步骤列表，按顺序执行 |

### prefetch 配置

| 字段 | 类型 | 说明 |
|------|------|------|
| `endpoint` | string | 列表接口路径 |
| `fields` | dict | 缓存字段 → 响应候选字段列表 |

### step 配置

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | 步骤名（唯一），用于 `$ref` 引用 |
| `endpoint` | string | 接口路径 |
| `method` | string | HTTP 方法，默认 GET |
| `type` | string | `list` / `detail` / `aggregation` |
| `params` | dict | 请求参数，支持引用 |
| `extract` | dict | 从响应提取字段到上下文 |
| `expect` | object | 断言配置 |

### expect 配置

| 字段 | 类型 | 说明 |
|------|------|------|
| `status` | int | 期望 HTTP 状态码，默认 200 |
| `is_success` | bool | 期望响应 isSuccess 字段 |
| `match_response` | bool | 是否校验入参出参一致性 |

## 参数引用

### $cache.<field> — 引用预取缓存

```yaml
params:
  id: $cache.id  # 从 prefetch 提取的 id
```

### $ref.<step>.<key> — 引用前序步骤提取的值

```yaml
steps:
  - name: query_list
    extract:
      complaint_id: result.items.0.id    # 提取到上下文

  - name: query_detail
    params:
      id: $ref.query_list.complaint_id   # 引用前序步骤的值
```

## extract 字段提取

`extract` 从响应 JSON 中按路径提取字段，存入流程上下文。

路径格式：
- `result.items.0.id` — 点号风格
- `result.items[0].id` — 括号风格
- `id` — 简写，自动尝试 `result.id` 再尝试 `id`

## 多接口编排示例

```yaml
steps:
  - name: step1
    endpoint: /api/X/List
    extract:
      biz_id: result.items.0.id

  - name: step2
    endpoint: /api/X/Detail
    params:
      id: $ref.step1.biz_id
    expect:
      match_response: true
```
