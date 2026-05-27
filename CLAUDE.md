# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Smoke test automation framework for a car rental after-sales system (租车售后系统). Parses an OpenAPI 3.0 spec, generates positive test cases, and runs parametrized API smoke tests against a demo environment. Current scope: query (read) interfaces only, with data prefetch from list interfaces to populate detail interface params.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run all smoke tests (auto-cleans allure-results)
pytest tests/test_smoke.py -v --tb=short

# Run specific module (edit config/settings.py TEST_MODULES first)
pytest tests/test_smoke.py -v --tb=short

# Generate HTML report from allure-results (no Java needed)
python generate_report.py

# No linter is configured in this project
```

## Architecture

Data flow: Swagger spec → Parser → Prefetch → Generator → pytest → HTTP execution.

### Parser (`generators/swagger_parser.py`)
- Parses OpenAPI 3.0 JSON from `response.md`
- Classifies endpoints as create/read/update/delete based on Chinese keywords in `summary`
- **Classification priority**: GET → always read; POST/PUT/DELETE → mutation keywords first, then read keywords, then fallback by body presence
- Recursively resolves `$ref` (max depth 5)

### Prefetch (`generators/data_prefetch.py`)
- After login, calls list interfaces (those with `MaxResultCount`/`SkipCount`) to extract real business data
- Extracts fields per module: `id`, `orderNo`, `repairId`, `carNo`, `accidentId`, etc.
- Falls back to `config/test_data.py` manual data if auto-prefetch fails
- Caches are merged across multiple list interfaces within the same module

### Generator (`generators/data_generator.py`)
- Generates test cases **only for `operation_type == "read"`** interfaces
- List interfaces: params = `{Platform, SkipCount, MaxResultCount}` only
- Detail interfaces: business params get Faker placeholder values, replaced by prefetch cache at runtime
- Boolean params `IsAuth`/`IncludeRs` default to `true`

### pytest Execution (`tests/conftest.py`)
- Session-scoped `http_client` fixture: logs in once, all tests share the session/cookies
- Session-scoped `prefetch_cache` fixture: calls prefetch after login
- `pytest_generate_tests()`: dynamically parametrizes `case` fixture, filters by `TEST_MODULES` and per-module whitelists

### Test Function (`tests/test_smoke.py`)
- `test_crud_smoke(case, http_client, prefetch_cache)`
- Before request: replaces detail interface params from prefetch cache (ignore-case matching); removes params with no cache match to avoid sending Faker placeholder values
- After response: asserts `status_code == 200`, `isSuccess=True`, `errorCode=0`
- Input-output assertion: request param value == response field value (same name, case-insensitive; supports `self` prefix alias like `OrderNo` ↔ `selfOrderNo`)

### HTML Report (`generate_report.py`)
- Reads `allure-results/` JSON files (handles both standard JSON and Python `repr()` format)
- Generates `allure-report.html` with stats, filters, and expandable request/response details
- Opens automatically in browser

## Key Configuration

- `config/settings.py` — Env config. `TEST_MODULES` controls which modules to test. Credentials from `TEST_USERNAME`/`TEST_PASSWORD` env vars.
- `config/test_data.py` — Manual fallback test data per module when auto-prefetch fails.
- `response.md` — The OpenAPI 3.0 spec (~200 endpoints). This IS the swagger file.
- `utils/gateway_crypto.py` — AES-256-CFB encrypt/decrypt. Reserved; currently unused.

## Module Whitelists

Not all interfaces in a module are tested. Each module has a whitelist in `conftest.py`:
- **Complaint**: 9 read interfaces (list + detail)
- **Repair**: 19 interfaces (6 list + 9 detail + 4 aggregation/export)
- **Accident**: 5 interfaces (2 list + 2 detail + 1 count)
- **AfterSaleSetting**: 2 interfaces (1 list + 1 detail)
- **Annual**: 2 interfaces (1 list + 1 count)
- **Report**: 5 interfaces (all aggregation/count)

GET endpoints with side effects (e.g., `ConfigureComplaintVerifyUsers`, `RemoveComplaintType`) are excluded via `SIDE_EFFECT_GET_BLACKLIST` regardless of whitelist.

To add an interface to a module: add its endpoint path to the corresponding `*_WHITELIST` dict in `conftest.py`, and ensure its required params are mapped in `data_prefetch.py`'s `MODULE_FIELD_MAPPING`.

## CI/CD

Azure Pipelines (`azure-pipelines.yml`): manual trigger only, runs on ubuntu-latest with Python 3.11. Credentials injected from Azure variable group. Allure report published as build artifact even on failure.

## Conventions

- CRUD classification relies on Chinese keywords in endpoint summaries
- List interfaces recognized by `MaxResultCount`/`SkipCount` presence
- Cache field names use camelCase (e.g., `repairId`, `accidentId`, `orderNo`)
- All API responses follow `{ "isSuccess": bool, "errorCode": int, ... }` pattern
