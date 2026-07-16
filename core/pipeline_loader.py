"""业务流程 YAML 配置加载与启动前校验。"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from config import settings

SUPPORTED_SCHEMA_VERSIONS = {1}
SUPPORTED_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE"}
SUPPORTED_STEP_TYPES = {"list", "detail", "aggregation"}


class PipelineValidationError(ValueError):
    """业务流程配置不符合约定。"""


@dataclass
class StepExpect:
    status: int = 200
    is_success: bool | None = None
    match_response: bool = False
    equals: dict[str, Any] = field(default_factory=dict)
    exists: list[str] = field(default_factory=list)
    not_empty: list[str] = field(default_factory=list)


@dataclass
class StepConfig:
    name: str                          # 步骤名，唯一，用于 $ref 引用
    endpoint: str
    method: str = "GET"
    step_type: str = "detail"          # list | detail | aggregation
    params: dict[str, Any] = field(default_factory=dict)
    body: dict[str, Any] = field(default_factory=dict)      # POST 请求体（JSON）
    extract: dict[str, str] = field(default_factory=dict)  # {上下文键: 响应字段路径}
    expect: StepExpect = field(default_factory=StepExpect)


@dataclass
class PrefetchConfig:
    endpoint: str = ""
    fields: dict[str, list[str]] = field(default_factory=dict)


@dataclass
class PipelineConfig:
    name: str
    module: str
    version: int = 1
    enabled: bool = True
    tags: list[str] = field(default_factory=list)
    prefetch: PrefetchConfig = field(default_factory=PrefetchConfig)
    steps: list[StepConfig] = field(default_factory=list)
    source_file: str = ""


def load_pipeline(filepath: Path) -> PipelineConfig:
    """加载单个 YAML 配置文件。

    新配置使用 ``steps``；旧配置中的 ``cases`` 会继续自动转换为 steps。
    所有结构和引用在返回前完成校验，避免运行时才发现配置错误。
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        raise PipelineValidationError(f"{filepath.name}: YAML 语法错误: {exc}") from exc

    if not isinstance(raw, dict):
        _validation_error(filepath, "根节点必须是对象")

    version = raw.get("version", 1)
    if type(version) is not int or version not in SUPPORTED_SCHEMA_VERSIONS:
        _validation_error(filepath, f"version 必须是 {sorted(SUPPORTED_SCHEMA_VERSIONS)} 之一")

    name = _required_string(raw, "name", filepath)
    module = _required_string(raw, "module", filepath)

    enabled = raw.get("enabled", True)
    if not isinstance(enabled, bool):
        _validation_error(filepath, "enabled 必须是布尔值")

    tags = raw.get("tags") or []
    if not isinstance(tags, list) or not all(isinstance(tag, str) and tag.strip() for tag in tags):
        _validation_error(filepath, "tags 必须是非空字符串列表")

    prefetch_raw = raw.get("prefetch") or {}
    if not isinstance(prefetch_raw, dict):
        _validation_error(filepath, "prefetch 必须是对象")
    prefetch_endpoint = prefetch_raw.get("endpoint", "")
    prefetch_fields = prefetch_raw.get("fields") or {}
    if not isinstance(prefetch_endpoint, str):
        _validation_error(filepath, "prefetch.endpoint 必须是字符串")
    if not isinstance(prefetch_fields, dict):
        _validation_error(filepath, "prefetch.fields 必须是对象")
    prefetch = PrefetchConfig(
        endpoint=prefetch_endpoint,
        fields=prefetch_fields,
    )

    # 优先读 steps，回退到旧 cases 兼容格式。
    steps_raw = raw.get("steps") if "steps" in raw else raw.get("cases")
    if not isinstance(steps_raw, list) or not steps_raw:
        _validation_error(filepath, "steps 必须是非空列表")

    steps: list[StepConfig] = []
    step_names: set[str] = set()
    for idx, s in enumerate(steps_raw):
        location = f"steps[{idx}]"
        if not isinstance(s, dict):
            _validation_error(filepath, f"{location} 必须是对象")

        step_name = _required_string(s, "name", filepath, location)
        if step_name in step_names:
            _validation_error(filepath, f"{location}.name 重复: {step_name}")
        step_names.add(step_name)

        endpoint = _required_string(s, "endpoint", filepath, location)
        if not endpoint.startswith("/api/"):
            _validation_error(filepath, f"{location}.endpoint 必须以 /api/ 开头")

        method = s.get("method", "GET")
        if not isinstance(method, str) or method.upper() not in SUPPORTED_METHODS:
            _validation_error(filepath, f"{location}.method 不支持: {method}")

        step_type = s.get("type", "detail")
        if step_type not in SUPPORTED_STEP_TYPES:
            _validation_error(filepath, f"{location}.type 不支持: {step_type}")

        params = s.get("params") or {}
        extract = s.get("extract") or {}
        if not isinstance(params, dict):
            _validation_error(filepath, f"{location}.params 必须是对象")
        body = s.get("body") or {}
        if not isinstance(body, dict):
            _validation_error(filepath, f"{location}.body 必须是对象")
        if not isinstance(extract, dict) or not all(
            isinstance(key, str) and key and isinstance(path, str) and path
            for key, path in extract.items()
        ):
            _validation_error(filepath, f"{location}.extract 必须是非空字符串到 JSON 路径的映射")

        expect_raw = s.get("expect") or {}
        if not isinstance(expect_raw, dict):
            _validation_error(filepath, f"{location}.expect 必须是对象")
        unknown_expect = set(expect_raw) - {
            "status", "is_success", "match_response", "equals", "exists", "not_empty"
        }
        if unknown_expect:
            _validation_error(filepath, f"{location}.expect 包含不支持字段: {sorted(unknown_expect)}")
        status = expect_raw.get("status", 200)
        is_success = expect_raw.get("is_success")
        match_response = expect_raw.get("match_response", False)
        equals = expect_raw.get("equals") or {}
        exists = expect_raw.get("exists") or []
        not_empty = expect_raw.get("not_empty") or []
        if type(status) is not int:
            _validation_error(filepath, f"{location}.expect.status 必须是整数")
        if is_success is not None and not isinstance(is_success, bool):
            _validation_error(filepath, f"{location}.expect.is_success 必须是布尔值")
        if not isinstance(match_response, bool):
            _validation_error(filepath, f"{location}.expect.match_response 必须是布尔值")
        if not isinstance(equals, dict) or not all(isinstance(path, str) and path for path in equals):
            _validation_error(filepath, f"{location}.expect.equals 必须是 JSON 路径到期望值的映射")
        if not _is_string_list(exists):
            _validation_error(filepath, f"{location}.expect.exists 必须是非空字符串列表")
        if not _is_string_list(not_empty):
            _validation_error(filepath, f"{location}.expect.not_empty 必须是非空字符串列表")

        expect = StepExpect(
            status=status,
            is_success=is_success,
            match_response=match_response,
            equals=equals,
            exists=exists,
            not_empty=not_empty,
        )
        steps.append(StepConfig(
            name=step_name,
            endpoint=endpoint,
            method=method.upper(),
            step_type=step_type,
            params=params,
            body=body,
            extract=extract,
            expect=expect,
        ))

    _validate_step_references(filepath, steps)

    return PipelineConfig(
        name=name,
        module=module,
        version=version,
        enabled=enabled,
        tags=tags,
        prefetch=prefetch,
        steps=steps,
        source_file=str(filepath),
    )


