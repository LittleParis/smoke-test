# 租车售后系统冒烟测试框架 - 实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 搭建 pytest + requests 冒烟测试框架，用 Complaint 模块验证完整流程能跑通

**Architecture:** 四层架构：配置层 → HTTP 通信层 → 数据生成层 → pytest 执行层。登录采用 Cookie + CSRF Token，接口传明文参数，Allure 生成报告。

**Tech Stack:** Python 3.11, pytest, requests, allure-pytest, faker, pycryptodome

---

## File Structure

```
C:\Users\52071\Desktop\cicd\
├── config/
│   ├── __init__.py
│   └── settings.py              # 环境配置（URL、账号、SSL开关）
├── utils/
│   ├── __init__.py
│   ├── http_client.py            # HTTP 通信 + Cookie 登录
│   ├── gateway_crypto.py         # AES-CFB 加解密（预留，当前不用）
│   └── boundary_rules.py         # 边界值规则表
├── generators/
│   ├── __init__.py
│   ├── swagger_parser.py         # 解析 swagger.json
│   └── data_generator.py         # Faker 正向 + 规则边界数据
├── tests/
│   ├── __init__.py
│   ├── conftest.py               # fixtures: http_client, test_cases
│   └── test_smoke.py             # 参数化冒烟执行器
├── response.md                   # Swagger JSON（已有）
├── requirements.txt
├── pytest.ini
└── azure-pipelines.yml
```

---

### Task 1: 项目初始化 + 依赖配置

**Files:**
- Create: `requirements.txt`
- Create: `pytest.ini`
- Create: `config/__init__.py`
- Create: `config/settings.py`
- Create: `utils/__init__.py`
- Create: `generators/__init__.py`
- Create: `tests/__init__.py`

- [ ] **Step 1: 创建 requirements.txt**

```txt
pytest==8.3.4
requests==2.34.2
allure-pytest==2.13.5
Faker==37.1.0
pycryptodome==3.21.0
urllib3==2.7.0
```

- [ ] **Step 2: 安装依赖**

Run: `pip install -r C:\Users\52071\Desktop\cicd\requirements.txt`
Expected: 所有包安装成功

- [ ] **Step 3: 创建 pytest.ini**

```ini
[pytest]
testpaths = tests
addopts = -v --alluredir=allure-results
markers =
    smoke: smoke test marker
```

- [ ] **Step 4: 创建 config/settings.py**

```python
import os

# API
BASE_URL = "https://aftersaleapi.demo.ehi.com.cn"
SWAGGER_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "response.md")

# Login
LOGIN_URL = "https://login.demo.ehi.com.cn/Account/Login"
LOGIN_RETURN_URL = "https://djeoadmin.demo.ehi.com.cn/"
USERNAME = os.getenv("TEST_USERNAME", "33418")
PASSWORD = os.getenv("TEST_PASSWORD", "Demo:_password1")

# SSL
VERIFY_SSL = False  # demo 环境自签名证书

# Gateway crypto (预留，当前接口不需要加密)
GATEWAY_KEY = "YcgIYXMhHfEqqa/btNK50j4NLa98DAGUy3Wx2fLk7Bs="
GATEWAY_IV = "HJhVhS+drenvWfY7Mvalew=="

# Default query params
DEFAULT_PLATFORM = "MyEhi"
```

- [ ] **Step 5: 创建所有 __init__.py 空文件**

创建 `config/__init__.py`、`utils/__init__.py`、`generators/__init__.py`、`tests/__init__.py`，内容均为空。

- [ ] **Step 6: 验证 pytest 能发现测试目录**

Run: `cd C:\Users\52071\Desktop\cicd && python -m pytest --collect-only`
Expected: 无报错（可能显示 collected 0 items，正常）

---

### Task 2: HTTP 通信层 + Cookie 登录

**Files:**
- Create: `utils/http_client.py`

- [ ] **Step 1: 编写 http_client.py**

