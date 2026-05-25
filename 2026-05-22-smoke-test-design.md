---
name: smoke-test-design
description: 租车售后系统接口冒烟自动化测试框架设计
---

# 租车售后系统接口冒烟自动化测试框架设计

## 1. 项目背景

为租车售后系统建立接口冒烟自动化测试框架，集成到 Azure CI/CD 流水线中，实现每次部署后自动执行冒烟测试，快速验证核心接口可用性。

## 2. 技术选型

| 决策项 | 选择 | 理由 |
|--------|------|------|
| 测试框架 | pytest | 生态成熟，参数化能力强，Allure 集成简单 |
| HTTP 客户端 | requests | 简洁直观，pytest 配合最佳 |
| 报告格式 | Allure | 可视化效果好，支持历史趋势和附件 |
| 后端技术栈 | .NET Core / C# | 与测试框架无关，测试独立运行 |
| 认证方式 | Cookie 会话 | 登录 `/Account/Login` 后设置 Cookie，有效期 24 小时 |
| Swagger 版本 | OpenAPI 3.0.4 | 约 100+ POST + 100+ GET，174 个 schema 定义 |

## 3. 测试范围

### 3.1 正向用例（合法参数验证）

- 对每个接口发送合法参数
- 验证返回状态码 200
- 验证 `isSuccess=True` + `errorCode=0`
- 查询接口额外验证 `result` 结构完整（items 为数组）

### 3.2 边界值用例（仅限增删改接口）

查询接口不做边界值测试（后端对非法参数返回空结果不报错，断言无意义）。仅对增删改接口验证：

- 空值、null（必填字段）
- 超长字符串
- 非法格式（如手机号填字母）
- 特殊字符（SQL 注入、XSS payload）
- 数值边界（0、负数、超大值、小数）
- 非法枚举值

断言：`isSuccess=False` + `errorCode≠0`

### 3.3 排除范围

- 不涉及复杂业务逻辑验证
- 不涉及多接口联动场景
- 不做数据清理（测试环境沙箱，定期重置）

## 4. 架构设计

### 4.1 整体流程

```
部署完成
    ↓
① 解析 swagger.json           ← 几秒，纯本地解析
    ↓
② 生成测试数据（Faker + 规则） ← 几十毫秒，纯本地
    ↓
③ pytest 执行冒烟测试
    ↓
④ 生成 Allure 报告
```

### 4.2 四层架构

```
┌─────────────────────────────────────────┐
│  pytest 执行层                          │
│  conftest.py → 加载 test_cases fixture  │
│  test_smoke.py → 参数化执行             │
└────────────┬────────────────────────────┘
             │
┌────────────┴────────────────────────────┐
│  用例数据层                             │
│  由 generators 动态生成的 test_cases    │
└────────────┬────────────────────────────┘
             │
┌────────────┴────────────────────────────┐
│  数据生成层                             │
│  swagger_parser.py → 提取CRUD接口       │
│  data_generator.py → Faker正向+规则边界 │
└────────────┬────────────────────────────┘
             │
┌────────────┴────────────────────────────┐
│  HTTP 通信层                            │
│  http_client.py → session、auth、重试   │
└─────────────────────────────────────────┘
```

## 5. 模块详细设计

### 5.1 HTTP 通信层 (`utils/http_client.py`)

职责：封装所有 HTTP 交互，对外暴露简洁方法。

```python
# 使用方式
client = HttpClient(base_url="https://aftersaleapi.demo.ehi.com.cn")
client.login(username, password)        # Cookie 登录，后续请求自动带 Cookie
client.get("/api/repair/list")          # 自动携带 Cookie
client.post("/api/repair/create", json=data)
```

核心功能：

- **鉴权**：`login()` 调用登录接口，`requests.Session()` 自动管理 Cookie
- **会话保持**：Cookie 有效期 24 小时，session 级别复用，无需每次刷 Token
- **登录过期处理**：遇到 401 自动重新登录一次
- **参数无需加密**：后端接口接受明文参数
- **日志**：记录 method、url、耗时、状态码，失败时记录 request/response body
- **超时与重试**：连接超时 5s，读取超时 30s，网络错误重试 2 次

### 5.2 数据生成层

#### `generators/swagger_parser.py`

从 `swagger.json` 提取 CRUD 接口信息：

```python
# 输入：swagger.json URL
# 输出：接口列表
[
    {
        "endpoint": "/api/after-sales/orders",
        "method": "POST",
        "summary": "创建售后工单",
        "request_body_schema": {...},
        "response_schema": {...},
        "required_fields": ["orderId", "type"],
    }
]
```

识别规则（基于 summary 关键词匹配，而非 HTTP Method）：

本系统所有接口只有 GET 和 POST 两种方法，增删改全部用 POST，因此不能按 HTTP Method 区分 CRUD，改为按 summary 关键词识别：

| 操作 | 识别方式 |
|------|---------|
| 增 | summary 含 "添加"、"创建"、"新增"、"登记" |
| 删 | summary 含 "删除"、"取消" |
| 改 | summary 含 "修改"、"更新"、"保存"、"配置" |
| 查 | GET 方法，或 summary 含 "获取"、"查询" |

