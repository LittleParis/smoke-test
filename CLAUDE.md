# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Smoke test automation framework for a car rental after-sales system (租车售后系统). Parses an OpenAPI 3.0 spec, generates positive + boundary test cases, and runs parametrized API smoke tests against a demo environment with Allure reporting. Deployed via Azure DevOps CI/CD.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run all smoke tests
pytest tests/test_smoke.py -v --tb=short

# Run with Allure output (default via pytest.ini)
pytest tests/test_smoke.py

# Run a specific test by parametrized ID
pytest tests/test_smoke.py -k "登记客诉-正向"

# Generate Allure HTML report locally
allure generate allure-results -o allure-report --clean && allure open allure-report

# No linter is configured in this project
```

## Architecture

Four-layer design with data flow: Swagger spec → Parser → Data Generator → pytest parametrization → HTTP execution.

### Layer 1: HTTP Communication
- `utils/http_client.py` — `HttpClient` class using `requests.Session`. Login is a 2-step CSRF flow (GET page → extract token → POST form). Auto re-login on 401, 2 retries on network errors. SSL verification disabled for demo environment.

### Layer 2: Data Parsing
- `generators/swagger_parser.py` — Parses OpenAPI 3.0 JSON from `response.md`. Classifies each endpoint as create/read/update/delete based on Chinese keywords in `summary` (添加=create, 删除=delete, 修改=update, 获取/查询=read). Recursively resolves `$ref` (max depth 5). Filters .NET `System.Enum` base methods via `DOTNET_ENUM_BLACKLIST` in `utils/boundary_rules.py`.

### Layer 3: Test Case Generation
- `generators/data_generator.py` — Takes parsed interfaces and produces test case dicts. One positive case per interface (Faker zh_CN). Boundary cases for create/update/delete interfaces, skipping `Platform` param, using rules from `boundary_rules.py`.

### Layer 4: pytest Execution
- `tests/conftest.py` — Session-scoped `http_client` fixture. `pytest_generate_tests()` dynamically parametrizes the `case` fixture by calling the parser → generator pipeline. Filters by `settings.TEST_MODULES` if non-empty.
- `tests/test_smoke.py` — Single `test_crud_smoke(case, http_client)` function. Positive cases assert `isSuccess=True`; boundary cases assert `isSuccess=False`.

## Key Configuration

- `config/settings.py` — All env config. `TEST_MODULES = ["Complaint"]` controls which modules to test (empty list = all modules). Credentials from `TEST_USERNAME`/`TEST_PASSWORD` env vars.
- `response.md` — The OpenAPI 3.0 spec (~200 endpoints, GET/POST only). This IS the swagger file, not documentation.
- `utils/gateway_crypto.py` — AES-256-CFB encrypt/decrypt. Reserved for gateway-encrypted APIs; currently unused as endpoints accept plaintext.

## CI/CD

Azure Pipelines (`azure-pipelines.yml`): manual trigger only, runs on ubuntu-latest with Python 3.11. Credentials injected from Azure variable group (`testUsername`, `testPassword`). Allure report generated and published as build artifact even on test failure.

## Conventions

- CRUD classification relies on Chinese keywords in endpoint summaries — adding new endpoints requires following this naming convention.
- Boundary test rules are centralized in `utils/boundary_rules.py` — new parameter boundary rules go there.
- All API responses follow `{ "isSuccess": bool, "errorCode": int, ... }` pattern for assertions.