def load_all_pipelines(pipelines_dir: Path | None = None) -> list[PipelineConfig]:
    """加载目录下所有业务流程配置。

    - 扫描 *.yaml / *.yml
    - 跳过 enabled=False 的流程
    - 返回结果按文件名排序，保证执行顺序稳定
    """
    pipelines_dir = pipelines_dir or settings.PIPELINES_DIR
    if not pipelines_dir.exists():
        return []

    configs: list[PipelineConfig] = []
    for filepath in sorted(pipelines_dir.glob("*.y*ml")):
        cfg = load_pipeline(filepath)
        if cfg.enabled:
            configs.append(cfg)
    return configs


def _validation_error(filepath: Path, message: str) -> None:
    raise PipelineValidationError(f"{filepath.name}: {message}")


def _required_string(raw: dict[str, Any], key: str, filepath: Path, prefix: str = "") -> str:
    value = raw.get(key)
    location = f"{prefix}.{key}" if prefix else key
    if not isinstance(value, str) or not value.strip():
        _validation_error(filepath, f"{location} 必须是非空字符串")
    return value.strip()


def _validate_step_references(filepath: Path, steps: list[StepConfig]) -> None:
    """确保 $ref 只引用前序步骤已经声明的 extract 字段。"""
    available: dict[str, set[str]] = {}
    for step in steps:
        references = [
            (f"参数 {name}", value)
            for name, value in step.params.items()
        ] + [
            (f"请求体 {name}", value)
            for name, value in step.body.items()
        ] + [
            (f"断言 {path}", value)
            for path, value in step.expect.equals.items()
        ]
        for reference_location, value in references:
            if not isinstance(value, str) or not value.startswith("$ref."):
                continue
            parts = value[len("$ref."):].split(".", 1)
            if len(parts) != 2 or not all(parts):
                _validation_error(filepath, f"步骤 {step.name} {reference_location} 的引用格式错误: {value}")
            ref_step, ref_field = parts
            if ref_step not in available:
                _validation_error(
                    filepath,
                    f"步骤 {step.name} {reference_location} 引用了不存在或尚未执行的步骤: {ref_step}",
                )
            if ref_field not in available[ref_step]:
                _validation_error(
                    filepath,
                    f"步骤 {step.name} {reference_location} 引用了未提取字段: {value}",
                )
        available[step.name] = set(step.extract)


def _is_string_list(value: Any) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) and item.strip() for item in value)


def resolve_value(
    value: Any,
    context: dict[str, Any],
    variables: dict[str, Any] | None = None,
    legacy_cache: dict[str, Any] | None = None,
) -> tuple[Any, bool]:
    """解析参数值中的引用，返回 (解析后的值, 是否命中)。

    支持三种引用：
    - $var.<field>       引用运行时公共变量
    - $ref.<step>.<field> 引用前序步骤提取的上下文
    - $cache.<field>     旧配置兼容；新流程不再使用

    命中返回 (实际值, True)；未命中返回 (None, False)。
    非引用值原样返回 (value, True)。
    """
    variables = variables or {}
    if not isinstance(value, str):
        return value, True

    if value.startswith("$var."):
        field_name = value[len("$var."):]
        val = variables.get(field_name)
        return (val, val is not None)

    if value.startswith("$cache."):
        field_name = value[len("$cache."):]
        cache = legacy_cache if legacy_cache is not None else variables
        val = cache.get(field_name)
        return (val, val is not None)

    if value.startswith("$ref."):
        # 格式: $ref.<step_name>.<field>
        parts = value[len("$ref."):].split(".", 1)
        if len(parts) != 2:
            return None, False
        step_name, field_name = parts
        step_ctx = context.get(step_name, {})
        val = step_ctx.get(field_name)
        return (val, val is not None)

    return value, True
