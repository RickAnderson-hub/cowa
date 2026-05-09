import os
import sys
import time
import textwrap

# ANSI codes
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
GREEN   = "\033[92m"
RED     = "\033[91m"
MAGENTA = "\033[95m"
BLUE    = "\033[94m"
WHITE   = "\033[97m"

_ANSI_SUPPORTED = None


def _check_ansi() -> bool:
    if sys.platform == "win32":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            return True
        except Exception:
            return False
    return os.environ.get("TERM", "xterm") != "dumb"


def _ansi(code: str, text: str) -> str:
    global _ANSI_SUPPORTED
    if _ANSI_SUPPORTED is None:
        _ANSI_SUPPORTED = _check_ansi()
    if _ANSI_SUPPORTED:
        return f"{code}{text}{RESET}"
    return text


def clear_screen():
    os.system("cls" if sys.platform == "win32" else "clear")


def slow_print(text: str, delay: float = 0.025):
    wrapped = _wrap(text)
    for char in wrapped:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char not in (" ", "\n"):
            time.sleep(delay)
    print()


def _wrap(text: str, width: int = 72) -> str:
    lines = []
    for paragraph in text.split("\n"):
        if paragraph.strip() == "":
            lines.append("")
        else:
            lines.extend(textwrap.wrap(paragraph, width) or [""])
    return "\n".join(lines)


def print_title(text: str):
    print()
    print(_ansi(BOLD + YELLOW, text))
    print()


def print_scene_title(title: str):
    print()
    print(_ansi(BOLD + CYAN, f"  ── {title} ──"))
    print()


def print_scene_text(text: str):
    for line in _wrap(text).split("\n"):
        print(_ansi(CYAN, f"  {line}") if line.strip() else "")


def print_choice(n: int, text: str, locked: bool = False, need: str = ""):
    if locked:
        label = f"  {n}) {text}  (Need: {need})"
        print(_ansi(DIM, label))
    else:
        label = f"  {n}) {text}"
        print(_ansi(GREEN, label))


def print_item_acquired(item_name: str, icon: str = ""):
    print()
    msg = f"  ★ You got: {icon} {item_name}!".strip()
    print(_ansi(BOLD + MAGENTA, msg))
    print()


def print_item_lost(item_name: str, icon: str = ""):
    print()
    msg = f"  ✗ Lost: {icon} {item_name}".strip()
    print(_ansi(BOLD + RED, msg))
    print()


def print_chapter_banner(n: int, title: str):
    stars = "★" * 60
    print()
    print(_ansi(BOLD + YELLOW, stars))
    print(_ansi(BOLD + YELLOW, f"  CHAPTER {n}: {title.upper()}"))
    print(_ansi(BOLD + YELLOW, stars))
    print()


def print_inventory(items: list, item_registry: dict):
    print()
    print(_ansi(BOLD + WHITE, "  ── Your Inventory ──"))
    if not items:
        print(_ansi(DIM, "  (empty)"))
    else:
        for item_id in items:
            item = item_registry.get(item_id, {})
            name = item.get("name", item_id)
            icon = item.get("icon", "")
            desc = item.get("description", "")
            print(_ansi(MAGENTA, f"  {icon} {name}") + _ansi(DIM, f"  — {desc}"))
    print()


def print_win_screen(player_name: str):
    clear_screen()
    banner = [
        "  *  .  . *   .   *   .  *  .  *   .  *  .  *   .  *   .  *",
        "                                                              ",
        "        *    C O N G R A T U L A T I O N S !    *            ",
        "                                                              ",
        f"       {player_name}, you saved the galaxy!                  ",
        "                                                              ",
        "  *  .  . *   .   *   .  *  .  *   .  *  .  *   .  *   .  *",
    ]
    print()
    for line in banner:
        print(_ansi(BOLD + YELLOW, line))
    print()


def print_lose_screen(player_name: str, reason: str = ""):
    clear_screen()
    banner = [
        "  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X",
        "                                                              ",
        "           *   M I S S I O N   F A I L E D   *               ",
        "                                                              ",
        f"       Don't give up, {player_name}! Try again!             ",
        "                                                              ",
        "  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X",
    ]
    print()
    for line in banner:
        print(_ansi(BOLD + RED, line))
    if reason:
        print()
        print(_ansi(DIM, f"  ({reason})"))
    print()


def print_separator():
    print(_ansi(DIM, "  " + "─" * 68))


def pause(prompt: str = "  [Press Enter to continue...]"):
    print()
    print(_ansi(DIM, prompt), end="", flush=True)
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        pass
    print()


def print_error(text: str):
    print(_ansi(RED, f"  ! {text}"))


def print_info(text: str):
    print(_ansi(BLUE, f"  → {text}"))