```python
import re
import time
import logging
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger("smoke_test")


class HttpClient:
    def __init__(self, base_url: str, login_url: str, login_return_url: str,
                 verify_ssl: bool = False, timeout: int = 30, retries: int = 2):
        self.base_url = base_url.rstrip("/")
        self.login_url = login_url
        self.login_return_url = login_return_url
        self.verify_ssl = verify_ssl
        self.timeout = timeout
        self.retries = retries
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        self._username = None
        self._password = None
        self._logged_in = False

    def login(self, username: str, password: str) -> bool:
        self._username = username
        self._password = password
        login_url = f"{self.login_url}?returnUrl={self.login_return_url}"

        # Step 1: GET login page to get CSRF token
        resp = self.session.get(login_url, verify=self.verify_ssl, timeout=self.timeout)
        if resp.status_code != 200:
            logger.error("GET login page failed: %s", resp.status_code)
            return False

        token_match = re.search(r'__RequestVerificationToken[^>]*value="([^"]+)"', resp.text)
        if not token_match:
            token_match = re.search(r'name="__RequestVerificationToken"[^>]*value="([^"]+)"', resp.text)
        csrf_token = token_match.group(1) if token_match else ""

        # Step 2: POST login
        data = {
            "ReturnUrl": self.login_return_url,
            "Client": "",
            "Ticket": "",
            "Randstr": "",
            "username": username,
            "plainPassword": password,
            "Password": password,
            "__RequestVerificationToken": csrf_token,
        }
        headers = {
            "Referer": login_url,
            "Origin": self.login_url.rsplit("/", 1)[0],
        }
        resp = self.session.post(
            login_url, data=data, headers=headers,
            allow_redirects=False, verify=self.verify_ssl, timeout=self.timeout,
        )

        if resp.status_code == 302:
            self._logged_in = True
            logger.info("Login success, cookies: %s", list(self.session.cookies.keys()))
            return True
        else:
            logger.error("Login failed: status=%s", resp.status_code)
            return False

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{path}" if path.startswith("/") else path
        kwargs.setdefault("verify", self.verify_ssl)
        kwargs.setdefault("timeout", self.timeout)

        for attempt in range(self.retries + 1):
            try:
                start = time.time()
                resp = self.session.request(method, url, **kwargs)
                elapsed = time.time() - start
                logger.info("%s %s -> %s (%.2fs)", method, url, resp.status_code, elapsed)

                # Auto re-login on 401
                if resp.status_code == 401 and self._username and attempt == 0:
                    logger.info("Got 401, re-login...")
                    self.login(self._username, self._password)
                    continue

                return resp
            except requests.RequestException as e:
                logger.warning("Request failed (attempt %d/%d): %s", attempt + 1, self.retries + 1, e)
                if attempt == self.retries:
                    raise

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self.request("POST", path, **kwargs)
```

- [ ] **Step 2: 验证 HttpClient 登录和 API 调用**

Run:
```powershell
python -c "from utils.http_client import HttpClient; from config import settings; c = HttpClient(settings.BASE_URL, settings.LOGIN_URL, settings.LOGIN_RETURN_URL, settings.VERIFY_SSL); print('Login:', c.login(settings.USERNAME, settings.PASSWORD)); r = c.get('/api/Complaint/GetComplaints', params={'Platform':'MyEhi','MaxResultCount':1}); print('API:', r.status_code, r.json().get('isSuccess'))"
```
Expected: `Login: True` 和 `API: 200 True`

---

### Task 3: 边界值规则表

**Files:**
- Create: `utils/boundary_rules.py`

- [ ] **Step 1: 编写 boundary_rules.py**

```python
BOUNDARY_RULES = {
    "string": [
        "",
        " ",
        "a" * 256,
        "<script>alert(1)</script>",
        "'; DROP TABLE users--",
    ],
    "integer": [
        0,
        -1,
        999999999,
        1.5,
    ],
    "boolean": [],
    "email": [
        "",
        "notanemail",
        "a@b",
    ],
    "phone": [
        "",
        "abc",
        "123",
        "1" * 20,
    ],
}

# 字段名关键词 → 边界值类型的映射
FIELD_KEYWORD_RULES = {
    "email": "email",
    "phone": "phone",
    "mobile": "phone",
    "tel": "phone",
}

# .NET 枚举污染过滤
DOTNET_ENUM_BLACKLIST = {
    "HasFlag", "Equals", "GetHashCode", "CompareTo",
    "ToString", "GetTypeCode", "GetType", "value__",
}
```

---

### Task 4: Swagger 解析器

**Files:**
- Create: `generators/swagger_parser.py`

- [ ] **Step 1: 编写 swagger_parser.py**

