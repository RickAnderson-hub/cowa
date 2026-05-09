#!/usr/bin/env python3
import sys

import display
import save_load
import engine
from adventures import ADVENTURES


TITLE_ART = """
  ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★
  ★                                                             ★
  ★        C H O O S E   Y O U R   A D V E N T U R E          ★
  ★                                                             ★
  ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★
"""


def main():
    while True:
        result = main_menu()
        if result == "quit":
            display.clear_screen()
            print()
            display.print_title("See you next time, adventurer!")
            sys.exit(0)


def main_menu() -> str:
    display.clear_screen()
    display.print_title(TITLE_ART)

    has_autosave = save_load.autosave_exists()
    saves = save_load.list_saves()

    print()
    display.print_choice(1, "New Game")
    if has_autosave:
        display.print_choice(2, "Continue (last autosave)")
    if saves:
        display.print_choice(3, "Load a saved game")
    display.print_choice(9, "Quit")
    print()

    while True:
        try:
            raw = input("  > ").strip()
        except (EOFError, KeyboardInterrupt):
            return "quit"

        if raw == "1":
            return _new_game()
        elif raw == "2" and has_autosave:
            return _load_and_run("autosave")
        elif raw == "3" and saves:
            return _pick_save(saves)
        elif raw == "9":
            return "quit"
        else:
            display.print_error("Please choose a valid option.")


def _pick_adventure() -> dict | None:
    display.clear_screen()
    display.print_title("CHOOSE YOUR ADVENTURE")
    print()

    adv_list = list(ADVENTURES.values())
    for i, adv in enumerate(adv_list, start=1):
        display.print_choice(i, f"{adv['title']}  —  {adv['description']}")
    display.print_choice(0, "Back")
    print()

    while True:
        try:
            raw = input("  > ").strip()
        except (EOFError, KeyboardInterrupt):
            return None

        if raw == "0":
            return None
        try:
            n = int(raw)
            if 1 <= n <= len(adv_list):
                return adv_list[n - 1]
        except ValueError:
            pass
        display.print_error("Please enter a valid number.")


def _new_game() -> str:
    adventure = _pick_adventure()
    if adventure is None:
        return "menu"

    display.clear_screen()
    display.print_title(f"NEW GAME  ·  {adventure['title']}")
    print()
    display.print_info("What is your name, adventurer?")
    print()

    while True:
        try:
            raw = input("  > ").strip()
        except (EOFError, KeyboardInterrupt):
            return "menu"
        if raw:
            player_name = raw[:30]
            break
        display.print_error("Please enter your name!")

    state = save_load.new_game_state(
        player_name,
        adventure["id"],
        adventure["start_scene"],
    )

    start = adventure["story"][adventure["start_scene"]]
    display.clear_screen()
    display.print_chapter_banner(1, start.get("chapter_title", "Chapter 1"))
    display.pause()

    result = engine.run_game(state, adventure)
    return result if result != "restart" else "menu"


def _load_and_run(slot: str) -> str:
    try:
        state = save_load.load_game(slot)
    except Exception as e:
        display.print_error(f"Could not load save: {e}")
        display.pause()
        return "menu"

    adventure_id = state.get("adventure_id", "space_explorer")
    adventure = ADVENTURES.get(adventure_id)
    if adventure is None:
        display.print_error(f"Unknown adventure '{adventure_id}' in save file.")
        display.pause()
        return "menu"

    result = engine.run_game(state, adventure)
    return result if result != "restart" else "menu"


def _pick_save(saves: list) -> str:
    display.clear_screen()
    display.print_title("LOAD GAME")
    print()

    adv_titles = {k: v["title"] for k, v in ADVENTURES.items()}

    for i, s in enumerate(saves, start=1):
        ts = s.get("save_timestamp", "")[:10]
        ch = s.get("chapter", "?")
        name = s.get("player_name", "???")
        adv = adv_titles.get(s.get("adventure_id", ""), "Unknown Adventure")
        display.print_choice(i, f"{name}  |  {adv}  |  Chapter {ch}  |  {ts}")

    display.print_choice(0, "Back to main menu")
    print()

    while True:
        try:
            raw = input("  > ").strip()
        except (EOFError, KeyboardInterrupt):
            return "menu"

        if raw == "0":
            return "menu"
        try:
            n = int(raw)
            if 1 <= n <= len(saves):
                return _load_and_run(saves[n - 1]["slot"])
        except ValueError:
            pass
        display.print_error("Please enter a valid number.")


if __name__ == "__main__":
    main()
