#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
嘉豪模式 - 交互演示脚本
JIAHAO MODE - Interactive Demo

Usage:
    python demo.py              # Full automated showcase
    python demo.py --quick      # Quick preview (no typing effect)
    python demo.py --level 3    # Show only 自在极意豪 level
"""

import sys
import os
import time
import platform

# --- Encoding setup (Windows) ---
if platform.system() == "Windows":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")

# --- Color ---
try:
    from colorama import init, Fore, Style
    init()
    C = Fore
    S = Style
except ImportError:
    class Fake:
        def __getattr__(self, _): return ""
    C = Fake()
    S = Fake()

# ============================================================
# Demo scenarios: each has a title, user prompt, and 3 levels
# ============================================================

def L1(text):
    """轻度回复模板"""
    return text

def L2(text):
    """中度回复模板"""
    return text

def L3(text):
    """重度回复模板"""
    return text

SCENARIOS = []

# --- Scenario 1: Writing Code ---
SCENARIOS.append({
    "title": "场景一：写代码",
    "user_says": "帮我写个快速排序",
    "1": (
        "🌱 轻度 - 微豪",
        'def quicksort(arr):\n'
        '    if len(arr) <= 1:\n'
        '        return arr\n'
        '    pivot = arr[len(arr) // 2]\n'
        '    left = [x for x in arr if x < pivot]\n'
        '    middle = [x for x in arr if x == pivot]\n'
        '    right = [x for x in arr if x > pivot]\n'
        '    return quicksort(left) + middle + quicksort(right)\n'
        '\n'
        '# O(n log n)，稳稳的。这段代码的豪意值还行 🎧'
    ),
    "2": (
        "🔥 中度 - 标准嘉豪",
        '🎧 *(虚空打碟中扫了一眼排序需求)*\n'
        '\n'
        '十年的数组难道不排了吗？排！接好：\n'
        '\n'
        '```python\n'
        'def quicksort(arr):\n'
        '    if len(arr) <= 1:\n'
        '        return arr\n'
        '    pivot = arr[len(arr) // 2]  # 豪意值支点\n'
        '    left = [x for x in arr if x < pivot]\n'
        '    middle = [x for x in arr if x == pivot]\n'
        '    right = [x for x in arr if x > pivot]\n'
        '    return quicksort(left) + middle + quicksort(right)\n'
        '```\n'
        '\n'
        'O(n log n)，比The Spectre的drop还稳。一眼标准快排，豪意值75% 🔥'
    ),
    "3": (
        "🌪️ 重度 - 自在极意豪",
        '🖤 *(身穿黑色卫衣，推了推3D口罩，在雨中的The Spectre伴奏下双手飞舞)*\n'
        '\n'
        '十年的数组难道不排了吗？十年的O(n^2)难道不优化了吗？不！\n'
        '看我用自在极意豪之力终结乱序：\n'
        '\n'
        '```python\n'
        'def jiahao_quicksort(arr, haoyi_value=999):\n'
        '    """纯种赛级排序 | 豪意值MAX | 分治法的终极奥义"""\n'
        '    if len(arr) <= 1:\n'
        '        return arr  # 豪意值底线：只剩一个元素，已是自在极意豪\n'
        '    pivot = arr[len(arr) // 2]  # 🎧 支点选中间，豪意值最均衡\n'
        '    left = [x for x in arr if x < pivot]\n'
        '    middle = [x for x in arr if x == pivot]\n'
        '    right = [x for x in arr if x > pivot]\n'
        '    return (jiahao_quicksort(left, haoyi_value + 1)\n'
        '            + middle\n'
        '            + jiahao_quicksort(right, haoyi_value + 1))\n'
        '```\n'
        '\n'
        'O(n log n)平均，豪意值拉满。代码跑起来比AW全球巡演还流畅。\n'
        '这个快排没法喷，纯种赛级 🎧🔥'
    ),
})

# --- Scenario 2: Debugging ---
SCENARIOS.append({
    "title": "场景二：Debug",
    "user_says": "这个API怎么一直500？",
    "1": (
        "🌱 轻度 - 微豪",
        '看一下错误日志。大概率是 null pointer -- `user.address` 没判空。\n'
        '加上 optional chaining 就行。\n'
        '\n'
        '一眼嘉豪级别的bug，还好不是生产环境 🎧'
    ),
    "2": (
        "🔥 中度 - 标准嘉豪",
        '🎧 *(BGM突然卡了一下)* 豪意值警告 -- 500 Internal Server Error！\n'
        '\n'
        '让我探伤...找到了：`user.address.city`，`user` 可能是 undefined。\n'
        '十年的null难道不判了吗？\n'
        '\n'
        '加上 `user?.address?.city`，一行的事。豪意值回升至85%。再试试看。'
    ),
    "3": (
        "🌪️ 重度 - 自在极意豪",
        '🖤 *(身穿黑色卫衣，推了推3D口罩，凝视着500错误)*\n'
        '\n'
        '纯种赛级bug！`user.address.city` -- 三层嵌套没判空，豪意值直接归零。\n'
        '十年的null pointer难道不管了吗？十年的try-catch难道不写了吗？\n'
        '不！今天就让这个500终结在这里。\n'
        '\n'
        '```javascript\n'
        '// 豪意值修复：optional chaining + fallback\n'
        'const city = user?.address?.city ?? "自在极意豪市";\n'
        '```\n'
        '\n'
        '修了。服务器重新跑起来了，比AW的drop还稳。\n'
        '这个500没法喷，但修起来也就一行 🎧🔥'
    ),
})

# --- Scenario 3: Git Commit ---
SCENARIOS.append({
    "title": "场景三：Git提交",
    "user_says": "帮我commit一下",
    "1": (
        "🌱 轻度 - 微豪",
        '```bash\n'
        'git commit -m "fix: null pointer in user address lookup"\n'
        '```\n'
        '推上去了。豪意值+1 🎧'
    ),
    "2": (
        "🔥 中度 - 标准嘉豪",
        '🎧 *(虚空打碟中把所有改动加入暂存区)*\n'
        '\n'
        '```bash\n'
        'git commit -m "fix: 十年的null pointer难道不判了吗"\n'
        'git push\n'
        '```\n'
        '\n'
        '推上去了，豪意值+1。commit message一目了然，没法喷 🔥'
    ),
    "3": (
        "🌪️ 重度 - 自在极意豪",
        '🖤 *(身穿黑色卫衣，推了推3D口罩，在The Spectre鼓点中把改动推上远程)*\n'
        '\n'
        '```bash\n'
        'git add -A  # 豪意值暂存区，一个不漏\n'
        'git commit -m "fix: 十年的null pointer难道不判了吗 | 豪意值修复 | 纯种赛级patch"\n'
        'git push origin main  # 十年的代码难道不推了吗？推！\n'
        '```\n'
        '\n'
        '远程已同步。commit history豪意值+1。这个patch没法喷，纯种赛级 🎧🔥'
    ),
})


# ============================================================
# Display functions
# ============================================================

def type_out(text: str, delay: float = 0.0005):
    """Simulate typing effect."""
    if delay <= 0:
        print(text)
        return
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def show_divider(char: str = "─", width: int = 60):
    print(char * width)


def show_scenario(scenario: dict, level: str = "2"):
    """Display one scenario at a specific level."""
    show_divider("═")
    print(f"\n{C.YELLOW}{S.BRIGHT}{scenario['title']}{S.RESET_ALL}\n")
    print(f"{C.WHITE}🧑 用户：{scenario['user_says']}{S.RESET_ALL}\n")
    label, response = scenario.get(level, scenario["2"])
    print(f"{label}：\n")
    print(response)
    print()


def show_all_levels(scenario: dict, delay: float = 0.01):
    """Show one scenario at all 3 levels sequentially."""
    show_divider("═", 70)
    print(f"\n{C.YELLOW}{S.BRIGHT}{scenario['title']}{S.RESET_ALL}")
    print(f"{C.WHITE}🧑 用户：{scenario['user_says']}{S.RESET_ALL}\n")

    for lv in ["1", "2", "3"]:
        label, response = scenario[lv]
        show_divider("─", 50)
        print(f"\n{label}：\n")
        type_out(response, delay)
        if lv != "3":
            time.sleep(0.3)
        print()


def show_header():
    """Main demo header."""
    print(f"""
{C.MAGENTA}{S.BRIGHT}
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║        🖤🎧  嘉 豪 模 式  |  JIAHAO MODE  🎧🖤                 ║
║                    交 互 演 示  |  INTERACTIVE DEMO                ║
║                                                                  ║
║        "质疑嘉豪，理解嘉豪，成为嘉豪"                              ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
{S.RESET_ALL}

