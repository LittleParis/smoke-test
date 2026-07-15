"""环境与全局配置。

凭据通过 .env 文件或环境变量注入，源码不存储真实密钥。
本地使用：复制 .env.example 为 .env 并填值。
CI 使用：通过 secrets 注入环境变量。
"""
import os
from pathlib import Path

from dotenv import load_dotenv

# 加载项目根目录下的 .env（存在则加载，不存在则跳过）
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env")

# 运行环境与 API
TEST_ENVIRONMENT = os.getenv("TEST_ENVIRONMENT", "demo").strip().lower()
BASE_URL = os.getenv("TEST_BASE_URL", "https://aftersaleapi.demo.ehi.com.cn")
SWAGGER_FILE = str(_PROJECT_ROOT / "response.md")
ALLOWED_TEST_HOSTS = tuple(
    host.strip()
    for host in os.getenv("ALLOWED_TEST_HOSTS", "aftersaleapi.demo.ehi.com.cn").split(",")
    if host.strip()
)

# Login
LOGIN_URL = os.getenv("TEST_LOGIN_URL", "https://login.demo.ehi.com.cn/Account/Login")
LOGIN_RETURN_URL = os.getenv("TEST_LOGIN_RETURN_URL", "https://djeoadmin.demo.ehi.com.cn/")
USERNAME = os.getenv("TEST_USERNAME", "")
PASSWORD = os.getenv("TEST_PASSWORD", "")

# SSL
VERIFY_SSL = os.getenv("TEST_VERIFY_SSL", "false").lower() == "true"

# Gateway crypto（预留，当前接口不需要加密；密钥从环境变量读取，源码不存默认值）
GATEWAY_KEY = os.getenv("GATEWAY_KEY", "")
GATEWAY_IV = os.getenv("GATEWAY_IV", "")

# 默认查询参数
DEFAULT_PLATFORM = os.getenv("TEST_PLATFORM", "MyEhi")

# 模块过滤（空列表=全部测试，非空=只测试指定模块）
TEST_MODULES = ["Complaint", "Repair", "Accident", "AfterSaleSetting", "Annual", "Report"]

# 业务流程配置目录
PIPELINES_DIR = _PROJECT_ROOT / "config" / "pipelines"
