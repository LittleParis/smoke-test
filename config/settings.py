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
