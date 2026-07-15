#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
本地模拟 CI/CD Pipeline 流程

用法:
    python scripts/local_pipeline.py

可选项:
    --webhook URL      企微 Webhook（不传则只打印通知内容不发送）
    --skip-test        跳过测试（用现有 allure-results）
    --branch NAME      模拟分支名
    --trigger REASON   模拟触发原因
"""

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(cmd, label, cwd=None):
    """执行命令，实时输出"""
    print(f"\n{'='*60}")
    print(f"[STEP] {label}")
    print(f"[CMD]  {cmd}")
    print(f"{'='*60}")
    start = time.time()
    result = subprocess.run(
        cmd, shell=True, cwd=cwd or ROOT,
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
    )
    elapsed = time.time() - start
    status = "✅" if result.returncode == 0 else "❌"
    print(f"\n[{status}] {label} — 耗时 {elapsed:.1f}s (exit code: {result.returncode})")
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="本地模拟 CI/CD Pipeline")
    parser.add_argument("--webhook", default="", help="企微 Webhook URL（不传则只打印不发送）")
    parser.add_argument("--skip-test", action="store_true", help="跳过测试步骤")
    parser.add_argument("--branch", default="local-test", help="模拟分支名")
    parser.add_argument("--trigger", default="Manual", help="模拟触发原因")
    args = parser.parse_args()
    python_cmd = f'"{sys.executable}"'

    print("=" * 60)
    print("  本地 CI/CD Pipeline 模拟")
    print(f"  分支: {args.branch}  触发: {args.trigger}")
    print("=" * 60)

    exit_code = 0

    # Step 1: Install dependencies
    rc = run(f"{python_cmd} -m pip install -r requirements.txt -q", "Install dependencies")
    if rc != 0:
        exit_code = 1

    # Step 2: Run YAML gate smoke tests
    if not args.skip_test:
        rc = run(f"{python_cmd} -m pytest tests/test_pipeline.py -v --tb=short", "Run pipeline smoke tests")
        if rc != 0:
            exit_code = 1
    else:
        print("\n[SKIP] Run smoke tests (using existing allure-results)")

    # Step 3: Generate HTML report
    rc = run(f"{python_cmd} generate_report.py allure-report.html", "Generate HTML report")
    if rc != 0:
        exit_code = 1

    # Step 4: WeCom notification
    print(f"\n{'='*60}")
    print("[STEP] WeCom notification")
    print(f"{'='*60}")
    notify_cmd = (
        f"{python_cmd} scripts/notify_wecom.py"
        f" --results allure-results"
        f" --branch {args.branch}"
        f" --trigger {args.trigger}"
        f" --notify-always"
    )
    if args.webhook:
        notify_cmd += f" --webhook {args.webhook}"
        rc = run(notify_cmd, "Send WeCom notification")
    else:
        # 无 Webhook 时只预览消息不发送
        notify_cmd += " --webhook DRY_RUN --dry-run"
        rc = run(notify_cmd, "Preview WeCom notification (dry-run)")

    # Step 5: Summary
    print(f"\n{'='*60}")
    print("  Pipeline 模拟结果")
    print(f"{'='*60}")
    if exit_code == 0:
        print("  ✅ 全部步骤成功")
    else:
        print("  ❌ 有步骤失败，请检查上方输出")
    print(f"\n  报告: {ROOT / 'allure-report.html'}")
    print(f"  结果: {ROOT / 'allure-results'}")
    print()

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
