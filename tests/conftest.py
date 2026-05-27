import pytest
from config import settings
from utils.http_client import HttpClient
from generators.swagger_parser import parse_swagger_file
from generators.data_generator import generate_test_cases
from generators.data_prefetch import prefetch_module_data


@pytest.fixture(scope="session")
def http_client():
    client = HttpClient(
        base_url=settings.BASE_URL,
        login_url=settings.LOGIN_URL,
        login_return_url=settings.LOGIN_RETURN_URL,
        verify_ssl=settings.VERIFY_SSL,
    )
    assert client.login(settings.USERNAME, settings.PASSWORD), "Login failed"
    yield client


@pytest.fixture(scope="session")
def prefetch_cache(http_client):
    """登录后预取各模块列表数据，缓存供详情接口使用"""
    interfaces = parse_swagger_file(settings.SWAGGER_FILE)
    # 模块过滤
    if settings.TEST_MODULES:
        interfaces = [i for i in interfaces if i["feature"] in settings.TEST_MODULES]
    cache = prefetch_module_data(http_client, interfaces, settings.DEFAULT_PLATFORM)
    return cache


def pytest_generate_tests(metafunc):
    if "case" in metafunc.fixturenames:
        interfaces = parse_swagger_file(settings.SWAGGER_FILE)
        cases = generate_test_cases(interfaces, settings.DEFAULT_PLATFORM)

        # 模块过滤
        if settings.TEST_MODULES:
            cases = [c for c in cases if c["feature"] in settings.TEST_MODULES]

        # 只跑查询接口
        cases = [c for c in cases if c["story"] == "read"]

        # GET 但实际有副作用的接口（API 设计不规范），排除
        SIDE_EFFECT_GET_BLACKLIST = {
            "/api/Complaint/ConfigureComplaintVerifyUsers",  # 配置审核人，会修改数据
            "/api/Complaint/RemoveComplaintType",            # 删除投诉类型，会删数据
        }
        cases = [c for c in cases if c["endpoint"] not in SIDE_EFFECT_GET_BLACKLIST]

        # Repair 模块白名单
        REPAIR_WHITELIST = {
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
        }
        cases = [c for c in cases if c["feature"] != "Repair" or c["endpoint"] in REPAIR_WHITELIST]

        # Accident 模块白名单
        ACCIDENT_WHITELIST = {
            "/api/Accident/GetAccidentInfos",
            "/api/Accident/GetAccidentInfo",
            "/api/Accident/ExportAccidentInfoExcel",
            "/api/Accident/GetOrderLink",
            "/api/Accident/GetAccidentAnnualInspectionCount",
        }
        cases = [c for c in cases if c["feature"] != "Accident" or c["endpoint"] in ACCIDENT_WHITELIST]

        # AfterSaleSetting 模块白名单
        AFTERSALE_WHITELIST = {
            "/api/AfterSaleSetting/RepairItemPriceRules",
            "/api/AfterSaleSetting/RepairItemPriceRule",
        }
        cases = [c for c in cases if c["feature"] != "AfterSaleSetting" or c["endpoint"] in AFTERSALE_WHITELIST]

        # Annual 模块白名单
        ANNUAL_WHITELIST = {
            "/api/Annual/GetAnnualInspections",
            "/api/Annual/GetAnnualInspectionsCount",
        }
        cases = [c for c in cases if c["feature"] != "Annual" or c["endpoint"] in ANNUAL_WHITELIST]

        # Report 模块白名单
        REPORT_WHITELIST = {
            "/api/Report/GetAfterSaleIndexInfo",
            "/api/Report/GetIndexAccidents",
            "/api/Report/GetIndexAccidentsCount",
            "/api/Report/GetIndexMaintains",
            "/api/Report/GetUnMaintainedCount",
        }
        cases = [c for c in cases if c["feature"] != "Report" or c["endpoint"] in REPORT_WHITELIST]

        ids = [c["name"] for c in cases]
        metafunc.parametrize("case", cases, ids=ids)