```python
import json
from utils.boundary_rules import DOTNET_ENUM_BLACKLIST

# 操作类型识别关键词
CRUD_KEYWORDS = {
    "create": ["添加", "创建", "新增", "登记"],
    "delete": ["删除", "取消"],
    "update": ["修改", "更新", "保存", "配置"],
    "read": ["获取", "查询"],
}


def classify_operation(method: str, summary: str) -> str:
    if method == "GET":
        return "read"
    for op_type, keywords in CRUD_KEYWORDS.items():
        if any(kw in summary for kw in keywords):
            return op_type
    return "read"  # 默认归为查询


def parse_swagger_file(file_path: str) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as f:
        spec = json.load(f)

    schemas = spec.get("components", {}).get("schemas", {})
    enums = _extract_enums(schemas)
    paths = spec.get("paths", {})
    interfaces = []

    for endpoint, methods in paths.items():
        for method, detail in methods.items():
            if method not in ("get", "post", "put", "patch", "delete"):
                continue

            summary = detail.get("summary", "")
            operation_type = classify_operation(method, summary)
            tags = detail.get("tags", ["Unknown"])
            feature = tags[0] if tags else "Unknown"

            # 提取 query 参数
            query_params = []
            for p in detail.get("parameters", []):
                if p.get("in") == "query":
                    param_info = {
                        "name": p["name"],
                        "required": p.get("required", False),
                        "description": p.get("description", ""),
                        "schema": _resolve_schema(p.get("schema", {}), schemas),
                    }
                    query_params.append(param_info)

            # 提取 request body schema
            request_body_schema = {}
            request_body = detail.get("requestBody", {})
            if request_body:
                content = request_body.get("content", {})
                for ct, ct_detail in content.items():
                    schema_ref = ct_detail.get("schema", {})
                    request_body_schema = _resolve_schema(schema_ref, schemas)
                    break

            interfaces.append({
                "endpoint": endpoint,
                "method": method.upper(),
                "summary": summary,
                "feature": feature,
                "operation_type": operation_type,
                "query_params": query_params,
                "request_body_schema": request_body_schema,
                "enums": enums,
            })

    return interfaces


def _extract_enums(schemas: dict) -> dict[str, list[str]]:
    enums = {}
    for name, schema in schemas.items():
        if "enum" in schema:
            filtered = [v for v in schema["enum"] if v not in DOTNET_ENUM_BLACKLIST]
            if filtered:
                enums[name] = filtered
    return enums


def _resolve_schema(schema: dict, all_schemas: dict, depth: int = 0) -> dict:
    if depth > 5:
        return schema

    ref = schema.get("$ref", "")
    if ref:
        ref_name = ref.rsplit("/", 1)[-1]
        resolved = all_schemas.get(ref_name, {})
        return _resolve_schema(resolved, all_schemas, depth + 1)

    result = dict(schema)

    if "properties" in result:
        resolved_props = {}
        for prop_name, prop_schema in result["properties"].items():
            resolved_props[prop_name] = _resolve_schema(prop_schema, all_schemas, depth + 1)
        result["properties"] = resolved_props

    return result
```

- [ ] **Step 2: 验证解析器能正确解析 response.md**

Run:
```powershell
python -c "from generators.swagger_parser import parse_swagger_file; from config import settings; result = parse_swagger_file(settings.SWAGGER_FILE); print(f'Total: {len(result)}'); complaint = [i for i in result if i[\"feature\"]==\"Complaint\"]; print(f'Complaint: {len(complaint)}'); print([i[\"summary\"] for i in complaint[:5]])"
```
Expected: 输出接口总数和 Complaint 模块前 5 个接口的 summary

---

### Task 5: 数据生成器

**Files:**
- Create: `generators/data_generator.py`

- [ ] **Step 1: 编写 data_generator.py**

