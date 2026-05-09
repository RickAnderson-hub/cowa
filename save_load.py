import json
import os
from datetime import datetime

SAVES_DIR = os.path.join(os.path.dirname(__file__), "saves")


def _ensure_saves_dir():
    os.makedirs(SAVES_DIR, exist_ok=True)


def _slot_path(slot: str) -> str:
    safe = "".join(c for c in slot if c.isalnum() or c in ("_", "-"))
    return os.path.join(SAVES_DIR, f"{safe}.json")


def list_saves() -> list[dict]:
    _ensure_saves_dir()
    saves = []
    for fname in sorted(os.listdir(SAVES_DIR)):
        if fname.endswith(".json") and not fname.startswith("autosave"):
            slot = fname[:-5]
            try:
                data = load_game(slot)
                saves.append({
                    "slot": slot,
                    "player_name": data.get("player_name", "???"),
                    "adventure_id": data.get("adventure_id", "space_explorer"),
                    "chapter": data.get("chapter", 1),
                    "save_timestamp": data.get("save_timestamp", ""),
                })
            except Exception:
                pass
    return saves


def save_game(state: dict, slot: str) -> None:
    _ensure_saves_dir()
    state["save_timestamp"] = datetime.now().isoformat(timespec="seconds")
    with open(_slot_path(slot), "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)


def load_game(slot: str) -> dict:
    path = _slot_path(slot)
    if not os.path.exists(path):
        raise FileNotFoundError(f"No save found for slot '{slot}'")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def autosave(state: dict) -> None:
    save_game(state, "autosave")


def autosave_exists() -> bool:
    return os.path.exists(_slot_path("autosave"))


def delete_save(slot: str) -> None:
    path = _slot_path(slot)
    if os.path.exists(path):
        os.remove(path)


def new_game_state(player_name: str, adventure_id: str, start_scene: str) -> dict:
    return {
        "version": 1,
        "player_name": player_name,
        "adventure_id": adventure_id,
        "current_scene": start_scene,
        "inventory": [],
        "visited_scenes": [],
        "chapter": 1,
    }