{C.GREEN}✨ 三个场景 × 三层浓度 = 九种嘉豪风味{S.RESET_ALL}

{C.WHITE}按 Enter 开始演示，或 Ctrl+C 退出...{S.RESET_ALL}
""")


def show_outro():
    """Closing message."""
    print(f"""
{C.MAGENTA}{S.BRIGHT}
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║        🖤  演 示 结 束  |  DEMO COMPLETE  🖤                     ║
║                                                                  ║
║        安装：claude skills install jiahao-mode                     ║
║        GitHub: github.com/lhao17202-hue/jiahao-mode                ║
║                                                                  ║
║        ⭐ Star = 豪意值 +1                                       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
{S.RESET_ALL}

{C.GREEN}十年的star难道不点了吗？点！ 🎧🔥{S.RESET_ALL}
""")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="嘉豪模式 | 交互演示")
    parser.add_argument("--quick", action="store_true", help="快速预览（无打字效果）")
    parser.add_argument("--level", type=str, default="all",
                        choices=["1", "2", "3", "all"],
                        help="只展示一个浓度等级")
    args = parser.parse_args()

    delay = 0 if args.quick else 0.008

    show_header()
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        print()
        return

    print("\n" * 2)

    for i, scenario in enumerate(SCENARIOS):
        if args.level != "all":
            show_scenario(scenario, args.level)
        else:
            show_all_levels(scenario, delay)
        if i < len(SCENARIOS) - 1:
            time.sleep(0.5)

    show_outro()


if __name__ == "__main__":
    main()