```python
from faker import Faker
from utils.boundary_rules import BOUNDARY_RULES, FIELD_KEYWORD_RULES

fake = Faker("zh_CN")


def generate_test_cases(interfaces: list[dict], default_platform: str = "MyEhi") -> list[dict]:
    cases = []
    for iface in interfaces:
        # 正向用例
        positive_params = _generate_positive_params(iface, default_platform)
        cases.append({
            "name": f"{iface['summary']}-正向",
            "feature": iface["feature"],
            "story": iface["operation_type"],
            "endpoint": iface["endpoint"],
            "method": iface["method"],
            "case_type": "positive",
            "params": positive_params,
            "expect": {"status": 200},
        })

        # 边界值用例（仅增删改）
        if iface["operation_type"] in ("create", "update", "delete"):
            boundary_cases = _generate_boundary_cases(iface, default_platform)
            cases.extend(boundary_cases)

    return cases


def _generate_positive_params(iface: dict, default_platform: str) -> dict:
    params = {}

    # Query 参数
    for p in iface.get("query_params", []):
        name = p["name"]
        schema = p.get("schema", {})
        ptype = schema.get("type", "string")

        if name == "Platform":
            params[name] = default_platform
        elif name in ("SkipCount",):
            params[name] = 0
        elif name in ("MaxResultCount",):
            params[name] = 10
        elif p.get("required", False):
            params[name] = _generate_value_by_type(name, ptype, schema)

    # Request body 参数（POST 接口）
    body_schema = iface.get("request_body_schema", {})
    if body_schema and iface["method"] == "POST":
        body = _generate_body_from_schema(body_schema)
        if body:
            params["_body"] = body

    return params


def _generate_value_by_type(field_name: str, field_type: str, schema: dict = None) -> any:
    schema = schema or {}
    name_lower = field_name.lower()

    # 枚举值
    if "enum" in schema:
        valid = [v for v in schema["enum"] if isinstance(v, (str, int)) and not str(v).startswith("__")]
        if valid:
            return valid[0]

    # 字段名关键词匹配
    for keyword, rule_type in FIELD_KEYWORD_RULES.items():
        if keyword in name_lower:
            if rule_type == "email":
                return fake.email()
            elif rule_type == "phone":
                return fake.phone_number()

    # 类型匹配
    if field_type == "integer":
        return fake.random_int(min=1, max=100)
    elif field_type == "boolean":
        return True
    elif field_type == "number":
        return round(fake.pyfloat(min_value=1, max_value=100), 2)
    elif field_type == "string":
        fmt = schema.get("format", "")
        if fmt == "date-time":
            return fake.date_time_this_year().isoformat()
        return fake.word()
    return fake.word()


def _generate_body_from_schema(schema: dict) -> dict:
    properties = schema.get("properties", {})
    required_fields = schema.get("required", [])
    if not properties:
        return {}

    body = {}
    for prop_name, prop_schema in properties.items():
        if prop_name in required_fields or fake.random_int(min=0, max=1):
            ptype = prop_schema.get("type", "string")
            body[prop_name] = _generate_value_by_type(prop_name, ptype, prop_schema)
    return body


def _generate_boundary_cases(iface: dict, default_platform: str) -> list[dict]:
    cases = []

    # 对必填 query 参数生成边界值
    for p in iface.get("query_params", []):
        if not p.get("required", False):
            continue
        schema = p.get("schema", {})
        ptype = schema.get("type", "string")
        name = p["name"]
        if name == "Platform":
            continue

        rule_type = FIELD_KEYWORD_RULES.get(name.lower(), ptype)
        boundary_values = BOUNDARY_RULES.get(rule_type, BOUNDARY_RULES.get(ptype, []))

        for bv in boundary_values:
            params = {"Platform": default_platform}
            params[name] = bv
            cases.append({
                "name": f"{iface['summary']}-边界-{name}={repr(bv)[:30]}",
                "feature": iface["feature"],
                "story": iface["operation_type"],
                "endpoint": iface["endpoint"],
                "method": iface["method"],
                "case_type": "boundary",
                "params": params,
                "expect": {"status": 200},
            })

    return cases
```

- [ ] **Step 2: 验证数据生成器输出 Complaint 模块的测试用例**

Run:
```powershell
python -c "from generators.swagger_parser import parse_swagger_file; from generators.data_generator import generate_test_cases; from config import settings; ifaces = parse_swagger_file(settings.SWAGGER_FILE); complaint = [i for i in ifaces if i['feature']=='Complaint']; cases = generate_test_cases(complaint); print(f'Cases: {len(cases)}'); [print(c['name']) for c in cases[:8]]"
```
Expected: 输出 Complaint 模块的用例数量和前 8 条用例名

---

### Task 6: pytest 执行层 + conftest

**Files:**
- Create: `tests/conftest.py`
- Create: `tests/test_smoke.py`

- [ ] **Step 1: 编写 tests/conftest.py**

```python
import pytest
import allure
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


@pytest.fixture(scope="session")
def test_cases():
    interfaces = parse_swagger_file(settings.SWAGGER_FILE)
    cases = generate_test_cases(interfaces, settings.DEFAULT_PLATFORM)
    return cases
```

- [ ] **Step 2: 编写 tests/test_smoke.py**

