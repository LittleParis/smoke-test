# CI/CD 集成设计

## 目标

将冒烟测试框架嵌入 Azure Pipelines，实现 PR 触发、失败重试、企微通知、HTML 报告持久化。

## 范围

- CI 平台：Azure Pipelines（现有）
- 触发方式：PR 触发（main 分支）
- 通知方式：企业微信机器人 Webhook
- 环境：单环境（demo）

## 1. Pipeline 流程

```
PR → Install → Run Tests (含重试) → Generate Report → 企微通知 → Publish Artifacts
```

每个步骤失败不阻断后续（`condition: always()`），确保报告和通知始终执行。

### azure-pipelines.yml 改造

```yaml
pr:
  branches:
    include:
      - main

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

  - script: python generate_report.py allure-report.html
    displayName: 'Generate HTML report'
    condition: always()

  - script: |
      python scripts/notify_wecom.py \
        --webhook $(WecomWebhook) \
        --results allure-results \
        --build-url "$(Build.BuildUri)" \
        --branch "$(Build.SourceBranch)" \
        --trigger "$(Build.Reason)" \
        --notify-always
    displayName: 'Send WeCom notification'
    condition: always()

  - task: PublishBuildArtifacts@1
    inputs:
      pathToPublish: 'allure-report.html'
      artifactName: 'smoke-test-report'
    condition: always()

  - task: PublishBuildArtifacts@1
    inputs:
      pathToPublish: 'allure-results'
      artifactName: 'allure-results'
    condition: always()
```

关键变更：
- `trigger: none` + `pr:` 替代原来的手动触发
- 移除 `AllureGenerate@1`（需要 Java），改用 `generate_report.py`
- 新增企微通知步骤
- 同时发布 HTML 报告和 allure-results 原始数据

## 2. 失败重试

使用 pytest-rerunfailures 插件，全局重试 2 次，间隔 3 秒。

### pytest.ini 变更

```ini
[pytest]
testpaths = tests
addopts = -v --alluredir=allure-results --clean-alluredir --reruns 2 --reruns-delay 3
markers =
    smoke: smoke test marker
```

### 新增依赖

```
pytest-rerunfailures==15.0
```

## 3. 企微通知

### 新增脚本: `scripts/notify_wecom.py`

读取 allure-results 中的测试结果，生成 Markdown 消息推送到企微机器人。

### 通知内容

```markdown
## 冒烟测试报告

**状态**: ✅ 通过 / ❌ 失败
**分支**: feature/xxx
**触发**: Pull Request

**统计**: 41 总计 | 39 通过 | 2 失败 | 0 异常
**耗时**: 20.5s

### 失败用例
1. 获取违章列表 - HTTP 289, Drivers 必填
2. 获取操作日志 - HTTP 500, SQL异常

[查看详细报告](azure-artifact-url)
```

### 参数

| 参数 | 说明 |
|------|------|
| `--webhook` | 企微机器人 Webhook URL（必填） |
| `--results` | allure-results 目录路径（默认 allure-results） |
| `--build-url` | 构建详情页链接 |
| `--branch` | 分支名 |
| `--trigger` | 触发原因 |
| `--notify-always` | 无论成功失败都发通知（默认只发失败） |

### Azure 变量组

在现有 Variable Group 中新增：
- `WecomWebhook` — 企微机器人 Webhook URL

## 4. 报告产物

| 产物 | 说明 | 格式 |
|------|------|------|
| `allure-report.html` | 单文件 HTML 报告，浏览器直接打开 | HTML |
| `allure-results/` | Allure 原始数据，可用 Java 版 Allure 生成趋势报告 | JSON |

## 文件变更清单

| 文件 | 变更 |
|------|------|
| `azure-pipelines.yml` | PR 触发 + generate_report 替代 AllureGenerate + 企微通知 + 产物发布 |
| `scripts/notify_wecom.py` | 新增：企微通知脚本 |
| `pytest.ini` | 添加 `--reruns 2 --reruns-delay 3` |
| `requirements.txt` | 添加 `pytest-rerunfailures` |
