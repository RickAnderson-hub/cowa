from adventures.space_explorer import STORY as _SE_STORY, ITEMS as _SE_ITEMS
from adventures.minecraft import STORY as _MC_STORY, ITEMS as _MC_ITEMS

ADVENTURES = {
    "space_explorer": {
        "id": "space_explorer",
        "title": "Space Explorer",
        "description": "Blast off to a distant planet and make alien friends!",
        "start_scene": "ch1_intro",
        "story": _SE_STORY,
        "items": _SE_ITEMS,
    },
    "minecraft": {
        "id": "minecraft",
        "title": "Minecraft Adventure",
        "description": "Mine, craft, brave the Nether, and defeat the Ender Dragon!",
        "start_scene": "mc_intro",
        "story": _MC_STORY,
        "items": _MC_ITEMS,
    },
}
