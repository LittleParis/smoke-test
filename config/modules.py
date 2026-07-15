"""模块级配置：白名单、副作用黑名单、字段映射。

集中管理原先散落在 tests/conftest.py 和 generators/data_prefetch.py 中的硬编码配置，
便于维护和扩展。新增模块或接口时只需修改本文件。
"""
from __future__ import annotations

# GET 但实际有副作用的接口（API 设计不规范），全局排除
SIDE_EFFECT_GET_BLACKLIST: set[str] = {
    "/api/Complaint/ConfigureComplaintVerifyUsers",  # 配置审核人，会修改数据
    "/api/Complaint/RemoveComplaintType",            # 删除投诉类型，会删数据
}

# 各模块查询接口白名单
# key: 模块名, value: 允许测试的 endpoint 集合
MODULE_WHITELISTS: dict[str, set[str]] = {
    "Complaint": {
        # 投诉模块当前未设白名单 → 所有 read 接口均参与测试
    },
    "Repair": {
        # 保养记录查询 - 列表
        "/api/Repair/GetRepairInfos",
        # 保养记录查询 - 详情
        "/api/Repair/GetRepairInfo",
        "/api/Repair/GetOrderDetailLink",
        "/api/Repair/GetReimburseMiddleResponse",
        "/api/Repair/RepairRescueUrl",
        "/api/Repair/GetRepairInfoGroupCount",
        # 工单凭证审核 - 列表
        "/api/Repair/GetEarlyApplyInfos",
        "/api/Repair/ExportEarlyApplyInfosExcel",
        # 工单凭证审核 - 详情
        "/api/Repair/GetEarlyApplyInfo",
        # 需保养车辆 - 列表
        "/api/Repair/GetMaintainAlarms",
        # 政企服务 - 列表
        "/api/Repair/GetMaintenanceInfos",
        # 日志 - 列表
        "/api/Repair/GetAccessLogs",
        "/api/Repair/GetFields",
        # 维修保养地点（需 CarNo，从预取缓存填充）
        "/api/Repair/GetContractMainRepairInfo",
        # 需保养车辆导出
        "/api/Repair/GetExportMaintainAlarmsExcel",
        # 预警修改日志（需 Key，从预取缓存填充）
        "/api/Repair/GetMaintainAlarmLogs",
        # 订单汇总
        "/api/Repair/GetTicketGroupByBizType",
        # 材料不符合
        "/api/Repair/UserReimburseNotMatchInfos",
        # 操作日志（KeyNo 从缓存 repairId 填充）
        "/api/Repair/GetOperationLogs",
        # 保养记录导出（CarNo 从缓存填充，限制导出范围）
        "/api/Repair/GetExportRepairInfoExcel",
    },
    "Accident": {
        "/api/Accident/GetAccidentInfos",
        "/api/Accident/GetAccidentInfo",
        "/api/Accident/ExportAccidentInfoExcel",
        "/api/Accident/GetOrderLink",
        "/api/Accident/GetAccidentAnnualInspectionCount",
    },
    "AfterSaleSetting": {
        "/api/AfterSaleSetting/RepairItemPriceRules",
        "/api/AfterSaleSetting/RepairItemPriceRule",
    },
    "Annual": {
        "/api/Annual/GetAnnualInspections",
        "/api/Annual/GetAnnualInspectionsCount",
    },
    "Report": {
        "/api/Report/GetAfterSaleIndexInfo",
        "/api/Report/GetIndexAccidents",
        "/api/Report/GetIndexAccidentsCount",
        "/api/Report/GetIndexMaintains",
        "/api/Report/GetUnMaintainedCount",
    },
}


# 各模块从列表响应中提取的字段
# key: 缓存字段名, value: 列表响应中候选字段名列表（按优先级）
MODULE_FIELD_MAPPING: dict[str, dict[str, list[str]]] = {
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


def is_endpoint_allowed(module: str, endpoint: str) -> bool:
    """判断某接口是否允许测试（受模块白名单约束）。

    - 模块未配置白名单（空集合或缺失）→ 允许
    - 模块配置了白名单 → 仅允许白名单内接口
    """
    whitelist = MODULE_WHITELISTS.get(module, set())
    if not whitelist:
        return True
    return endpoint in whitelist


def is_side_effect_get(endpoint: str) -> bool:
    """判断是否为有副作用的 GET 接口（应排除）"""
    return endpoint in SIDE_EFFECT_GET_BLACKLIST