枚举值过滤：

本系统 Swagger 存在 .NET 枚举污染问题，PlatformEnum 等枚举中混入了 `HasFlag`、`Equals`、`GetHashCode`、`CompareTo`、`ToString`、`GetTypeCode`、`GetType`、`value__` 等 System.Enum 基类方法。解析时需过滤掉这些非业务枚举值：

```python
DOTNET_ENUM_BLACKLIST = {
    "HasFlag", "Equals", "GetHashCode", "CompareTo",
    "ToString", "GetTypeCode", "GetType", "value__"
}
# 过滤逻辑：enum_value not in DOTNET_ENUM_BLACKLIST
```

#### `generators/data_generator.py`

正向数据：根据字段名/类型匹配 Faker 方法

```python
# 字段名含 "name" → faker.name()
# 字段名含 "phone" → faker.phone_number()
# 字段名含 "email" → faker.email()
# 字段类型 string → faker.word()
# 字段类型 integer → random int
```

边界数据：规则驱动

```python
# utils/boundary_rules.py
boundary_rules = {
    "string":  ["", " ", "a"*256, "<script>", "'; DROP TABLE--"],
    "integer": [0, -1, 999999999, 1.5],
    "email":   ["", "notanemail", "a@b"],
    "phone":   ["", "abc", "123", "1"*20],
}
```

### 5.3 pytest 执行层

#### `tests/conftest.py`

```python
@pytest.fixture(scope="session")
def http_client():
    client = HttpClient(base_url=settings.BASE_URL)
    client.login(settings.USERNAME, settings.PASSWORD)
    return client

@pytest.fixture(scope="session")
def test_cases():
    # 解析 swagger + 生成数据
    interfaces = swagger_parser.parse(settings.SWAGGER_URL)
    cases = data_generator.generate(interfaces)
    return cases
```

#### `tests/test_smoke.py`

```python
@allure.feature("{feature}")
@allure.story("{type}")
@pytest.mark.parametrize("case", test_cases, ids=lambda c: c["name"])
def test_crud_smoke(case, http_client):
    response = http_client.request(
        method=case["method"],
        url=case["endpoint"],
        json=case["params"]
    )

    allure.attach(str(case["params"]), name="请求参数", attachment_type=AttachmentType.JSON)
    allure.attach(response.text, name="响应内容", attachment_type=AttachmentType.JSON)

    assert response.status_code == case["expect"]["status"]
    assert "isSuccess" in response.json()
    assert "errorCode" in response.json()

    if case["type"] == "positive":
        assert response.json()["isSuccess"] == True
        assert response.json()["errorCode"] == 0
```

### 5.4 配置层 (`config/settings.py`)

```python
# API 基础地址
BASE_URL = "https://aftersaleapi.demo.ehi.com.cn"

# Swagger 文档地址
SWAGGER_URL = "https://aftersaleapi.demo.ehi.com.cn/swagger/v1/swagger.json"

# 登录配置（前端域名，Cookie 认证）
LOGIN_URL = "https://aftersaleadmin.demo.ehi.com.cn/Account/Login"
USERNAME = os.getenv("TEST_USERNAME")
PASSWORD = os.getenv("TEST_PASSWORD")

# 测试环境域名（用于匹配网关加密配置）
TEST_DOMAIN = "aftersaleadmin.demo"
```

敏感信息（账号密码）从环境变量读取，CI Pipeline 中通过 Azure 变量组注入。

### 5.5 网关加解密模块 (`utils/gateway_crypto.py`)

后端网关对接口参数做了 AES 加密，前端请求时参数被加密后拼到 URL 上。测试脚本需要实现相同的加解密逻辑。

加密算法：AES-256-CFB

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
from urllib.parse import unquote, quote

# 密钥配置（来自 Chrome 插件 Development Companion）
GATEWAY_KEY = "YcgIYXMhHfEqqa/btNK50j4NLa98DAGUy3Wx2fLk7Bs="  # 32字节, Base64
GATEWAY_IV  = "HJhVhS+drenvWfY7Mvalew=="                        # 16字节, Base64

def encrypt(plaintext: str) -> str:
    """明文 → 密文（用于构造请求 URL）"""
    key = base64.b64decode(GATEWAY_KEY)
    iv = base64.b64decode(GATEWAY_IV)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
    encrypted = cipher.encrypt(plaintext.encode('utf-8'))
    b64_str = base64.b64encode(encrypted).decode('utf-8')
    # URL 安全替换: + → $, = → *
    return b64_str.replace("+", "$").replace("=", "*")

def decrypt(encrypted_str: str) -> str:
    """密文 → 明文（用于解密响应内容）"""
    if not encrypted_str:
        return ""
    # URL 安全替换还原: $ → +, * → =
    encrypted_str = unquote(encrypted_str).replace("*", "=").replace("$", "+")
    key = base64.b64decode(GATEWAY_KEY)
    iv = base64.b64decode(GATEWAY_IV)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_str))
    return decrypted.decode('utf-8')
