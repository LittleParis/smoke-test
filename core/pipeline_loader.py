"""业务流程配置加载器。

从 config/pipelines/*.yaml 加载业务流程配置，供 test_pipeline.py 驱动执行。

YAML Schema（v2，支持多接口编排）:
    name:      流程名称
    module:    所属模块
    enabled:   是否启用
    prefetch:  数据预取配置（从列表接口提取字段供流程内引用）
    steps:     步骤列表（按顺序执行，支持跨步骤数据传递）
      - name:      步骤名（唯一，用于 $ref 引用）
        endpoint:  接口路径
        method:    HTTP 方法
        type:      list | detail | aggregation
        params:    请求参数（支持 $cache.<field> 和 $ref.<step>.<field>）
        extract:   从响应提取字段存入流程上下文 {上下文键: 响应字段路径}
        expect:    断言
          status:        HTTP 状态码
          is_success:    响应 isSuccess 字段
          match_response: 是否校验入参出参一致性
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from config import settings


@dataclass
class StepExpect:
    status: int = 200
    is_success: bool | None = None
    match_response: bool = False


@dataclass
class StepConfig:
    name: str                          # 步骤名，唯一，用于 $ref 引用
    endpoint: str
    method: str = "GET"
    step_type: str = "detail"          # list | detail | aggregation
    params: dict[str, Any] = field(default_factory=dict)
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
    enabled: bool = True
    prefetch: PrefetchConfig = field(default_factory=PrefetchConfig)
    steps: list[StepConfig] = field(default_factory=list)
    source_file: str = ""


def load_pipeline(filepath: Path) -> PipelineConfig:
    """加载单个 YAML 配置文件。

    支持 v2 schema（steps）和向后兼容 v1 schema（cases，自动转换为 steps）。
    """
    with open(filepath, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    prefetch_raw = raw.get("prefetch") or {}
    prefetch = PrefetchConfig(
        endpoint=prefetch_raw.get("endpoint", ""),
        fields=prefetch_raw.get("fields") or {},
    )

    # 优先读 steps（v2），回退到 cases（v1 兼容）
    steps_raw = raw.get("steps") or raw.get("cases") or []
    steps: list[StepConfig] = []
    for idx, s in enumerate(steps_raw):
        expect_raw = s.get("expect") or {}
        expect = StepExpect(
            status=expect_raw.get("status", 200),
            is_success=expect_raw.get("is_success"),
            match_response=expect_raw.get("match_response", False),
        )
        steps.append(StepConfig(
            name=s.get("name", f"step_{idx}"),
            endpoint=s["endpoint"],
            method=s.get("method", "GET").upper(),
            step_type=s.get("type", "detail"),
            params=s.get("params") or {},
            extract=s.get("extract") or {},
            expect=expect,
        ))

    return PipelineConfig(
        name=raw.get("name", filepath.stem),
        module=raw.get("module", ""),
        enabled=raw.get("enabled", True),
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
        try:
            cfg = load_pipeline(filepath)
        except Exception as e:
            print(f"[PipelineLoader] 加载失败 {filepath.name}: {e}")
            continue
        if cfg.enabled:
            configs.append(cfg)
    return configs


def resolve_value(value: Any, context: dict[str, Any], cache: dict[str, Any]) -> tuple[Any, bool]:
    """解析参数值中的引用，返回 (解析后的值, 是否命中)。

    支持两种引用：
    - $cache.<field>     引用预取缓存
    - $ref.<step>.<field> 引用前序步骤提取的上下文

    命中返回 (实际值, True)；未命中返回 (None, False)。
    非引用值原样返回 (value, True)。
    """
    if not isinstance(value, str):
        return value, True

    if value.startswith("$cache."):
        field_name = value[len("$cache."):]
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
