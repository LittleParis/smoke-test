#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
企业微信机器人通知脚本

用法:
    python scripts/notify_wecom.py \
        --webhook $WECOM_WEBHOOK \
        --results allure-results \
        --build-url "$(Build.BuildUri)" \
        --branch "$(Build.SourceBranch)" \
        --trigger "$(Build.Reason)" \
        --notify-always
"""

import argparse
import ast
import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import requests


def load_json(filepath):
    """加载 JSON 文件，兼容 Python dict 单引号格式"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    try:
        return json.loads(content)
    except Exception:
        pass
    try:
        return ast.literal_eval(content)
    except Exception:
        return None


def parse_results(results_dir):
    """解析 allure-results 目录中的测试结果"""
    results_dir = Path(results_dir)
    results = []

    for f in results_dir.glob("*-result.json"):
        data = load_json(f)
        if data:
            results.append(data)

    return results


def get_stats(results):
    """统计测试结果"""
    by_status = defaultdict(int)
    failed_cases = []

    for r in results:
        status = r.get("status", "unknown")
        by_status[status] += 1

        if status in ("failed", "broken"):
            name = r.get("name", "Unknown")
            error_msg = ""
            status_details = r.get("statusDetails", {})
            if status_details.get("message"):
                error_msg = status_details["message"].split("\n")[0][:50]
            failed_cases.append({"name": name, "error": error_msg})

    return by_status, failed_cases


def format_duration(results):
    """计算总耗时"""
    start_times = [r.get("start", 0) for r in results if r.get("start")]
    stop_times = [r.get("stop", 0) for r in results if r.get("stop")]

    if start_times and stop_times:
        min_start = min(start_times)
        max_stop = max(stop_times)
        duration_ms = max_stop - min_start
        if duration_ms < 60000:
            return f"{duration_ms/1000:.1f}s"
        else:
            return f"{duration_ms/60000:.1f}m"
    return "N/A"


def build_message(stats, failed_cases, build_url, branch, trigger, duration):
    """构建企微 Markdown 消息"""
    total = sum(stats.values())
    passed = stats.get("passed", 0)
    failed = stats.get("failed", 0)
    broken = stats.get("broken", 0)

    # 判断整体状态
    if failed > 0 or broken > 0:
        status_icon = "❌"
        status_text = "失败"
    else:
        status_icon = "✅"
        status_text = "通过"

    # 构建消息
    lines = [
        f"## {status_icon} 冒烟测试报告",
        "",
        f"**状态**: {status_text}",
        f"**分支**: {branch or 'N/A'}",
        f"**触发**: {trigger or 'N/A'}",
        "",
        f"**统计**: {total} 总计 | {passed} 通过 | {failed} 失败 | {broken} 异常",
        f"**耗时**: {duration}",
    ]

    if build_url:
        lines.append("")
        lines.append(f"[查看详细报告]({build_url})")

    # 失败用例列表（最多展示 5 个）
    if failed_cases:
        lines.append("")
        lines.append("### 失败用例")
        for i, case in enumerate(failed_cases[:5], 1):
            error = case["error"] or "无错误信息"
            lines.append(f"{i}. {case['name'][:30]} - {error}")

        if len(failed_cases) > 5:
            lines.append(f"... 还有 {len(failed_cases) - 5} 个失败用例")

    return "\n".join(lines)


def send_notification(webhook, message):
    """发送企微通知"""
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content": message
        }
    }

    try:
        resp = requests.post(webhook, json=payload, timeout=10)
        resp.raise_for_status()
        result = resp.json()
        if result.get("errcode") == 0:
            print("[OK] 企微通知发送成功")
            return True
        else:
            print(f"[ERROR] 企微通知发送失败: {result.get('errmsg')}")
            return False
    except Exception as e:
        print(f"[ERROR] 企微通知发送异常: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="企业微信冒烟测试通知")
    parser.add_argument("--webhook", required=True, help="企微机器人 Webhook URL")
    parser.add_argument("--results", default="allure-results", help="allure-results 目录路径")
    parser.add_argument("--build-url", default="", help="构建详情页链接")
    parser.add_argument("--branch", default="", help="分支名")
    parser.add_argument("--trigger", default="", help="触发原因")
    parser.add_argument("--notify-always", action="store_true", help="无论成功失败都发通知")
    parser.add_argument("--dry-run", action="store_true", help="只打印消息不发送（本地测试用）")

    args = parser.parse_args()

    # 解析结果
    results = parse_results(args.results)
    if not results:
        print("[WARN] 未找到测试结果，跳过通知")
        return

    stats, failed_cases = get_stats(results)
    duration = format_duration(results)

    # 判断是否需要发送
    has_failure = stats.get("failed", 0) > 0 or stats.get("broken", 0) > 0
    if not has_failure and not args.notify_always:
        print("[INFO] 测试全部通过，跳过通知（使用 --notify-always 可始终发送）")
        return

    # 构建并发送消息
    message = build_message(stats, failed_cases, args.build_url, args.branch, args.trigger, duration)
    print(f"[INFO] 通知内容:\n{message}\n")

    if args.dry_run:
        print("[INFO] --dry-run 模式，跳过发送")
        return

    send_notification(args.webhook, message)


if __name__ == "__main__":
    main()
