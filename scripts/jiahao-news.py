#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os, platform, random

if platform.system() == "Windows":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")

try:
    from colorama import init, Fore, Style
    init()
    C, S = Fore, Style
except ImportError:
    class F:
        def __getattr__(s, _): return ""
    C = F(); S = F()

FACTS = [
    "嘉豪梗起源于2024年，一名叫政阳不是羊的中学生在教室模仿Alan Walker虚空打碟，视频标签被误打成嘉豪后爆火。",
    "2024年10月，Alan Walker本人主动联系政阳面基，送了签名夹克和《五年高考三年模拟》。",
    "2026年，质疑嘉豪理解嘉豪成为嘉豪成为流行语，嘉豪从贬义词演变为精神符号。",
    "嘉豪的最高境界是自在极意豪——浑然天成地装酷而不自知。一旦自知即降级。",
    "程序员嘉豪核心技能：打开CMD -> color 0a -> dir /s -> tree -> 声称在入侵服务器。",
    "嘉欣是女性版嘉豪，同样黑色卫衣+3D口罩+虚空打碟。",
]

QUOTES = [
    ("十年的仇难道不报了吗", "嘉豪原视频经典台词"),
    ("黑帽衫束脚裤，我叫嘉豪你记住", "嘉豪登场诗"),
    ("一眼嘉豪", "一眼看出嘉豪特征"),
    ("这个没法喷，纯种赛级", "嘉豪最高评价"),
    ("质疑嘉豪，理解嘉豪，成为嘉豪", "2026嘉豪三段论"),
    ("底层架构你们不懂", "程序员嘉豪万能搪塞语"),
    ("代码和暴雨都懂我的孤独", "雨中coding专用emo文案"),
    ("一遍过，零bug", "做题学霸嘉豪标配呐喊"),
    ("凌晨十一点，城市灯火配代码", "职场嘉豪加班朋友圈"),
]

BRANCHES = [
    ("雨中嘉豪", "下雨拒绝撑伞，淋雨绕操场独行"),
    ("军训兵王嘉豪", "基础训练摆特战兵姿态，实际体力垫底"),
    ("CMD嘉豪", "color 0a开启黑客模式，dir /s滚动屏幕"),
    ("做题学霸嘉豪", "简单题做对大喊全对零失误，复杂题卡壳"),
    ("白板金融嘉豪", "抢占教室多媒体展示K线，假装校园股神"),
    ("巡视高冷嘉豪", "耳机不放歌，双手插兜踱步"),
    ("舞蹈体育嘉豪", "无球虚空三分，走廊即兴街舞"),
    ("电音嘉豪", "黑色卫衣+3D口罩，The Spectre中虚空打碟"),
]

def hr(title, color=None):
    c = color or C.MAGENTA
    r = S.RESET_ALL
    print()
    print(c + S.BRIGHT + "=" * 60 + r)
    print(c + S.BRIGHT + "  " + title + r)
    print(c + S.BRIGHT + "=" * 60 + r)
    print()

def show_daily():
    hr("嘉豪日报 | JIAHAO DAILY", C.MAGENTA)
    print(C.CYAN + "今日嘉豪冷知识" + S.RESET_ALL)
    print("  " + random.choice(FACTS))
    print()
    q, s = random.choice(QUOTES)
    print(C.GREEN + "今日嘉豪语录" + S.RESET_ALL)
    print("  " + q)
    print("  -- " + s)
    print()
    b, d = random.choice(BRANCHES)
    print(C.YELLOW + "今日嘉豪分支" + S.RESET_ALL)
    print("  " + b + ": " + d)
    print()
    print(C.WHITE + "今日豪意值：" + str(random.randint(75, 99)) + "%" + S.RESET_ALL)
    print("  BGM: The Spectre - Alan Walker")
    print()

def show_quote():
    hr("随机嘉豪语录", C.GREEN)
    q, s = random.choice(QUOTES)
    print("  " + q)
    print("  -- " + s)
    print()

def show_wiki():
    hr("嘉豪百科速览", C.CYAN)
    print("  [起源] 2024年，教室，Alan Walker模仿，标签误打")
    print("  [人设] 黑色卫衣+3D口罩，The Spectre BGM下虚空打碟")
    print("  [最高境界] 自在极意豪——浑然天成，装酷而不自知")
    print("  [演化] 嘲讽期(2024) -> 反思期(2025) -> 共鸣期(2026)")
    print("  [AW连接] Alan Walker本人2024年10月面基，送签名夹克+五三")
    print()
    print(C.YELLOW + "  [嘉豪宇宙分支]" + S.RESET_ALL)
    for b, d in BRANCHES:
        print("    - " + b + ": " + d)
    print()

def show_search():
    hr("嘉豪热梗搜索指南", C.GREEN)
    print("  由于嘉豪梗持续演化，建议通过以下渠道获取最新动态：")
    print()
    print("  抖音: 搜索 嘉豪 / 嘉豪合集 / 隔壁班嘉豪")
    print("  B站: 搜索 嘉豪合集 / 嘉豪名场面")
    print("  知乎: 话题 为什么嘉豪梗这么火")
    print("  百度百科: 嘉豪词条（持续更新）")
    print()
    print("  提示: 用 Claude Code 的 WebSearch 功能可实时搜索最新嘉豪梗")
    print()

def main():
    import argparse
    p = argparse.ArgumentParser(description="JIAHAO NEWS FETCHER")
    p.add_argument("--search", action="store_true")
    p.add_argument("--wiki", action="store_true")
    p.add_argument("--quote", action="store_true")
    p.add_argument("--daily", action="store_true")
    args = p.parse_args()
    if not any([args.search, args.wiki, args.quote, args.daily]):
        args.daily = True
    if args.daily: show_daily()
    if args.search: show_search()
    if args.wiki: show_wiki()
    if args.quote: show_quote()

if __name__ == "__main__":
    main()