```python
import allure
import pytest


@allure.feature("{feature}")
@allure.story("{story}")
@pytest.mark.parametrize("case", indirect=["test_cases"], ids=lambda c: c["name"])
def test_crud_smoke(case, http_client):
    params = dict(case["params"])
    body = params.pop("_body", None)

    with allure.step(f"{case['method']} {case['endpoint']}"):
        if case["method"] == "GET":
            response = http_client.get(case["endpoint"], params=params)
        elif case["method"] == "POST":
            kwargs = {"params": params}
            if body:
                kwargs["json"] = body
            response = http_client.post(case["endpoint"], **kwargs)
        else:
            response = http_client.request(case["method"], case["endpoint"], params=params)

    # Attach to Allure
    allure.attach(str(params), name="请求参数", attachment_type=allure.attachment_type.JSON)
    allure.attach(response.text[:2000], name="响应内容", attachment_type=allure.attachment_type.JSON)

    # 通用断言
    assert response.status_code == case["expect"]["status"], f"Status code: {response.status_code}"

    body_json = response.json()
    assert "isSuccess" in body_json, "Missing isSuccess in response"
    assert "errorCode" in body_json, "Missing errorCode in response"

    if case["case_type"] == "positive":
        assert body_json["isSuccess"] is True, f"isSuccess=False, message={body_json.get('message')}"
        assert body_json["errorCode"] == 0, f"errorCode={body_json['errorCode']}"
    elif case["case_type"] == "boundary":
        # 边界值期望接口拒绝
        assert body_json["isSuccess"] is False, f"Boundary input accepted: {case['name']}"
```

- [ ] **Step 3: 修复 conftest.py 中 parametrize 的用法**

conftest.py 中的 `test_cases` fixture 直接返回用例列表，`parametrize` 需要直接引用，不能用 `indirect`。更新 `test_smoke.py`：

```python
import allure
import pytest


@allure.feature("{feature}")
@allure.story("{story}")
def test_crud_smoke(case, http_client):
    params = dict(case["params"])
    body = params.pop("_body", None)

    allure.dynamic.feature(case["feature"])
    allure.dynamic.story(case["story"])
    allure.dynamic.title(case["name"])

    with allure.step(f"{case['method']} {case['endpoint']}"):
        if case["method"] == "GET":
            response = http_client.get(case["endpoint"], params=params)
        elif case["method"] == "POST":
            kwargs = {"params": params}
            if body:
                kwargs["json"] = body
            response = http_client.post(case["endpoint"], **kwargs)
        else:
            response = http_client.request(case["method"], case["endpoint"], params=params)

    allure.attach(str(params), name="请求参数", attachment_type=allure.attachment_type.JSON)
    allure.attach(response.text[:2000], name="响应内容", attachment_type=allure.attachment_type.JSON)

    assert response.status_code == case["expect"]["status"]
    body_json = response.json()
    assert "isSuccess" in body_json
    assert "errorCode" in body_json

    if case["case_type"] == "positive":
        assert body_json["isSuccess"] is True, f"message={body_json.get('message')}"
        assert body_json["errorCode"] == 0
    elif case["case_type"] == "boundary":
        assert body_json["isSuccess"] is False, f"Boundary input accepted: {case['name']}"
```

更新 `tests/conftest.py`，用 `pytest.param` 实现参数化：

```python
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
        ids = [c["name"] for c in cases]
        metafunc.parametrize("case", cases, ids=ids)
```

---

### Task 7: 用 Complaint 模块验证完整流程

**Files:**
- Modify: `generators/swagger_parser.py` (添加模块过滤)
- Modify: `config/settings.py` (添加过滤配置)

- [ ] **Step 1: 在 settings.py 添加模块过滤配置**

在 `config/settings.py` 末尾添加：

```python
# 模块过滤（空列表=全部测试，非空=只测试指定模块）
TEST_MODULES = ["Complaint"]
```

- [ ] **Step 2: 在 conftest.py 中添加模块过滤**

更新 `tests/conftest.py` 中的 `pytest_generate_tests`：

```python
def pytest_generate_tests(metafunc):
    if "case" in metafunc.fixturenames:
        interfaces = parse_swagger_file(settings.SWAGGER_FILE)
        cases = generate_test_cases(interfaces, settings.DEFAULT_PLATFORM)
        
        # 模块过滤
        if settings.TEST_MODULES:
            cases = [c for c in cases if c["feature"] in settings.TEST_MODULES]
        
        ids = [c["name"] for c in cases]
        metafunc.parametrize("case", cases, ids=ids)
```

- [ ] **Step 3: 运行测试验证完整流程**

