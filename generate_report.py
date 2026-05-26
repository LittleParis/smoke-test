#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从 allure-results 生成可读的 HTML 报告
用法: python generate_report.py [output.html]
"""

import ast
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict


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


def format_duration(ms):
    """格式化持续时间"""
    if ms is None:
        return "-"
    if ms < 1000:
        return f"{ms}ms"
    elif ms < 60000:
        return f"{ms/1000:.2f}s"
    else:
        return f"{ms/60000:.2f}m"


def get_status_icon(status):
    """获取状态图标"""
    icons = {
        "passed": "✅",
        "failed": "❌",
        "broken": "💔",
        "skipped": "⏭️"
    }
    return icons.get(status, "❓")


def get_status_color(status):
    """获取状态颜色"""
    colors = {
        "passed": "#28a745",
        "failed": "#dc3545",
        "broken": "#fd7e14",
        "skipped": "#6c757d"
    }
    return colors.get(status, "#6c757d")


def generate_html(results, attachments, output_path):
    """生成 HTML 报告"""

    # 统计
    total = len(results)
    by_status = defaultdict(int)
    by_feature = defaultdict(lambda: defaultdict(int))

    for r in results:
        status = r.get("status", "unknown")
        by_status[status] += 1
        feature = "Unknown"
        for label in r.get("labels", []):
            if label.get("name") == "feature":
                feature = label.get("value", "Unknown")
                break
        by_feature[feature][status] += 1

    # 开始时间
    start_times = [r.get("start", 0) for r in results if r.get("start")]
    min_start = min(start_times) if start_times else 0
    max_stop = max([r.get("stop", 0) for r in results if r.get("stop")] or [0])

    # HTML 模板
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smoke Test Report</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f5f5f5; color: #333; }}
        .container {{ max-width: 1400px; margin: 0 auto; padding: 20px; }}
        h1 {{ color: #2c3e50; margin-bottom: 20px; }}

        /* 统计卡片 */
        .stats {{ display: flex; gap: 15px; margin-bottom: 20px; flex-wrap: wrap; }}
        .stat-card {{ background: white; border-radius: 8px; padding: 20px; min-width: 120px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .stat-card h3 {{ font-size: 12px; color: #666; text-transform: uppercase; margin-bottom: 5px; }}
        .stat-card .value {{ font-size: 28px; font-weight: bold; }}
        .stat-card.passed .value {{ color: #28a745; }}
        .stat-card.failed .value {{ color: #dc3545; }}
        .stat-card.broken .value {{ color: #fd7e14; }}
        .stat-card.skipped .value {{ color: #6c757d; }}
        .stat-card.total .value {{ color: #2c3e50; }}

        /* 筛选 */
        .filters {{ background: white; border-radius: 8px; padding: 15px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); display: flex; gap: 15px; flex-wrap: wrap; align-items: center; }}
        .filters label {{ font-size: 14px; color: #666; }}
        .filters select {{ padding: 8px 12px; border: 1px solid #ddd; border-radius: 4px; font-size: 14px; cursor: pointer; }}
        .filters button {{ padding: 8px 16px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 14px; }}
        .filters button:hover {{ background: #0056b3; }}

        /* 表格 */
        .results-table {{ background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        table {{ width: 100%; border-collapse: collapse; }}
        th {{ background: #343a40; color: white; padding: 12px 15px; text-align: left; font-size: 13px; text-transform: uppercase; }}
        td {{ padding: 12px 15px; border-bottom: 1px solid #eee; font-size: 14px; vertical-align: top; }}
        tr:hover {{ background: #f8f9fa; }}
        tr.hidden {{ display: none; }}

        .status-badge {{ display: inline-block; padding: 4px 10px; border-radius: 12px; font-size: 12px; font-weight: 500; color: white; }}
        .status-passed {{ background: #28a745; }}
        .status-failed {{ background: #dc3545; }}
        .status-broken {{ background: #fd7e14; }}
        .status-skipped {{ background: #6c757d; }}

        .feature-badge {{ display: inline-block; padding: 3px 8px; background: #e9ecef; border-radius: 4px; font-size: 12px; color: #495057; }}
        .story-badge {{ display: inline-block; padding: 3px 8px; background: #fff3cd; border-radius: 4px; font-size: 12px; color: #856404; }}

        .name-cell {{ max-width: 300px; word-break: break-word; }}
        .error-cell {{ max-width: 400px; font-family: monospace; font-size: 12px; color: #dc3545; word-break: break-word; }}

        /* 详情展开 */
        .details-toggle {{ background: none; border: none; color: #007bff; cursor: pointer; font-size: 13px; padding: 5px 0; }}
        .details-toggle:hover {{ text-decoration: underline; }}
        .details-content {{ display: none; margin-top: 10px; background: #f8f9fa; border-radius: 4px; padding: 12px; }}
        .details-content.show {{ display: block; }}
        .details-content pre {{ white-space: pre-wrap; word-break: break-word; margin: 8px 0; font-size: 12px; }}
        .details-content .label {{ font-weight: bold; color: #495057; margin-bottom: 4px; }}

        /* 运行信息 */
        .run-info {{ background: white; border-radius: 8px; padding: 15px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); font-size: 14px; color: #666; }}
        .run-info span {{ margin-right: 20px; }}

        /* 按模块统计 */
        .feature-stats {{ background: white; border-radius: 8px; padding: 15px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .feature-stats h3 {{ margin-bottom: 10px; font-size: 14px; color: #333; }}
        .feature-stats table {{ font-size: 13px; }}
        .feature-stats th {{ background: #f8f9fa; color: #333; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🧪 Smoke Test Report</h1>

        <div class="run-info">
            <span>📅 时间: {datetime.fromtimestamp(min_start/1000).strftime('%Y-%m-%d %H:%M:%S') if min_start else 'N/A'}</span>
            <span>⏱️ 总耗时: {format_duration(max_stop - min_start) if min_start and max_stop else 'N/A'}</span>
            <span>📊 测试数: {total}</span>
        </div>

        <div class="stats">
            <div class="stat-card total">
                <h3>Total</h3>
                <div class="value">{total}</div>
            </div>
            <div class="stat-card passed">
                <h3>Passed</h3>
                <div class="value">{by_status.get("passed", 0)}</div>
            </div>
            <div class="stat-card failed">
                <h3>Failed</h3>
                <div class="value">{by_status.get("failed", 0)}</div>
            </div>
            <div class="stat-card broken">
                <h3>Broken</h3>
                <div class="value">{by_status.get("broken", 0)}</div>
            </div>
            <div class="stat-card skipped">
                <h3>Skipped</h3>
                <div class="value">{by_status.get("skipped", 0)}</div>
            </div>
        </div>

        <div class="feature-stats">
            <h3>按模块统计</h3>
            <table>
                <thead>
                    <tr><th>模块</th><th>通过</th><th>失败</th><th>异常</th><th>跳过</th><th>总计</th></tr>
                </thead>
                <tbody>
'''

    # 按模块统计
    for feature in sorted(by_feature.keys()):
        stats = by_feature[feature]
        row_total = sum(stats.values())
        html += f'''                    <tr>
                        <td>{feature}</td>
                        <td style="color:#28a745">{stats.get("passed", 0)}</td>
                        <td style="color:#dc3545">{stats.get("failed", 0)}</td>
                        <td style="color:#fd7e14">{stats.get("broken", 0)}</td>
                        <td style="color:#6c757d">{stats.get("skipped", 0)}</td>
                        <td>{row_total}</td>
                    </tr>
'''

    html += '''                </tbody>
            </table>
        </div>

        <div class="filters">
            <label>状态筛选:</label>
            <select id="statusFilter">
                <option value="all">全部</option>
                <option value="passed">✅ 通过</option>
                <option value="failed">❌ 失败</option>
                <option value="broken">💔 异常</option>
                <option value="skipped">⏭️ 跳过</option>
            </select>
            <label>模块筛选:</label>
            <select id="featureFilter">
                <option value="all">全部</option>
'''

    # 模块筛选选项
    for feature in sorted(by_feature.keys()):
        html += f'                <option value="{feature}">{feature}</option>\n'

    html += '''            </select>
            <button onclick="resetFilters()">重置</button>
        </div>

        <div class="results-table">
            <table>
                <thead>
                    <tr>
                        <th>状态</th>
                        <th>测试名称</th>
                        <th>模块</th>
                        <th>类型</th>
                        <th>耗时</th>
                        <th>错误信息</th>
                        <th>详情</th>
                    </tr>
                </thead>
                <tbody>
'''

    # 结果行
    for i, r in enumerate(results):
        status = r.get("status", "unknown")
        name = r.get("name", "Unknown")
        duration = (r.get("stop", 0) or 0) - (r.get("start", 0) or 0)

        # 获取 feature 和 story
        feature = ""
        story = ""
        for label in r.get("labels", []):
            if label.get("name") == "feature":
                feature = label.get("value", "")
            elif label.get("name") == "story":
                story = label.get("value", "")

        # 错误信息
        error_msg = ""
        status_details = r.get("statusDetails", {})
        if status_details.get("message"):
            error_msg = status_details["message"].split("\n")[0]  # 只取第一行

        # 获取附件
        req_attachment = None
        resp_attachment = None
        for att in r.get("attachments", []):
            att_name = att.get("name", "")
            source = att.get("source", "")
            if "请求" in att_name or "param" in att_name.lower():
                req_attachment = attachments.get(source)
            elif "响应" in att_name or "response" in att_name.lower():
                resp_attachment = attachments.get(source)

        # 详情内容
        details_id = f"details-{i}"
        req_json = json.dumps(req_attachment, ensure_ascii=False, indent=2) if req_attachment else "无"
        resp_json = json.dumps(resp_attachment, ensure_ascii=False, indent=2) if resp_attachment else "无"

        html += f'''                    <tr data-status="{status}" data-feature="{feature}">
                        <td><span class="status-badge status-{status}">{get_status_icon(status)} {status}</span></td>
                        <td class="name-cell">{name}</td>
                        <td><span class="feature-badge">{feature or '-'}</span></td>
                        <td><span class="story-badge">{story or '-'}</span></td>
                        <td>{format_duration(duration)}</td>
                        <td class="error-cell">{error_msg or '-'}</td>
                        <td>
                            <button class="details-toggle" onclick="toggleDetails('{details_id}')">展开</button>
                            <div id="{details_id}" class="details-content">
                                <div class="label">请求参数:</div>
                                <pre>{req_json}</pre>
                                <div class="label">响应内容:</div>
                                <pre>{resp_json}</pre>
                            </div>
                        </td>
                    </tr>
'''

    html += '''                </tbody>
            </table>
        </div>
    </div>

    <script>
        function toggleDetails(id) {
            const el = document.getElementById(id);
            const btn = el.previousElementSibling;
            if (el.classList.contains('show')) {
                el.classList.remove('show');
                btn.textContent = '展开';
            } else {
                el.classList.add('show');
                btn.textContent = '收起';
            }
        }

        function applyFilters() {
            const statusFilter = document.getElementById('statusFilter').value;
            const featureFilter = document.getElementById('featureFilter').value;
            const rows = document.querySelectorAll('tbody tr');

            rows.forEach(row => {
                const status = row.dataset.status;
                const feature = row.dataset.feature;
                const matchStatus = statusFilter === 'all' || status === statusFilter;
                const matchFeature = featureFilter === 'all' || feature === featureFilter;
                row.classList.toggle('hidden', !(matchStatus && matchFeature));
            });
        }

        function resetFilters() {
            document.getElementById('statusFilter').value = 'all';
            document.getElementById('featureFilter').value = 'all';
            applyFilters();
        }

        document.getElementById('statusFilter').addEventListener('change', applyFilters);
        document.getElementById('featureFilter').addEventListener('change', applyFilters);
    </script>
</body>
</html>
'''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

    return total, by_status


def main():
    # 路径
    script_dir = Path(__file__).parent
    results_dir = script_dir / "allure-results"
    output_path = script_dir / (sys.argv[1] if len(sys.argv) > 1 else "allure-report.html")

    print(f"[INFO] 读取 allure-results: {results_dir}")

    # 加载所有结果
    results = []
    attachments = {}

    for f in results_dir.glob("*-result.json"):
        data = load_json(f)
        if data:
            results.append(data)

    for f in results_dir.glob("*-attachment.json"):
        data = load_json(f)
        if data:
            # 从文件名提取 UUID
            uuid = f.stem
            attachments[uuid] = data
            # 也存 source 格式
            attachments[str(f.name)] = data

    print(f"[INFO] 找到 {len(results)} 个测试结果")
    print(f"[INFO] 找到 {len(attachments)} 个附件")

    # 生成报告
    total, by_status = generate_html(results, attachments, output_path)

    print(f"\n[OK] 报告已生成: {output_path}")
    print(f"   总计: {total} | 通过: {by_status.get('passed', 0)} | 失败: {by_status.get('failed', 0)} | 异常: {by_status.get('broken', 0)}")

    # 尝试在浏览器中打开
    import webbrowser
    webbrowser.open(f"file://{output_path.absolute()}")


if __name__ == "__main__":
    main()