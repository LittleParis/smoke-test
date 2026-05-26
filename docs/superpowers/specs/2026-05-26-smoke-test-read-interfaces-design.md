# 查询接口冒烟测试改进设计

## 背景

当前 smoke test 框架跑 Complaint 模块时，33 个查询接口中 15 个失败。失败原因：

1. **CRUD 分类不准** — POST 接口如 `CompleteComplaint`（完成）、`VerifyComplaintInfos`（审核）被误判为 read
2. **参数不够** — 详情接口需要 id/OrderNo 等参数，但 swagger 标记为 required=False，生成器不填充

## 目标

让 Complaint 模块的查询接口在 CI/CD 中稳定通过，断言方式改为入参出参校验（请求值 == 响应值）。

## 设计方案

### 1. 数据获取策略：自动优先 + 手动兜底

查询接口需要的业务参数（id、OrderNo 等），通过两种方式获取：

**优先：自动从列表接口取**
- 调用列表类查询接口（有 MaxResultCount/SkipCount 参数）
- 从响应中提取第一条数据的 id、orderNo 等字段
- 缓存供详情接口使用

**兜底：手动配置的测试数据**
- 配置文件中预定义各模块的已知测试数据
- 自动取不到时（列表接口返回空或失败），使用手动数据
- 都没有则跳过该测试并标记原因

配置文件结构：
```python
# config/test_data.py
TEST_DATA = {
    "Complaint": {"id": 52, "orderNo": "A001", "complainantPhone": "138xxxx"},
    "Accident": {"accidentId": 1186822},
    # 其他模块...
}
```

### 2. 接口分类改进

扩充 CRUD_KEYWORDS 关键词表：

```python
CRUD_KEYWORDS = {
    "create": ["添加", "创建", "新增", "登记"],
    "delete": ["删除", "取消", "移除"],
    "update": ["修改", "更新", "保存", "配置", "审核", "完成", "处理",
               "分配", "录入", "发送", "撤销", "批量修改", "推送", "同步",
               "解析", "导入", "预约"],
    "read": ["获取", "查询", "导出"],
}
```

增加判断规则：
- GET → read
- POST 有 requestBody 且 summary 不含查询关键词 → 非 read（按关键词判定）
- POST 有 requestBody 且 summary 含查询关键词 → read（如驾管获取事故列表）
- POST 无 requestBody → 按关键词判定，默认 read

### 3. 参数填充逻辑

详情接口参数填充优先级：

1. 从自动预取缓存中同名匹配
2. 从手动配置 TEST_DATA 中同名匹配
3. 都没有 → 不填充（保持当前逻辑）

列表接口识别规则：
- 有 MaxResultCount 或 SkipCount 参数 → 列表接口
- endpoint 结尾是 `s`（如 GetComplaints）→ 列表接口

详情接口识别规则：
- 有 id/Id/AccidentId/ComplaintId 等单值参数且无分页参数 → 详情接口

### 4. 断言逻辑改进

从 `isSuccess=True` 改为入参出参校验：

```python
# 请求: GET /api/Complaint/GetComplaintInfo?id=52
# 响应: {"isSuccess": true, "data": {"id": 52, ...}}

assert response["isSuccess"] == True
assert response["data"]["id"] == request_params["id"]  # 入参出参一致
```

只校验请求中显式传入的参数，不校验接口自动返回的字段。

### 5. 执行流程

```
1. 登录 http_client（session fixture）
2. 预取阶段：
   - 识别列表接口
   - 调用列表接口（只传 Platform）
   - 提取响应中的业务数据 → 缓存
3. 生成用例：
   - 列表接口：只传 Platform + 分页参数
   - 详情接口：从缓存或 TEST_DATA 取值填充
4. 执行测试：
   - 调接口
   - 断言 isSuccess=True
   - 断言入参值 == 响应同名字段值
```

### 6. 当前阶段范围

- 只跑 Complaint 模块（TEST_MODULES = ["Complaint"]）
- 只跑 operation_type == "read" 的接口
- 增删改接口的分类先修好，但暂不执行

## 改动文件

| 文件 | 改动 |
|-----|------|
| `swagger_parser.py` | 扩充 CRUD_KEYWORDS，增加 has_body 参数判断 |
| `config/test_data.py` | 新增，手动测试数据配置 |
| `generators/data_prefetch.py` | 新增，自动预取列表数据逻辑 |
| `data_generator.py` | 详情接口参数填充优先从缓存/配置取 |
| `test_smoke.py` | 断言增加入参出参校验 |
| `conftest.py` | session fixture 中调用预取逻辑 |

## 不改动的

- `http_client.py` — 登录逻辑不变
- `boundary_rules.py` — 当前只跑查询，边界值逻辑不动
- `utils/gateway_crypto.py` — 当前不用