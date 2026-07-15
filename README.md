# 租车售后查询冒烟测试

该项目使用 pytest 对售后系统核心查询流程进行冒烟验证，并通过测试退出码充当 CI/CD 发布门禁。

## 两种运行模式

- `tests/test_pipeline.py`：YAML 核心业务流程，作为发布门禁。
- `tests/test_smoke.py`：Swagger 批量查询扫描，作为手动或定时补充覆盖。

## 本地准备

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

在 `.env` 中填写测试账号和密码。框架只允许配置的测试环境和测试域名，不允许执行未经批准的写接口。

## 常用命令

```powershell
# 代码检查
.\.venv\Scripts\python.exe -m ruff check .

# 框架单元测试
.\.venv\Scripts\python.exe -m pytest tests/unit/ -o addopts="" --tb=short

# 收集 YAML 核心流程，不访问网络
.\.venv\Scripts\python.exe -m pytest tests/test_pipeline.py --collect-only -o addopts=""

# 使用本地 HTTP Mock 跑完整登录和三条业务流程（不需要公司网络）
.\.venv\Scripts\python.exe -m pytest tests/integration/ -v -o addopts=""

# 运行 CI/CD 核心冒烟
.\.venv\Scripts\python.exe -m pytest tests/test_pipeline.py -v --tb=short

# 手动运行 Swagger 批量查询扫描
$env:SMOKE_MODE="full"
.\.venv\Scripts\python.exe -m pytest tests/test_smoke.py -v --tb=short

# 生成单页 HTML 报告
.\.venv\Scripts\python.exe generate_report.py allure-report.html
```

## 新增业务流程

复制 `config/pipelines` 中现有 YAML，配置列表查询、主键提取、详情查询和断言。详细格式见 [YAML 配置说明](config/pipelines/README.md)。

目前发布门禁包含：

- Complaint：投诉列表 → 投诉详情。
- Repair：维修列表 → 维修详情。
- Accident：事故列表 → 事故详情。

## CI/CD 门禁

`.github/workflows/smoke-test.yml` 可以独立运行，也可以通过 `workflow_call` 被实际部署流水线调用。调用顺序应为：

```text
部署测试环境 → 调用 Smoke Test Gate → 通过后继续发布
```

冒烟失败时 pytest 返回非零退出码，调用方后续 job 不应执行；测试报告使用 `always()` 保留。失败通知脚本已保留，但暂不接入主门禁。
