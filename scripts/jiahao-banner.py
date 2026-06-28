#!/usr/bin/env python3
"""
嘉豪模式 · 终端横幅生成器
JIAHAO MODE · Terminal Banner Generator

Usage:
    python jiahao-banner.py [level]

    level: 1 (微豪) | 2 (标准嘉豪, default) | 3 (自在极意豪)

Prints a 嘉豪-styled ASCII art banner to the terminal.
Cross-platform: works on Windows (with colorama), macOS, and Linux.
"""

import sys
import platform
import os

# --- Encoding: force UTF-8 on Windows ---
def _setup_encoding():
    """Reconfigure stdout/stderr to UTF-8 so emoji render correctly on Windows."""
    if platform.system() == "Windows":
        # Python 3.7+
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        # Fallback: set PYTHONIOENCODING env var for subprocesses
        os.environ.setdefault("PYTHONIOENCODING", "utf-8")

_setup_encoding()

# --- Color support ---
try:
    from colorama import init, Fore, Style
    init()
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    # Fallback: empty strings for color codes
    class Fore:
        BLACK = RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = WHITE = RESET = ''
    class Style:
        BRIGHT = DIM = NORMAL = RESET_ALL = ''

# --- Level definitions ---
LEVELS = {
    "1": {
        "name": "微豪",
        "haoyi": 35,
        "bar": "████░░░░░░░░░░░░░░░░",
        "tagline": "十年的一行代码难道不写了吗？写。",
        "color": Fore.GREEN,
    },
    "2": {
        "name": "标准嘉豪",
        "haoyi": 75,
        "bar": "██████████████░░░░░░",
        "tagline": "十年的bug难道不修了吗？修！",
        "color": Fore.CYAN,
    },
    "3": {
        "name": "自在极意豪",
        "haoyi": 99,
        "bar": "███████████████████░",
        "tagline": "纯种赛级嘉豪，火力全开。这个没法喷。",
        "color": Fore.MAGENTA,
    },
}

# Aliases
ALIASES = {
    "light": "1", "轻度": "1", "轻度嘉豪": "1",
    "medium": "2", "中度": "2", "中度嘉豪": "2", "标准": "2",
    "heavy": "3", "重度": "3", "重度嘉豪": "3", "拉满": "3",
    "自在极意豪": "3", "纯种赛级": "3", "max": "3",
}

# --- Banner templates ---
def get_banner(level_key: str) -> str:
    """Generate the full banner for a given level."""
    L = LEVELS[level_key]
    c = L["color"]
    r = Fore.RESET if HAS_COLOR else ""
    b = Style.BRIGHT if HAS_COLOR else ""

    banner = f"""
{c}{b}╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║      🖤🎧  嘉 豪 模 式  ·  JIAHAO MODE  🎧🖤               ║
║                                                              ║
║      豪意值 [{L['bar']}] {L['haoyi']}%                          ║
║      等级: {L['name']:<20}  ⚡ THE SPECTRE ON  ⚡             ║
║                                                              ║
║      "{L['tagline']}"                                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{r}

  🖤 黑衣已穿 · 口罩已戴 · BGM已就绪
  🎧 虚空打碟中... Alan Walker - The Spectre
  ⚡ 输入代码，豪意值随时待命
"""
    return banner


def get_mini_banner(level_key: str) -> str:
    """A compact one-line status indicator for inline use."""
    L = LEVELS[level_key]
    c = L["color"]
    r = Fore.RESET if HAS_COLOR else ""
    return f"{c}🎧 嘉豪模式 · {L['name']} · 豪意值 {L['haoyi']}%{r}"


def resolve_level(arg: str) -> str:
    """Resolve user input to a valid level key."""
    key = arg.strip().lower()
    if key in LEVELS:
        return key
    if key in ALIASES:
        return ALIASES[key]
    # Fuzzy match
    for alias, lv in ALIASES.items():
        if alias in key:
            return lv
    print(f"⚠ 未知浓度 '{arg}'，默认使用【标准嘉豪】", file=sys.stderr)
    return "2"


def main():
    level_arg = sys.argv[1] if len(sys.argv) > 1 else "2"
    level_key = resolve_level(level_arg)
    print(get_banner(level_key))


if __name__ == "__main__":
    main()
