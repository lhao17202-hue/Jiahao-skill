#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alan Walker 签名输出器 · AW SIGNATURE GENERATOR

Usage:
    python aw-logo.py --inline    # AW one-line signatures
    python aw-logo.py --banner    # AW text banner (no ASCII art)
    python aw-logo.py             # Show all

Alan Walker，挪威电音制作人。2013年设计了经典的AW交错标识。
黑色连帽卫衣 + 口罩是他的标志造型。嘉豪模仿的核心对象。
"""

import sys, os, platform

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

AW_INLINE_SIGS = """
AW One-line Signatures (for commit messages / code comments):

  // 🎧 AW · The Spectre ON
  # [AW] THE SPECTRE · 豪意值 MAX
  /* AW · WALKER · 自在极意豪 */
  <!-- 🎧 AW · THE SPECTRE -->
  # AW · 虚空打碟中
  // AW · WALKER × 嘉豪
"""

AW_BANNER = r"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║              🎧  ALAN WALKER · THE SPECTRE  🎧               ║
║              🖤  WALKER × 嘉豪 · 自在极意豪  🖤               ║
║                                                              ║
║       "在别人眼里中二的瞬间，正是你最勇敢最真实的时刻"          ║
║                           — Alan Walker                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

AW_QUICK_FACTS = """
Alan Walker Quick Facts:
  - 挪威电音制作人/DJ，1997年生
  - 代表作: Faded (35亿+播放), The Spectre, Alone, Darkside
  - 标志造型: 黑色连帽卫衣 + 口罩遮脸
  - AW标识: 2013年亲自设计，A与W几何线条交织
  - 理念: "任何人都可以成为Walker"——穿卫衣戴口罩你就是Walker
  - 2024年10月主动面基"嘉豪"政阳，送签名夹克+《五年高考三年模拟》
  - 2025年7月发布鼓励视频获赞26.5万
"""

def sec(title, color=None):
    c = color or C.MAGENTA
    r = S.RESET_ALL
    print(f"\n{c}{S.BRIGHT}{'='*60}{r}")
    print(f"{c}{S.BRIGHT}  {title}{r}")
    print(f"{c}{S.BRIGHT}{'='*60}{r}\n")

def show_all():
    sec("AW QUICK FACTS", C.CYAN)
    print(AW_QUICK_FACTS)
    sec("AW TEXT BANNER", C.MAGENTA)
    print(AW_BANNER)
    sec("AW ONE-LINE SIGNATURES", C.GREEN)
    print(AW_INLINE_SIGS)

def show_banner():
    print(AW_BANNER)

def show_inline():
    print(AW_INLINE_SIGS)

def main():
    import argparse
    p = argparse.ArgumentParser(description="AW SIGNATURE GENERATOR")
    p.add_argument("--inline", action="store_true", help="AW one-line signatures")
    p.add_argument("--banner", action="store_true", help="AW text banner")
    args = p.parse_args()
    if not any([args.inline, args.banner]):
        show_all()
    else:
        if args.banner: show_banner()
        if args.inline: show_inline()

if __name__ == "__main__":
    main()