Run: `cd C:\Users\52071\Desktop\cicd && python -m pytest tests/test_smoke.py -v --tb=short`
Expected: Complaint 模块的正向用例全部 PASS

- [ ] **Step 4: 查看 Allure 报告**

Run: `cd C:\Users\52071\Desktop\cicd && python -m pytest tests/test_smoke.py --alluredir=allure-results`
Expected: allure-results 目录下生成 JSON 报告文件

---

### Task 8: 网关加解密模块（预留）

**Files:**
- Create: `utils/gateway_crypto.py`

- [ ] **Step 1: 编写 gateway_crypto.py**

```python
import base64
from urllib.parse import unquote

from Crypto.Cipher import AES

from config import settings


def encrypt(plaintext: str, key_b64: str = None, iv_b64: str = None) -> str:
    key_b64 = key_b64 or settings.GATEWAY_KEY
    iv_b64 = iv_b64 or settings.GATEWAY_IV
    key = base64.b64decode(key_b64)
    iv = base64.b64decode(iv_b64)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
    encrypted = cipher.encrypt(plaintext.encode("utf-8"))
    b64_str = base64.b64encode(encrypted).decode("utf-8")
    return b64_str.replace("+", "$").replace("=", "*")


def decrypt(encrypted_str: str, key_b64: str = None, iv_b64: str = None) -> str:
    if not encrypted_str:
        return ""
    key_b64 = key_b64 or settings.GATEWAY_KEY
    iv_b64 = iv_b64 or settings.GATEWAY_IV
    encrypted_str = unquote(encrypted_str).replace("*", "=").replace("$", "+")
    key = base64.b64decode(key_b64)
    iv = base64.b64decode(iv_b64)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_str))
    return decrypted.decode("utf-8")
```

- [ ] **Step 2: 验证加解密可逆**

Run:
```powershell
python -c "from utils.gateway_crypto import encrypt, decrypt; ct = encrypt('hello world'); print('Encrypted:', ct); pt = decrypt(ct); print('Decrypted:', pt); assert pt == 'hello world', 'Round-trip failed'; print('OK')"
```
Expected: 加密后再解密能还原原文

---

### Task 9: Azure Pipeline 配置

**Files:**
- Create: `azure-pipelines.yml`

- [ ] **Step 1: 编写 azure-pipelines.yml**

```yaml
trigger:
  - none

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.11'
      addToPath: true

  - script: pip install -r requirements.txt
    displayName: 'Install dependencies'

  - script: pytest tests/test_smoke.py --alluredir=allure-results
    displayName: 'Run smoke tests'
    env:
      TEST_USERNAME: $(testUsername)
      TEST_PASSWORD: $(testPassword)

  - task: AllureGenerate@1
    inputs:
      resultsDir: 'allure-results'
      targetDir: 'allure-report'
    condition: always()

  - task: PublishBuildArtifacts@1
    inputs:
      pathToPublish: 'allure-report'
      artifactName: 'allure-report'
    condition: always()
```

---

### Task 10: 清理临时文件

**Files:**
- Delete: `test_login.py`

- [ ] **Step 1: 删除之前的测试验证脚本**

Run: `Remove-Item C:\Users\52071\Desktop\cicd\test_login.py`

---

## Self-Review

**1. Spec coverage:**
- 5.1 HTTP 通信层 → Task 2 ✅
- 5.2 Swagger 解析 → Task 4 ✅
- 5.2 数据生成 → Task 5 ✅
- 5.3 pytest 执行层 → Task 6 ✅
- 5.4 配置层 → Task 1 ✅
- 5.5 网关加解密 → Task 8 ✅
- 6. 项目结构 → 全部覆盖 ✅
- 7. CI/CD → Task 9 ✅
- 8. 枚举过滤 → Task 3 + Task 4 ✅
- CRUD 识别（summary 关键词）→ Task 4 ✅
- 模块过滤验证 → Task 7 ✅

**2. Placeholder scan:** 无 TBD/TODO，所有步骤包含完整代码 ✅

**3. Type consistency:**
- `generate_test_cases` 返回 `list[dict]`，每个 dict 含 `name/feature/story/endpoint/method/case_type/params/expect` → `test_crud_smoke` 中使用一致 ✅
- `parse_swagger_file` 返回 `list[dict]`，每个 dict 含 `endpoint/method/summary/feature/operation_type/query_params/request_body_schema/enums` → `generate_test_cases` 使用一致 ✅
