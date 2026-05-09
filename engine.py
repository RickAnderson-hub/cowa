import time

import display
import save_load
from inventory import Inventory


def run_game(state: dict, adventure: dict) -> str:
    """
    Main game loop. Returns 'quit', 'restart', or 'menu' when the loop ends.
    """
    story = adventure["story"]
    items = adventure["items"]
    inv = Inventory(state.get("inventory", []), items)
    _last_chapter = state.get("chapter", 1)

    while True:
        scene_id = state["current_scene"]

        if scene_id not in story:
            display.print_error(f"Missing scene: '{scene_id}'. Returning to menu.")
            return "menu"

        scene = story[scene_id]

        # Chapter banner on chapter transition
        chapter = scene.get("chapter", 1)
        chapter_title = scene.get("chapter_title", "")
        if chapter != _last_chapter:
            display.clear_screen()
            display.print_chapter_banner(chapter, chapter_title)
            display.pause()
            _last_chapter = chapter
            state["chapter"] = chapter

        # Display scene
        display.clear_screen()
        _show_scene_header(scene)
        _show_scene_text(scene, state["player_name"])

        # Handle auto-next (no choice)
        if scene.get("auto_next"):
            display.pause()
            state["current_scene"] = scene["auto_next"]
            _record_visit(state, scene_id)
            save_load.autosave(state)
            continue

        # Handle ending
        if scene.get("ending") == "win":
            display.print_win_screen(state["player_name"])
            save_load.autosave(state)
            display.pause("  [Press Enter to return to the main menu...]")
            return "menu"

        if scene.get("ending") == "lose":
            display.print_lose_screen(state["player_name"], scene.get("lose_reason", ""))
            save_load.autosave(state)
            display.pause("  [Press Enter to return to the main menu...]")
            return "menu"

        # Build choice list
        choices = scene.get("choices", [])
        if not choices:
            display.pause()
            return "menu"

        # If every choice is locked, the player can't progress — show a lose screen
        all_locked = all(
            bool(c.get("requires_item") and not inv.has(c["requires_item"]))
            for c in choices
        )
        if all_locked:
            missing = [
                items.get(c["requires_item"], {}).get("name", c["requires_item"])
                for c in choices if c.get("requires_item")
            ]
            reason = f"You needed: {', '.join(dict.fromkeys(missing))}" if missing else ""
            display.print_lose_screen(state["player_name"], reason)
            save_load.autosave(state)
            display.pause("  [Press Enter to return to the main menu...]")
            return "menu"

        # Show choices
        _show_choices(choices, inv, items)

        # Show inventory hint
        print()
        display.print_info("Type a number to choose, or 'I' for inventory, 'Q' to quit")
        print()

        # Get player input
        action = _get_input(choices, inv, items)

        if action == "quit":
            save_load.save_game({**state, "inventory": inv.to_list()}, "autosave")
            return "quit"
        elif action == "inventory":
            display.clear_screen()
            inv.display()
            display.pause("  [Press Enter to go back...]")
            continue
        elif action == "menu":
            save_load.save_game({**state, "inventory": inv.to_list()}, "autosave")
            return "menu"

        # action is an int — zero-based index into choices
        chosen = choices[action]

        # Apply gives_item from the choice
        if chosen.get("gives_item"):
            item_id = chosen["gives_item"]
            if inv.add(item_id):
                item = items.get(item_id, {})
                display.print_item_acquired(item.get("name", item_id), item.get("icon", ""))
                time.sleep(1.2)

        # Apply removes_item from the choice (consequence of dangerous paths)
        if chosen.get("removes_item"):
            item_id = chosen["removes_item"]
            if inv.remove(item_id):
                item = items.get(item_id, {})
                display.print_item_lost(item.get("name", item_id), item.get("icon", ""))
                time.sleep(1.0)

        _record_visit(state, scene_id)
        state["inventory"] = inv.to_list()
        state["current_scene"] = chosen["next"]
        save_load.autosave(state)


def _show_scene_header(scene: dict):
    display.print_separator()
    display.print_scene_title(scene.get("title", ""))


def _show_scene_text(scene: dict, player_name: str):
    raw = scene.get("text", "")
    text = raw.format(name=player_name) if "{name}" in raw else raw
    display.slow_print(text)


def _show_choices(choices: list, inv: Inventory, items: dict):
    display.print_separator()
    print()
    for i, choice in enumerate(choices, start=1):
        req = choice.get("requires_item")
        locked = bool(req and not inv.has(req))
        need_name = items.get(req, {}).get("name", req) if req else ""
        display.print_choice(i, choice["label"], locked=locked, need=need_name)


def _get_input(choices: list, inv: Inventory, items: dict) -> any:
    while True:
        try:
            raw = input("  > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            return "quit"

        if raw == "q":
            return "quit"
        if raw == "i":
            return "inventory"
        if raw == "m":
            return "menu"

        try:
            n = int(raw)
        except ValueError:
            display.print_error("Please enter a number from the list above.")
            continue

        if n < 1 or n > len(choices):
            display.print_error(f"Please enter a number between 1 and {len(choices)}.")
            continue

        chosen = choices[n - 1]
        req = chosen.get("requires_item")
        if req and not inv.has(req):
            item_name = items.get(req, {}).get("name", req)
            display.print_error(f"You need the {item_name} to do that!")
            continue

        return n - 1  # zero-based index


def _record_visit(state: dict, scene_id: str):
    if scene_id not in state.get("visited_scenes", []):
        state.setdefault("visited_scenes", []).append(scene_id)
