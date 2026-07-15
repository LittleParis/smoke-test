import pytest

from config import settings
from config.modules import is_endpoint_allowed, is_side_effect_get
from generators.data_generator import generate_test_cases
from generators.data_prefetch import prefetch_module_data
from generators.swagger_parser import parse_swagger_file
from utils.http_client import HttpClient


@pytest.fixture(scope="session")
def http_client():
    assert settings.USERNAME, "缺少 TEST_USERNAME，请通过 .env 或 CI Secrets 注入"
    assert settings.PASSWORD, "缺少 TEST_PASSWORD，请通过 .env 或 CI Secrets 注入"
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

        # 排除有副作用的 GET 接口
        cases = [c for c in cases if not is_side_effect_get(c["endpoint"])]

        # 应用各模块白名单
        cases = [c for c in cases if is_endpoint_allowed(c["feature"], c["endpoint"])]

        ids = [c["name"] for c in cases]
        metafunc.parametrize("case", cases, ids=ids)
