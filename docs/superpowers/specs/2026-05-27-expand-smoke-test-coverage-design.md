# 扩展冒烟测试覆盖范围设计

## 目标

将冒烟测试从 21 个 read 接口扩展到 41 个，覆盖售后核心 6 个模块：Complaint、Repair、Accident、AfterSaleSetting、Annual、Report。

## 最终覆盖率（实际实施后）

| 模块 | read 总数 | 修改前 | 修改后 | 新增 |
|------|----------|--------|--------|------|
| Complaint | 9 | 9 | 9 | 0 |
| Repair | 28 | 10 | 19 | +9 |
| Accident | 8 | 1 | 5 | +4 |
| AfterSaleSetting | 2 | 1 | 2 | +1 |
| Annual | 2 | 0 | 2 | +2 |
| Report | 5 | 0 | 5 | +5 |
| **合计** | **54** | **21** | **41** | **+20** |

注：部分接口因服务端校验复杂（如 Drivers 数组必填）、导出超限、或依赖外部系统（考拉）而移除。

## 1. 分类逻辑修正

**文件**: `generators/swagger_parser.py`

**问题**: GET 请求因 summary 含"审核/处理"等 mutation 关键词被误分类为 update。

**修复**: GET 请求在 read 关键词未匹配时，跳过 mutation 关键词检查，直接返回 read。

```python
def classify_operation(method, summary, has_body=False):
    if any(kw in summary for kw in CRUD_KEYWORDS["read"]):
        return "read"
    if method.upper() == "GET":
        return "read"
    for op_type, keywords in CRUD_KEYWORDS.items():
        if op_type == "read": continue
        if any(kw in summary for kw in keywords):
            return op_type
    return "update" if has_body else "read"
```

**影响接口**: Repair/GetEarlyApplyInfo、Report/GetAfterSaleIndexInfo、Complaint/ConfigureComplaintVerifyUsers

## 2. 白名单扩展

**文件**: `tests/conftest.py`

```python
TEST_MODULES = ["Complaint", "Repair", "Accident", "AfterSaleSetting", "Annual", "Report"]
```

### Repair (+12 个接口)

新增白名单：
- `/api/Repair/GetAccessLogs` — 日志详情列表
- `/api/Repair/GetActionLogs` — 操作日志
- `/api/Repair/GetContractMainRepairInfo` — 维修保养地点信息 (需 CarNo)
- `/api/Repair/GetExportMaintainAlarmsExcel` — 需保养车辆导出
- `/api/Repair/GetExportRepairInfoExcel` — 保养记录导出
- `/api/Repair/GetFields` — 操作日志表字段配置
- `/api/Repair/GetJgTicketDetail` — 违章详情 (需 TicketId)
- `/api/Repair/GetJgTicketDetails` — 违章列表
- `/api/Repair/GetMaintainAlarmLogs` — 预警修改日志 (需 Key)
- `/api/Repair/GetReimburseMiddlePageUrl` — 报销跳转页 (需 Key/UserCode/Type)
- `/api/Repair/GetTicketGroupByBizType` — 订单类型汇总
- `/api/Repair/GetWbOrderInfo` — 考拉维保信息 (需 orderId)
- `/api/Repair/UserReimburseNotMatchInfos` — 材料不符合信息

### Accident (+4 个接口)

新增白名单：
- `/api/Accident/GetAccidentInfo` — 事故详情 (需 AccidentId)
- `/api/Accident/ExportAccidentInfoExcel` — 事故导出
- `/api/Accident/GetInsuranceCustomer` — 跟进客服列表
- `/api/Accident/GetOrderLink` — 订单跳转链接 (需 AccidentId)

不纳入: `/api/Accident/AddAccidentLog` — POST + body，实际是写操作

### AfterSaleSetting (+1 个接口)

新增白名单：
- `/api/AfterSaleSetting/RepairItemPriceRule` — 维保规则详情 (需 Id)

### Annual (新模块，2 个接口)

新增白名单：
- `/api/Annual/GetAnnualInspections` — 需年检车辆列表
- `/api/Annual/GetAnnualInspectionsCount` — 需年检车辆数

### Report (新模块，5 个接口)

新增白名单：
- `/api/Report/GetAfterSaleIndexInfo` — 首页待办汇总
- `/api/Report/GetIndexAccidents` — 首页事故数据
- `/api/Report/GetIndexAccidentsCount` — 待处理事故数
- `/api/Report/GetIndexMaintains` — 首页维保数据
- `/api/Report/GetUnMaintainedCount` — 已预约未保养车辆数

## 3. Prefetch 映射扩展

**文件**: `generators/data_prefetch.py`

### MODULE_FIELD_MAPPING 变更

```python
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
        "ticketId": ["ticketId"],       # 新增：违章详情用
        "key": ["key"],                   # 新增：预警日志用
    },
    "Annual": {                           # 新增模块
        "carNo": ["carNo"],
        "orderNo": ["orderNo"],
    },
}
```

### 新增预取列表接口

| 接口 | 提取字段 | 供哪个详情接口用 |
|------|---------|---------------|
| Repair/GetJgTicketDetails | ticketId | GetJgTicketDetail |
| Annual/GetAnnualInspections | carNo, orderNo | (预留，当前无详情接口) |
| Accident/GetAccidentInfos | 已在预取中 | GetAccidentInfo, GetOrderLink |
| AfterSaleSetting/RepairItemPriceRules | id | RepairItemPriceRule |

## 4. 难点接口处理策略

| 接口 | 所需参数 | 数据来源 |
|------|---------|---------|
| GetContractMainRepairInfo | CarNo (必填) | Repair 预取缓存 carNo |
| GetJgTicketDetail | TicketId | 从 GetJgTicketDetails 列表预取 |
| GetMaintainAlarmLogs | Key | 从 GetMaintainAlarms 列表预取 key 字段 |
| GetReimburseMiddlePageUrl | Key + UserCode + Type | 手动 test_data 兜底 |
| GetWbOrderInfo | orderId | Repair 预取缓存 orderNo |
| UserReimburseNotMatchInfos | UserPhone | Repair 预取缓存 userPhone |
| GetInsuranceCustomer | Type=1 | 枚举参数，data_generator 自动生成 |
| RepairItemPriceRule | Id | AfterSaleSetting 列表预取 |
| Report 全部 | 无业务参数 | 只需 Platform |

## 5. test_data.py 兜底数据

**文件**: `config/test_data.py`

新增手动数据：
```python
TEST_DATA = {
    "Repair": {
        "userCode": "CS001",  # GetReimburseMiddlePageUrl 用
    },
}
```

其他模块数据均可从预取获取，无需手动兜底。

## 6. 不纳入的接口

- `/api/Accident/AddAccidentLog` — POST + request body，summary 含"添加"，实际是写操作
- `/api/Repair/VerifyRepairInfo` — POST，summary 含"审核"，写操作
- 所有 Test 模块接口 — 排除
- 所有 ForDriver/ForH5/ForCrm/ForEo/ForSupport 模块 — 排除

## 文件变更清单

| 文件 | 变更 |
|------|------|
| `generators/swagger_parser.py` | classify_operation 增加 GET 优先读逻辑 |
| `generators/data_prefetch.py` | MODULE_FIELD_MAPPING 增加 Repair 字段 + Annual 模块 |
| `config/test_data.py` | 新增 Repair userCode 兜底数据 |
| `tests/conftest.py` | TEST_MODULES + Annual/Report；扩展各模块白名单 |
