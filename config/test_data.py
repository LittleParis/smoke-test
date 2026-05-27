import os

# 手动兜底测试数据（当自动预取失败时使用）
# 环境变化后需要更新这些值
TEST_DATA = {
    "Complaint": {
        "id": 52,
        "orderNo": "A001",
    },
    "Accident": {
        "accidentId": 1186822,
    },
    "Repair": {
        "userCode": "CS001",
    },
}

# 可通过环境变量覆盖
_env_data = os.getenv("TEST_DATA_JSON")
if _env_data:
    import json
    try:
        TEST_DATA = json.loads(_env_data)
    except json.JSONDecodeError:
        pass