```

加解密流程：

```
请求时：
原始参数 "orderId=123&type=repair"
    → AES-CFB 加密
    → Base64 编码
    → URL 安全替换 (+→$, =→*)
    → 拼到 URL: /api/xxx?3a82dm7$QhM9...

响应时：
加密响应体 "3a82dm7$QhM9..."
    → URL 安全替换还原 ($→+, *→=)
    → Base64 解码
    → AES-CFB 解密
    → 明文 JSON
```

## 6. 项目结构

```
smoke-test/
├── tests/
│   ├── conftest.py              # fixtures: http_client, test_cases
│   └── test_smoke.py            # 参数化执行器
├── generators/
│   ├── swagger_parser.py        # 解析 swagger.json
│   └── data_generator.py        # Faker + 规则生成正向/边界数据
├── utils/
│   ├── http_client.py           # session、auth、日志、重试
│   ├── gateway_crypto.py        # AES-CFB 加解密（网关加密）
│   └── boundary_rules.py        # 边界值规则表
├── config/
│   └── settings.py              # base_url、auth配置、swagger_url
├── requirements.txt
├── pytest.ini
└── azure-pipelines.yml          # CI 流水线配置
```

## 7. CI/CD 集成

### 7.1 Azure Pipeline 配置

```yaml
trigger:
  - none  # 由部署完成后手动触发或调用 API 触发

pool:
  vmImage: 'ubuntu-latest'

steps:
  - task: UsePythonVersion@0
    inputs:
      versionSpec: '3.11'
      addToPath: true

  - script: pip install -r requirements.txt
    displayName: 'Install dependencies'

  - script: pytest --alluredir=allure-results
    displayName: 'Run smoke tests'
    env:
      TEST_USERNAME: $(testUsername)  # Azure 变量组中配置
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

### 7.2 触发方式

- 方式一：部署完成后在 Pipeline 中添加调用测试 Pipeline 的步骤
- 方式二：使用 Azure DevOps REST API 触发测试 Pipeline
- 方式三：配置为同一 Pipeline 的后续 stage

## 8. Swagger 接口分析

基于 `swagger.json`（OpenAPI 3.0.4，31025 行）的实际解析结果：

### 8.1 接口统计

| 类型 | 数量 |
|------|------|
| POST | ~100+ |
| GET | ~100+ |
| PUT/PATCH/DELETE | 0（本系统不使用） |

### 8.2 业务模块（Tags）

| 模块 | 说明 |
|------|------|
| Accident | 事故管理 |
| Complaint | 客诉管理 |
| Repair | 维保/维修 |
| AnnualInspection | 年检 |
| Maintenance | 保养预警 |
| Report | 报表 |
| Common | 公共接口（城市、银行等） |
| ... | 其他模块 |

### 8.3 典型接口示例

| 接口 | 方法 | Summary | 操作类型 |
|------|------|---------|---------|
| `/api/Accident/AddAccidentLog` | POST | 事故查询 添加日志 | 增 |
| `/api/Accident/EditFollowState` | POST | 修改事故跟进状态 | 改 |
| `/api/Accident/GetAccidentDetail` | GET | 获取事故详情 | 查 |
| `/api/Complaint/RegisterComplaint` | POST | 登记客诉 | 增 |
| `/api/Complaint/CancelComplaint` | POST | 取消客诉 | 删 |
| `/api/Repair/GetrepairInfos` | GET | 获取维修信息列表 | 查 |

### 8.4 公共参数

多数接口需要传递以下 Query 参数：

- `Platform`：平台标识（枚举值如 `MyEhi`、`Booking`、`CallCenter` 等）
- `OperatorId`：操作人 ID（可选）
- 其他业务参数在 Request Body（JSON）中传递

### 8.5 响应结构

统一响应格式（`result` 类型随接口变化）：

```json
{
  "isSuccess": true,       // 是否成功
  "errorCode": 0,          // 错误码，0 表示成功
  "message": "string",     // 提示信息
  "operationId": "string", // 操作ID
  "result": ...            // 业务数据，类型不定
}
```

`result` 可能的类型：

| 类型 | 示例 | 常见场景 |
|------|------|---------|
| boolean | `true` | 增/删/改操作，表示操作是否成功 |
| integer | `0` | 新增后返回的 ID |
| object | `{"id": 1, "name": "..."}` | 详情查询 |
| array | `[{"id": 1}, {"id": 2}]` | 列表查询 |
| null | `null` | 无返回数据 |

断言策略：

```python
# 通用断言（所有用例）
assert "isSuccess" in response.json()
assert "errorCode" in response.json()

# 正向用例
assert response.json()["isSuccess"] == True
assert response.json()["errorCode"] == 0

# 边界值用例
assert response.json()["isSuccess"] == False
assert response.json()["errorCode"] != 0
# result 类型不固定，不对 result 做结构断言
```

## 9. 后续扩展

当前版本暂不包含，后续可考虑：

- [ ] 大模型生成边界数据（LLM generator）——已预留扩展点
- [ ] 测试结果通知（邮件/Slack/钉钉）
- [ ] 历史趋势对比告警（失败率上升时自动通知）
- [ ] 接口变更自动检测（Swagger 结构变化时提醒补充测试）