import pytest
from config import settings
from utils.http_client import HttpClient
from generators.swagger_parser import parse_swagger_file
from generators.data_generator import generate_test_cases


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


def pytest_generate_tests(metafunc):
    if "case" in metafunc.fixturenames:
        interfaces = parse_swagger_file(settings.SWAGGER_FILE)
        cases = generate_test_cases(interfaces, settings.DEFAULT_PLATFORM)

        # 模块过滤
        if settings.TEST_MODULES:
            cases = [c for c in cases if c["feature"] in settings.TEST_MODULES]

        ids = [c["name"] for c in cases]
        metafunc.parametrize("case", cases, ids=ids)