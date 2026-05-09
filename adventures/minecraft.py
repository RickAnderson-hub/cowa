ITEMS = {
    "wooden_pickaxe": {
        "id": "wooden_pickaxe",
        "name": "Wooden Pickaxe",
        "icon": "[PICKAXE]",
        "description": "Your first tool! Good for mining stone and coal.",
    },
    "iron_sword": {
        "id": "iron_sword",
        "name": "Iron Sword",
        "icon": "[SWORD]",
        "description": "A solid iron sword. Great for fighting mobs!",
    },
    "diamond_pickaxe": {
        "id": "diamond_pickaxe",
        "name": "Diamond Pickaxe",
        "icon": "[DIAMOND]",
        "description": "The best pickaxe! The only tool that can mine obsidian.",
    },
    "obsidian": {
        "id": "obsidian",
        "name": "Obsidian",
        "icon": "[OBSIDIAN]",
        "description": "10 shiny black blocks. Perfect for building a Nether portal!",
    },
    "blaze_rod": {
        "id": "blaze_rod",
        "name": "Blaze Rod",
        "icon": "[BLAZEROD]",
        "description": "A fiery stick dropped by a Blaze. Hot to hold!",
    },
    "ender_pearls": {
        "id": "ender_pearls",
        "name": "Ender Pearls",
        "icon": "[PEARL]",
        "description": "Shimmery green pearls dropped by an Enderman.",
    },
    "eye_of_ender": {
        "id": "eye_of_ender",
        "name": "Eye of Ender",
        "icon": "[EYE]",
        "description": "Crafted from a Blaze Rod and an Ender Pearl. It points to the End Portal!",
    },
    "diamond_armor": {
        "id": "diamond_armor",
        "name": "Diamond Armor",
        "icon": "[ARMOR]",
        "description": "Full diamond protection. Almost nothing can hurt you now!",
    },
}

STORY = {

    # ──────────────────────────────────────────────────────────────────
    # CHAPTER 1 — DAY ONE
    # ──────────────────────────────────────────────────────────────────

    "mc_intro": {
        "id": "mc_intro",
        "chapter": 1,
        "chapter_title": "Day One",
        "title": "You've Spawned!",
        "text": (
            "You are {name} — and you have just spawned into a Minecraft world!\n\n"
            "Everything is made of blocks. The trees are blocky. The clouds are "
            "blocky. Even YOU are a bit blocky, honestly.\n\n"
            "Your goal? Survive, explore, and eventually — if you're brave "
            "enough — defeat the ENDER DRAGON and beat the game!\n\n"
            "But first things first. The sun is up, you have nothing in your "
            "pockets, and the night will come in about ten minutes.\n\n"
            "Time to get to work!"
        ),
        "choices": [],
        "auto_next": "mc_spawn",
        "ending": None,
    },

    "mc_spawn": {
        "id": "mc_spawn",
        "chapter": 1,
        "chapter_title": "Day One",
        "title": "Look Around!",
        "text": (
            "You're standing in a grassy plains biome. Fluffy square sheep wander "
            "nearby. There's a forest of oak trees to the east. To the west, "
            "a mountain rises up with a dark cave entrance near the bottom. "
            "In the distance you can just barely see rooftops — a village!\n\n"
            "Inventory: empty. Time until dark: a lot (but not forever).\n\n"
            "What's your first move?"
        ),
        "choices": [
            {
                "label": "Run over and punch a tree — gotta get that wood!",
                "next": "mc_punch_tree",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Head toward the village — maybe there's useful stuff there.",
                "next": "mc_village",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Head toward the mountain cave — punch a few trees on the way.",
                "next": "mc_cave_start",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_cave_start": {
        "id": "mc_cave_start",
        "chapter": 1,
        "chapter_title": "Day One",
        "title": "Mountain Bound!",
        "text": (
            "On the way to the mountain cave you bash a few oak trees and craft "
            "a quick wooden pickaxe. Sticks, planks, done.\n\n"
            "Inside the cave entrance you find coal seams right away. You pop "
            "them into a crafting bench alongside some sticks: torches! "
            "You place them on the walls one by one. The cave lights up orange "
            "and warm. It smells like stone and adventure.\n\n"
            "A bat zooms past your ear. You do not scream. (You scream a little.)\n\n"
            "The sun is getting lower outside. Better find shelter before dark!"
        ),
        "choices": [
            {
                "label": "Head back out to find shelter before dark.",
                "next": "mc_shelter_choice",
                "requires_item": None,
                "gives_item": "wooden_pickaxe",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_punch_tree": {
        "id": "mc_punch_tree",
        "chapter": 1,
        "chapter_title": "Day One",
        "title": "PUNCH THAT TREE",
        "text": (
            "You walk up to an oak tree and punch it with your fist.\n\n"
            "BONK. BONK. BONK.\n\n"
            "The tree doesn't seem to mind. After about six punches, a wood "
            "block pops out like magic. You pick it up. Repeat five more times.\n\n"
            "You now have 6 Oak Wood blocks. You open your crafting menu (the "
            "little 2x2 grid in your inventory), make planks, then sticks, "
            "then arrange them into the pickaxe shape.\n\n"
            "A beautiful, terrible, wooden pickaxe appears.\n\n"
            "'It's... it's so beautiful,' you whisper. It is not beautiful. "
            "It is made of sticks and planks. But it is YOURS."
        ),
        "choices": [
            {
                "label": "Head out and find a good spot for shelter.",
                "next": "mc_shelter_choice",
                "requires_item": None,
                "gives_item": "wooden_pickaxe",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_village": {
        "id": "mc_village",
        "chapter": 1,
        "chapter_title": "Day One",
        "title": "Village!",
        "text": (
            "You jog toward the village. It's a cozy little place — stone "
            "paths, little houses, a blacksmith forge, and about a dozen "
            "villagers waddling around making 'HMMMM' noises at each other.\n\n"
            "You poke around the houses. Most chests are empty, but in the "
            "blacksmith's chest you find treasure: a shiny iron sword! "
            "Someone left it here just for you (or you're technically stealing, "
            "but in Minecraft that's fine).\n\n"
            "A villager walks past and stares at you with a blank expression. "
            "You wave. They make the 'HMMM' noise. Close enough."
        ),
        "choices": [
            {
                "label": "Grab the sword and find shelter before dark.",
                "next": "mc_shelter_choice",
                "requires_item": None,
                "gives_item": "iron_sword",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_shelter_choice": {
        "id": "mc_shelter_choice",
        "chapter": 1,
        "chapter_title": "Day One",
        "title": "Build Shelter!",
        "text": (
            "The sun is getting lower. You can actually see it moving across "
            "the sky now. Somewhere out there, zombies and skeletons are "
            "waiting for darkness to come out and ruin your day.\n\n"
            "You need shelter — fast!\n\n"
            "The mountain has a cave entrance not far away. Or you could "
            "quickly build a small shelter right here on flat ground."
        ),
        "choices": [
            {
                "label": "Dig into the hillside and make a dirt hut — quick and safe!",
                "next": "mc_dirt_hut",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Head to that cave entrance in the mountain.",
                "next": "mc_cave_shelter",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Dig a hidey-hole straight into the mountainside — fastest option!",
                "next": "mc_hidey_hole",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_hidey_hole": {
        "id": "mc_hidey_hole",
        "chapter": 1,
        "chapter_title": "Day One",
        "title": "The Hidey-Hole",
        "text": (
            "You dig three blocks into the mountain, spin around, and place "
            "dirt blocks behind you.\n\n"
            "That's it. That's your house.\n\n"
            "No door. No windows. Barely room to turn around. "
            "Outside: zombies groaning, skeletons clattering, a Creeper going "
            "'sssss' very nearby.\n\n"
            "Inside: you, in the dark, eating a carrot.\n\n"
            "It is somehow perfect."
        ),
        "choices": [],
        "auto_next": "mc_morning",
        "ending": None,
    },

    "mc_dirt_hut": {
        "id": "mc_dirt_hut",
        "chapter": 1,
        "chapter_title": "Day One",
        "title": "Humble Home",
        "text": (
            "You dig up dirt blocks at super speed and stack them into a tiny "
            "cube hut. It's about the size of a wardrobe. There's barely room "
            "to turn around. You place a wooden door on the front.\n\n"
            "It is the ugliest building in the history of buildings.\n\n"
            "You step inside just as the sun disappears. Outside you hear "
            "shuffling, groaning, and the occasional 'CLICK CLICK CLICK' of "
            "a skeleton.\n\n"
            "Inside: safe, cozy, and absolutely beautiful (to you).\n\n"
            "You spend the night crafting by the light of a torch you made. "
            "Morning comes. Time to go underground!"
        ),
        "choices": [],
        "auto_next": "mc_morning",
        "ending": None,
    },

    "mc_cave_shelter": {
        "id": "mc_cave_shelter",
        "chapter": 1,
        "chapter_title": "Day One",
        "title": "Cave Shelter",
        "text": (
            "You run to the mountain cave and use dirt blocks to seal up the "
            "entrance just as the last light fades. The cave is dark — you "
            "quickly craft some torches from sticks and coal you find on the "
            "floor, and pop them on the walls.\n\n"
            "Outside: monsters. Inside: cozy cave. Perfect.\n\n"
            "The broken handle of an old wooden pickaxe rests against the wall — "
            "someone was here before you, once. They left in a hurry.\n\n"
            "You set up a small crafting bench and wait out the night. "
            "By morning you're ready for real mining."
        ),
        "choices": [],
        "auto_next": "mc_morning",
        "ending": None,
    },

    "mc_morning": {
        "id": "mc_morning",
        "chapter": 1,
        "chapter_title": "Day One",
        "title": "Morning!",
        "text": (
            "The sun rises. You survived your first night!\n\n"
            "A zombie outside your door slowly catches fire in the sunlight "
            "and runs around in a panic. You watch through a gap in the wall.\n\n"
            "Rude, but also: very satisfying.\n\n"
            "Time to go mining. Those diamonds aren't going to find themselves!"
        ),
        "choices": [],
        "auto_next": "mc_mine_start",
        "ending": None,
    },

    # ──────────────────────────────────────────────────────────────────
    # CHAPTER 2 — GOING UNDERGROUND
    # ──────────────────────────────────────────────────────────────────

    "mc_mine_start": {
        "id": "mc_mine_start",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "Time to Mine!",
        "text": (
            "You stand at the entrance to your mine (or the side of a hill — "
            "either way, you're going in).\n\n"
            "The question is: how?\n\n"
            "An experienced miner once said: 'Never dig straight down.' "
            "But you know what? That experienced miner isn't here right now."
        ),
        "choices": [
            {
                "label": "Dig straight down. Rules are made to be broken!",
                "next": "mc_straight_down",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Dig a proper staircase mine. Safety first.",
                "next": "mc_staircase_mine",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Head back to that mountain cave — you already know the way!",
                "next": "mc_explore_known_cave",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_explore_known_cave": {
        "id": "mc_explore_known_cave",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "Back to the Mountain Cave",
        "text": (
            "You return to the mountain cave entrance you spotted on Day One. "
            "No digging needed — it's already there! Very efficient.\n\n"
            "You head down into the darkness, torches crackling on the walls, "
            "and almost immediately the tunnel opens into a massive cave system. "
            "Bats scatter in every direction like a flying explosion of squeaks.\n\n"
            "Iron ore glitters on every wall. And from somewhere deep below: "
            "a faint blue shimmer.\n\n"
            "You've only been here five seconds and already it's incredible."
        ),
        "choices": [],
        "auto_next": "mc_cave_system",
        "ending": None,
    },

    "mc_straight_down": {
        "id": "mc_straight_down",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "Never Dig Straight Down",
        "text": (
            "You dig straight down.\n\n"
            "Block. Block. Block. Block. Block—\n\n"
            "FWOOOOSH!\n\n"
            "The block beneath you disappears and you fall TWENTY METRES into "
            "a cavern. Your heart stops.\n\n"
            "But SPLASH — you land in a small underground pool. You float there "
            "for a second, heart hammering.\n\n"
            "Slowly you look around. You're deep in a massive cave system. "
            "Iron ore glitters on the walls. Coal everywhere. And — "
            "is that a faint blue glow further down...?\n\n"
            "That was the most terrifying and lucky thing to ever happen to you."
        ),
        "choices": [
            {
                "label": "Explore this cave system!",
                "next": "mc_cave_system",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_staircase_mine": {
        "id": "mc_staircase_mine",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "Staircase Mine",
        "text": (
            "Smart! You dig a neat staircase going diagonally down into the earth. "
            "Each step goes one block forward and one block down.\n\n"
            "It's very satisfying. You are a professional.\n\n"
            "After about 30 steps you hit a cave system — a massive underground "
            "network of tunnels and caverns. Bats squeak and fly past your face. "
            "Iron ore and coal are everywhere. In the distance you see "
            "a flickering glow...\n\n"
            "Could that be... diamonds?"
        ),
        "choices": [
            {
                "label": "Explore the cave system!",
                "next": "mc_cave_system",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_cave_system": {
        "id": "mc_cave_system",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "Underground!",
        "text": (
            "You venture deeper into the cave. It's dark and echoey. "
            "Your torch casts long shadows on the stone walls.\n\n"
            "You find iron ore and smelt it into iron ingots at a quick furnace "
            "you set up. If you don't already have an iron sword, you make one now.\n\n"
            "The cave splits in two directions. To the left: you can hear "
            "a faint hissing noise. To the right: a pale blue shimmer in "
            "the stone wall.\n\n"
            "The hissing is almost certainly a creeper.\n"
            "The blue shimmer is almost certainly diamonds."
        ),
        "choices": [
            {
                "label": "Go left toward the hissing sound.",
                "next": "mc_creeper_encounter",
                "requires_item": None,
                "gives_item": "iron_sword",
            },
            {
                "label": "Go right toward the blue shimmer!",
                "next": "mc_diamond_vein",
                "requires_item": None,
                "gives_item": "iron_sword",
            },
            {
                "label": "Set up a proper mining camp here first — torches everywhere, crafting table out.",
                "next": "mc_mining_camp",
                "requires_item": None,
                "gives_item": "iron_sword",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_mining_camp": {
        "id": "mc_mining_camp",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "Base Camp Underground",
        "text": (
            "You take five minutes to be sensible. Torches on every wall — "
            "no monster is sneaking up on you in HERE. Crafting bench placed "
            "on a flat rock. You smelt your iron ore right here, eat a piece "
            "of bread, and assess the situation like a professional.\n\n"
            "While placing the last torch, you notice a third tunnel — going "
            "STRAIGHT DOWN, with an orange glow at the bottom. Lava. "
            "Which means... obsidian potential.\n\n"
            "But first: you mine all the nearby diamonds (they are RIGHT THERE "
            "and you're not walking past them). Then you follow the lava tunnel. "
            "This was an excellent plan."
        ),
        "choices": [],
        "auto_next": "mc_diamond_vein",
        "ending": None,
    },

    "mc_creeper_encounter": {
        "id": "mc_creeper_encounter",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "Ssssss...",
        "text": (
            "You round the corner and come face-to-face with a Creeper.\n\n"
            "It's green. It has a sad face. It is staring directly at you.\n\n"
            "It begins to hiss: 'Ssssssss...'\n\n"
            "That sound means it's about to EXPLODE. You have about two seconds."
        ),
        "choices": [
            {
                "label": "ATTACK IT with your iron sword!",
                "next": "mc_creeper_fight",
                "requires_item": "iron_sword",
                "gives_item": None,
            },
            {
                "label": "RUN AWAY as fast as possible!",
                "next": "mc_creeper_run",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Freeze completely still — maybe it won't notice you.",
                "next": "mc_death_creeper",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_death_creeper": {
        "id": "mc_death_creeper",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "BOOM.",
        "text": (
            "You freeze completely still.\n\n"
            "The Creeper stares at you.\n\n"
            "You stare at the Creeper.\n\n"
            "It is still hissing. 'Sssssssss...'\n\n"
            "That means it is ALREADY EXPLODING. Freezing doesn't stop the "
            "explosion. Freezing is for statues, not for Creepers. "
            "These are very different situations.\n\n"
            "BOOOOOOM.\n\n"
            "You respawn at your bed, blinking in the morning light.\n\n"
            "Your inventory is empty. The cave is rubble.\n\n"
            "On the bright side: now you know what NOT to do.\n\n"
            "Never freeze near a hissing Creeper. Run or fight — never freeze."
        ),
        "choices": [],
        "auto_next": None,
        "ending": "lose",
        "lose_reason": "Creepers don't care if you stand still. Run away or fight!",
    },

    "mc_creeper_fight": {
        "id": "mc_creeper_fight",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "FIGHT!",
        "text": (
            "You swing your iron sword!\n\n"
            "CLANG! CLANG! The creeper takes hits and flashes red. "
            "It tries to hiss again but you hit it a third time and—\n\n"
            "POP! It dies. No explosion. Just gone, leaving behind a small "
            "pile of... gunpowder?\n\n"
            "You collect it. Apparently creepers are mostly just compressed "
            "gunpowder shaped like a sad green tube. Good to know.\n\n"
            "Heart still pounding, you remember: diamonds. Right. That blue glow."
        ),
        "choices": [
            {
                "label": "Head for the blue shimmer!",
                "next": "mc_diamond_vein",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_creeper_run": {
        "id": "mc_creeper_run",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "RUUUUN!",
        "text": (
            "You spin around and sprint.\n\n"
            "BOOOOOM!\n\n"
            "The explosion knocks you forward. The tunnel behind you is now a "
            "small crater. Your ears are ringing. Your health bar has taken "
            "a serious hit. But you are alive.\n\n"
            "You look down at your hands. Still attached. Great.\n\n"
            "You eat a piece of bread from your pocket (always carry bread) "
            "and your health slowly fills back up. Lesson learned?\n\n"
            "Maybe. But there are still diamonds to find."
        ),
        "choices": [
            {
                "label": "Cautiously head for that blue shimmer.",
                "next": "mc_diamond_vein",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_diamond_vein": {
        "id": "mc_diamond_vein",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "DIAMONDS!!!",
        "text": (
            "There they are.\n\n"
            "Eight diamond ore blocks, glittering brilliant blue in the torchlight. "
            "The most beautiful thing you have ever seen in your entire life.\n\n"
            "With your wooden or iron pickaxe you can chip away at them, but "
            "they'll drop regular diamonds (which is still great!). "
            "You mine each one carefully.\n\n"
            "At your crafting bench you arrange three diamonds across the top, "
            "two sticks underneath. A Diamond Pickaxe appears. It is glorious. "
            "It shines. It hums faintly. A nearby bat flies over to look at it."
        ),
        "choices": [
            {
                "label": "Look for obsidian — you'll need it for a Nether portal!",
                "next": "mc_lava_pool",
                "requires_item": None,
                "gives_item": "diamond_pickaxe",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_lava_pool": {
        "id": "mc_lava_pool",
        "chapter": 2,
        "chapter_title": "Going Underground",
        "title": "Lava!",
        "text": (
            "Deeper in the cave you find what you were looking for: a pool of "
            "lava, glowing orange and bubbling. Next to it, a small waterfall "
            "trickles down from the ceiling.\n\n"
            "Where water meets lava: obsidian. Black, shiny, incredibly hard.\n\n"
            "You carefully redirect the water using a bucket (you improvised "
            "one from iron ingots). The water flows over the lava and — "
            "HISS — black obsidian blocks form, one by one.\n\n"
            "You mine them with your Diamond Pickaxe. ONLY a diamond pickaxe "
            "can do this. It takes a while — obsidian is TOUGH — but you "
            "chip out 10 blocks."
        ),
        "choices": [
            {
                "label": "Head back to the surface with all this loot!",
                "next": "mc_surface_return",
                "requires_item": None,
                "gives_item": "obsidian",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    # ──────────────────────────────────────────────────────────────────
    # CHAPTER 3 — THE NETHER
    # ──────────────────────────────────────────────────────────────────

    "mc_surface_return": {
        "id": "mc_surface_return",
        "chapter": 3,
        "chapter_title": "The Nether",
        "title": "Back on the Surface",
        "text": (
            "You emerge from the mine blinking in the sunlight. Your inventory "
            "is absolutely packed. Diamonds! Iron! Obsidian! Coal!\n\n"
            "You make yourself a proper base — a wooden house, a bed, "
            "a furnace, and some storage chests. You even put a flower "
            "in a pot by the door. Very cozy.\n\n"
            "But cozy isn't going to defeat the Ender Dragon. "
            "For that, you need to go somewhere far worse than a dark cave.\n\n"
            "You need to go to THE NETHER."
        ),
        "choices": [
            {
                "label": "Build the Nether portal using your obsidian!",
                "next": "mc_portal_built",
                "requires_item": "obsidian",
                "gives_item": None,
            },
            {
                "label": "You have no obsidian — look for a ruined portal nearby.",
                "next": "mc_ruined_portal",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Craft Diamond Armor before going anywhere near the Nether.",
                "next": "mc_craft_armor",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_craft_armor": {
        "id": "mc_craft_armor",
        "chapter": 3,
        "chapter_title": "The Nether",
        "title": "Diamond Armor!",
        "text": (
            "You've got diamonds and you are NOT an idiot.\n\n"
            "You spend an hour at your crafting table making a full diamond "
            "chestplate, leggings, boots, and helmet. Each piece clicks together "
            "perfectly. You put it on.\n\n"
            "You look INCREDIBLE.\n\n"
            "You are basically indestructible. The flower by your door sways "
            "in the breeze, as if impressed.\n\n"
            "Now THAT is how you prepare for another dimension."
        ),
        "choices": [
            {
                "label": "Now build that Nether portal!",
                "next": "mc_portal_built",
                "requires_item": None,
                "gives_item": "diamond_armor",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_ruined_portal": {
        "id": "mc_ruined_portal",
        "chapter": 3,
        "chapter_title": "The Nether",
        "title": "Ruined Portal",
        "text": (
            "You explore the area and discover a ruined Nether portal — "
            "a crumbling stone arch with a few obsidian blocks already "
            "in place. Some of the blocks are missing, but there's a "
            "chest nearby with crying obsidian and some regular obsidian.\n\n"
            "You patch up the gaps using the obsidian from the chest. "
            "It's a bit wobbly-looking, but structurally sound.\n\n"
            "Now to light it. You find some flint on the ground and bang "
            "it against an iron ingot: SPARK! The portal ignites with "
            "a purple swirling glow.\n\n"
            "Here we go."
        ),
        "choices": [
            {
                "label": "Step into the portal!",
                "next": "mc_nether_arrive",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_portal_built": {
        "id": "mc_portal_built",
        "chapter": 3,
        "chapter_title": "The Nether",
        "title": "Portal Built!",
        "text": (
            "You place the obsidian blocks in a rectangle — four wide, "
            "five tall. Then you grab some flint and steel (iron ingot + "
            "flint from the ground), click the lighter inside the frame and—\n\n"
            "WHOOOOSH!\n\n"
            "Purple fire erupts inside the frame. Swirling violet light fills "
            "the portal. It makes a low humming sound that you feel in your chest.\n\n"
            "This is a door to another dimension. You built it yourself. "
            "From blocks.\n\n"
            "Minecraft is incredible."
        ),
        "choices": [
            {
                "label": "Take a deep breath and step through.",
                "next": "mc_nether_arrive",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_nether_arrive": {
        "id": "mc_nether_arrive",
        "chapter": 3,
        "chapter_title": "The Nether",
        "title": "Welcome to the Nether",
        "text": (
            "You step through.\n\n"
            "The world on the other side is RED. The ceiling is far above you. "
            "Everything is made of netherrack — a dark red crumbly stone. "
            "Lava waterfalls pour down the walls. The sky glows orange.\n\n"
            "It is very, very hot. It smells like burnt toast.\n\n"
            "Zombie Pigmen waddle past you, ignoring you completely. "
            "A ghast — a giant floating white jelly cube — cries somewhere "
            "in the distance. Somewhere far off, there is a FORTRESS. "
            "You can just make out its dark walls through the fog."
        ),
        "choices": [
            {
                "label": "Head toward the Nether Fortress.",
                "next": "mc_piglins",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_piglins": {
        "id": "mc_piglins",
        "chapter": 3,
        "chapter_title": "The Nether",
        "title": "Piglins!",
        "text": (
            "On the path to the fortress you encounter a group of Piglins — "
            "pig-headed warriors in gold armour. They're blocking the path.\n\n"
            "One of them spots you and raises their crossbow.\n\n"
            "Then it spots something shiny in your hand — you accidentally "
            "had a gold ingot from your mining earlier. The Piglin's eyes "
            "light up. They LOVE gold.\n\n"
            "You hold it out. The Piglin snatches it and tosses something back "
            "at you: a fire resistance potion. They grunt and step aside.\n\n"
            "That potion means lava can't hurt you for a while. Very useful "
            "in a dimension made mostly of lava."
        ),
        "choices": [
            {
                "label": "Continue to the Nether Fortress!",
                "next": "mc_fortress_entrance",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_fortress_entrance": {
        "id": "mc_fortress_entrance",
        "chapter": 3,
        "chapter_title": "The Nether",
        "title": "Nether Fortress!",
        "text": (
            "The Nether Fortress is enormous — dark stone walkways and "
            "bridges stretching in every direction above lakes of lava. "
            "It's ancient and crumbling and honestly quite impressive.\n\n"
            "Inside, you can see Blazes — spinning fire creatures with "
            "yellow cores, floating in the air, shooting balls of flame.\n\n"
            "You need a Blaze Rod from one of them. They won't give it up "
            "without a fight.\n\n"
            "There might be another way — but it won't be easy."
        ),
        "choices": [
            {
                "label": "Fight the Blazes with your iron sword!",
                "next": "mc_blaze_fight",
                "requires_item": "iron_sword",
                "gives_item": None,
            },
            {
                "label": "Try to sneak through and find a Blaze Rod in a chest.",
                "next": "mc_blaze_sneak",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Put on your Diamond Armor and just walk straight through — take the hits!",
                "next": "mc_blaze_tank",
                "requires_item": "diamond_armor",
                "gives_item": "blaze_rod",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_blaze_tank": {
        "id": "mc_blaze_tank",
        "chapter": 3,
        "chapter_title": "The Nether",
        "title": "Basically Indestructible",
        "text": (
            "You stride into the fortress like you own the place.\n\n"
            "A Blaze fires a fireball directly at your chest. "
            "CLANG — it bounces off your diamond chestplate. "
            "The Blaze looks confused.\n\n"
            "Another fireball. CLANG.\n\n"
            "You walk calmly forward, collect the Blaze Rod right out of "
            "the Blaze's spinning hands (basically), and keep walking. "
            "Three Blazes try to stop you. None succeed.\n\n"
            "The fortress falls silent as you exit.\n\n"
            "Diamond armor was absolutely worth it."
        ),
        "choices": [],
        "auto_next": "mc_nether_exit",
        "ending": None,
    },

    "mc_blaze_fight": {
        "id": "mc_blaze_fight",
        "chapter": 3,
        "chapter_title": "The Nether",
        "title": "Blaze Battle!",
        "text": (
            "You charge into the fortress!\n\n"
            "A Blaze fires a trio of fireballs at you. You dodge left — "
            "one misses, one singes your sleeve. You charge forward and "
            "swing your sword!\n\n"
            "CLANG! The Blaze spins and rattles. You hit it twice more. "
            "It explodes into flame and drops — a single glowing Blaze Rod.\n\n"
            "You grab it. It's HOT. Like, genuinely hot. You hold it with "
            "the very tips of your fingers.\n\n"
            "A second Blaze comes around the corner. You defeat that one too. "
            "You are getting frighteningly good at this."
        ),
        "choices": [
            {
                "label": "Get out of the Nether and go find some Endermen.",
                "next": "mc_nether_exit",
                "requires_item": None,
                "gives_item": "blaze_rod",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_blaze_sneak": {
        "id": "mc_blaze_sneak",
        "chapter": 3,
        "chapter_title": "The Nether",
        "title": "The Sneaky Route",
        "text": (
            "You creep along the walls, staying out of the Blazes' line of sight.\n\n"
            "Past one. Past two. You hold your breath around a corner "
            "as a Blaze drifts by, close enough to feel the heat.\n\n"
            "In a chest near the back of the fortress you find some "
            "Nether items, but no Blaze Rod. You'll have to find another way "
            "to get to the End.\n\n"
            "For now though — you made it through. Let's get back to the overworld."
        ),
        "choices": [
            {
                "label": "Head back through the Nether portal.",
                "next": "mc_nether_exit",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_nether_exit": {
        "id": "mc_nether_exit",
        "chapter": 3,
        "chapter_title": "The Nether",
        "title": "Back to the Overworld",
        "text": (
            "You step back through the portal.\n\n"
            "WHOOOOSH — and you're home. Green grass, blue sky, square clouds.\n\n"
            "You breathe deeply. Normal air. Air that doesn't smell like burnt toast.\n\n"
            "Now: Endermen. You need their Ender Pearls to craft Eyes of Ender, "
            "which you'll need to find the End Portal.\n\n"
            "Endermen come out at night. Night falls very soon.\n\n"
            "How convenient."
        ),
        "choices": [],
        "auto_next": "mc_enderman_hunt",
        "ending": None,
    },

    # ──────────────────────────────────────────────────────────────────
    # CHAPTER 4 — THE END
    # ──────────────────────────────────────────────────────────────────

    "mc_enderman_hunt": {
        "id": "mc_enderman_hunt",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "Enderman Hunt",
        "text": (
            "Night falls. Tall, thin, dark figures appear across the plains — "
            "Endermen. They're three blocks tall with long legs and glowing "
            "purple eyes. They teleport around making eerie 'WUUUU' sounds.\n\n"
            "Endermen are usually peaceful — UNLESS you look directly at them. "
            "Then they get very upset.\n\n"
            "You need their Ender Pearls. You're going to have to fight one.\n\n"
            "You put on your iron sword and approach carefully."
        ),
        "choices": [
            {
                "label": "Look it directly in the eyes — start the fight!",
                "next": "mc_enderman_fight",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Attack it without looking at its eyes — sneak up!",
                "next": "mc_enderman_sneak_attack",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Stare it down — a staring contest. Refuse to blink.",
                "next": "mc_death_enderman",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_death_enderman": {
        "id": "mc_death_enderman",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "The Staring Contest You Could Not Win.",
        "text": (
            "You look the Enderman directly in its glowing purple eyes.\n\n"
            "The Enderman looks at you.\n\n"
            "You do not blink.\n\n"
            "The Enderman SHRIEKS. It teleports directly on top of you. "
            "It hits you once. You fly backwards. It teleports behind you "
            "and hits you again. It teleports above you and hits you a third time.\n\n"
            "In the time it takes you to swing your sword once, the Enderman "
            "has already teleported eleven times.\n\n"
            "You did not blink.\n\n"
            "But you did die.\n\n"
            "You respawn at your base. The Enderman has vanished into the night, "
            "probably very pleased with itself.\n\n"
            "Next time: attack without looking at its eyes. Sneak attacks work much better."
        ),
        "choices": [],
        "auto_next": None,
        "ending": "lose",
        "lose_reason": "Endermen get very angry when you stare at them. Sneak attack instead!",
    },

    "mc_enderman_fight": {
        "id": "mc_enderman_fight",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "Enderman Battle!",
        "text": (
            "The Enderman SHRIEKS — a horrible high-pitched scream — and "
            "teleports directly in front of you!\n\n"
            "It swings its long arms. You duck and slash with your sword. "
            "It teleports away. You look around — it teleports back behind you!\n\n"
            "You spin and hit it twice. It teleports into a pond nearby "
            "(Endermen HATE water). You chase it to the edge and attack.\n\n"
            "The Enderman lets out one final screech and vanishes. "
            "In its place: three shimmery green Ender Pearls.\n\n"
            "You pick them up carefully. They feel weird — like holding "
            "a bubble that hasn't popped yet."
        ),
        "choices": [
            {
                "label": "Craft Eyes of Ender if you have a Blaze Rod!",
                "next": "mc_craft_eyes",
                "requires_item": "blaze_rod",
                "gives_item": "ender_pearls",
            },
            {
                "label": "Search for the stronghold — there might be Eyes in a chest!",
                "next": "mc_stronghold_search",
                "requires_item": None,
                "gives_item": "ender_pearls",
            },
            {
                "label": "Hunt a few more Endermen — the more pearls the better!",
                "next": "mc_more_pearls",
                "requires_item": None,
                "gives_item": "ender_pearls",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_more_pearls": {
        "id": "mc_more_pearls",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "Pearl Collector",
        "text": (
            "You spend the rest of the night fighting Endermen. "
            "By morning you have nine Ender Pearls and a begrudging respect "
            "for teleporting monsters.\n\n"
            "On the way back through a village, a librarian villager waves at "
            "you from their doorstep and holds up something green and swirling "
            "— an Eye of Ender! Apparently they trade these. You hand over "
            "some emeralds you found underground.\n\n"
            "The librarian nods. Deal done. The villager makes the 'HMMM' noise "
            "and goes back inside.\n\n"
            "You now have more Ender Pearls than you will ever need. Excellent."
        ),
        "choices": [
            {
                "label": "Now find the stronghold!",
                "next": "mc_stronghold_search",
                "requires_item": None,
                "gives_item": "eye_of_ender",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_enderman_sneak_attack": {
        "id": "mc_enderman_sneak_attack",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "Sneak Attack!",
        "text": (
            "You circle around slowly, keeping your eyes slightly to the side. "
            "Just close enough. Just close enough...\n\n"
            "You LUNGE and hit the Enderman from behind!\n\n"
            "It shrieks and teleports away. You look around wildly. "
            "It appears on your right. You hit it again. Teleport. Again. Hit. "
            "This goes on for a while. It's like fighting a very tall, angry ghost.\n\n"
            "Eventually it falls, leaving three Ender Pearls behind.\n\n"
            "'YESSS!' you say, to no one in particular."
        ),
        "choices": [
            {
                "label": "Craft Eyes of Ender if you have a Blaze Rod!",
                "next": "mc_craft_eyes",
                "requires_item": "blaze_rod",
                "gives_item": "ender_pearls",
            },
            {
                "label": "Search for the stronghold — maybe Eyes are in a chest.",
                "next": "mc_stronghold_search",
                "requires_item": None,
                "gives_item": "ender_pearls",
            },
            {
                "label": "Hunt a few more Endermen — the more pearls the better!",
                "next": "mc_more_pearls",
                "requires_item": None,
                "gives_item": "ender_pearls",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_craft_eyes": {
        "id": "mc_craft_eyes",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "Eyes of Ender!",
        "text": (
            "You open your crafting table and place a Blaze Rod in the "
            "centre, with an Ender Pearl on top.\n\n"
            "A swirling green eye appears.\n\n"
            "Eye of Ender: crafted.\n\n"
            "You make several. Now all you have to do is throw one in the air — "
            "it will fly in the direction of the nearest End Portal, then "
            "fall to the ground for you to pick up.\n\n"
            "It's basically a living compass. Except it looks like an eyeball. "
            "An eyeball that flies."
        ),
        "choices": [
            {
                "label": "Throw the Eye of Ender and follow it!",
                "next": "mc_stronghold_search",
                "requires_item": None,
                "gives_item": "eye_of_ender",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_stronghold_search": {
        "id": "mc_stronghold_search",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "Following the Eye",
        "text": (
            "You throw an Eye of Ender into the sky.\n\n"
            "It soars upward... slows... and drifts to the northeast. "
            "You run after it, pick it up where it lands, and throw it again.\n\n"
            "Again and again, tracking across hills and rivers, until finally "
            "it starts pointing STRAIGHT DOWN.\n\n"
            "You dig.\n\n"
            "After about fifteen blocks, your pickaxe breaks into stone brick — "
            "STRONGHOLD stone. You've found it. You're in.\n\n"
            "And somewhere deep inside this labyrinth is a portal to The End."
        ),
        "choices": [
            {
                "label": "Navigate through the stronghold.",
                "next": "mc_stronghold_enter",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_stronghold_enter": {
        "id": "mc_stronghold_enter",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "The Stronghold",
        "text": (
            "The stronghold is a maze of stone-brick corridors, staircases, "
            "libraries with floating bookshelves, and prison cells. "
            "Silverfish lurk in the walls — little stone-grey bugs that burst "
            "out if you mine the wrong block.\n\n"
            "In one room, a chest contains diamond leggings and boots. "
            "You put them on over your existing armor. Diamond protection!\n\n"
            "You follow the Eye of Ender deeper and deeper into the labyrinth, "
            "until you find a door marked by a strange symbol.\n\n"
            "Behind it: the End Portal room."
        ),
        "choices": [
            {
                "label": "Enter the End Portal room!",
                "next": "mc_end_portal_room",
                "requires_item": None,
                "gives_item": "diamond_armor",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_end_portal_room": {
        "id": "mc_end_portal_room",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "The End Portal!",
        "text": (
            "The room is circular. In the centre, a ring of End Portal frames "
            "sits around a pit of absolute blackness. Twelve frames, each "
            "needing an Eye of Ender to activate.\n\n"
            "Three frames already have Eyes in them. You have enough for the rest.\n\n"
            "One by one, you place an Eye of Ender into each empty frame. "
            "They click into place. The room hums. The portal begins to fill "
            "with a swirling darkness that looks like space.\n\n"
            "The last Eye goes in.\n\n"
            "The portal ACTIVATES. The darkness churns. From far below, "
            "you hear a distant, unearthly roar.\n\n"
            "The Ender Dragon knows you're coming."
        ),
        "choices": [
            {
                "label": "Jump in. LET'S DO THIS.",
                "next": "mc_end_arrive",
                "requires_item": "eye_of_ender",
                "gives_item": None,
            },
            {
                "label": "Jump in. (Found spare Eyes in a stronghold chest.)",
                "next": "mc_end_arrive",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Take one moment to check your gear — then jump!",
                "next": "mc_portal_prep",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_portal_prep": {
        "id": "mc_portal_prep",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "Gear Check",
        "text": (
            "You look at the swirling darkness of the portal.\n\n"
            "You check your sword. Sharpened. Your armor. Solid. "
            "Your diamond pickaxe. Ready. You eat a golden apple you've been "
            "saving since you found it in a stronghold chest — now is "
            "DEFINITELY the time. Your health fills completely.\n\n"
            "The portal hums. The Dragon is waiting. "
            "The darkness churns like it knows you're coming.\n\n"
            "You've never been more ready."
        ),
        "choices": [],
        "auto_next": "mc_end_arrive",
        "ending": None,
    },

    "mc_end_arrive": {
        "id": "mc_end_arrive",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "The End",
        "text": (
            "You fall through the portal.\n\n"
            "You land on a pale yellow-grey island floating in infinite darkness. "
            "There are no stars here. Just black. The island is covered in "
            "obsidian pillars, each topped with an End Crystal that glows "
            "bright white.\n\n"
            "And above you — the ENDER DRAGON.\n\n"
            "It's massive. Purple and black, with glowing purple eyes, "
            "swooping through the air above the island. Each End Crystal "
            "it flies over heals it back to full health.\n\n"
            "You know what you have to do."
        ),
        "choices": [
            {
                "label": "Climb the obsidian pillars and destroy the End Crystals first!",
                "next": "mc_destroy_crystals",
                "requires_item": "diamond_pickaxe",
                "gives_item": None,
            },
            {
                "label": "Charge straight at the dragon — no time for strategy!",
                "next": "mc_charge_dragon",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Grab your bow — shoot the End Crystals from the ground!",
                "next": "mc_arrow_crystals",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_arrow_crystals": {
        "id": "mc_arrow_crystals",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "Bow vs. Crystals",
        "text": (
            "You found a bow and arrows in the stronghold. Smart thinking.\n\n"
            "Instead of climbing the obsidian pillars (terrifying, windy, "
            "very tall), you aim your bow at the nearest End Crystal and let fly.\n\n"
            "TWANG — first crystal explodes in a burst of white. "
            "The Dragon shrieks. TWANG — second crystal. TWANG — third.\n\n"
            "The Endermen on the island watch you in bewildered silence, "
            "like they've never seen anything so efficient.\n\n"
            "Twelve shots. Twelve explosions. The Dragon circles without "
            "healing now. There's nothing between you and it.\n\n"
            "You lower your bow and draw your sword."
        ),
        "choices": [
            {
                "label": "Face the Dragon!",
                "next": "mc_dragon_fight",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_destroy_crystals": {
        "id": "mc_destroy_crystals",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "Smashing Crystals!",
        "text": (
            "You climb the first obsidian pillar using dirt blocks as steps. "
            "The Dragon swoops at you — you dodge and reach the top.\n\n"
            "SMASH! Your Diamond Pickaxe hits the End Crystal. It EXPLODES "
            "in a burst of white light! You fly off the pillar and land hard "
            "but alive.\n\n"
            "SMASH! Second crystal. Third. Fourth. The Dragon shrieks with "
            "each one. You can see its health bar in the corner of your vision "
            "stop regenerating.\n\n"
            "The last crystal breaks.\n\n"
            "The Dragon has no more healing. It swoops down toward you "
            "for one final attack. You plant your feet and raise your sword."
        ),
        "choices": [
            {
                "label": "Face the Dragon!",
                "next": "mc_dragon_fight",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_charge_dragon": {
        "id": "mc_charge_dragon",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "CHARGE!",
        "text": (
            "You sprint toward the centre of the island, waving your sword "
            "and screaming. The Dragon breathes a stream of purple dragon "
            "breath at you — you roll sideways and it misses.\n\n"
            "The Dragon swoops low. You slash its wing with your sword. "
            "ROAR! It banks upward, loops around, swoops again.\n\n"
            "This is harder without destroying the crystals first — it keeps "
            "healing — but you are absolutely NOT giving up. You are relentless.\n\n"
            "Slowly, very slowly, the Dragon's health drops.\n\n"
            "Finally it swoops down to perch on the central pillar. "
            "This is your chance!"
        ),
        "choices": [
            {
                "label": "FINISH IT!",
                "next": "mc_dragon_fight",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_dragon_fight": {
        "id": "mc_dragon_fight",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "FINAL BATTLE!",
        "text": (
            "The Ender Dragon perches on the central End Stone pillar, "
            "its wings spread wide, roaring.\n\n"
            "You SPRINT toward it.\n\n"
            "Sword swing! CLANG! The Dragon roars. Purple energy gathers around it. "
            "It launches into the air again. You charge after it, shooting arrows, "
            "slashing whenever it comes close.\n\n"
            "Your health drops. You eat an apple. You press on.\n\n"
            "The Dragon swoops down one final time.\n\n"
            "You leap forward and hit it with every last bit of strength you have.\n\n"
            "There is a moment of silence.\n\n"
            "Then — light. Brilliant white light. The Dragon explodes into "
            "thousands of glittering particles that spiral upward and vanish.\n\n"
            "An enormous fountain of XP bubbles pours from the sky.\n\n"
            "And from the ground — a pillar of light opens. The End Poem begins. "
            "The credits roll."
        ),
        "choices": [
            {
                "label": "You did it. You beat Minecraft.",
                "next": "mc_ending_win",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "mc_ending_win": {
        "id": "mc_ending_win",
        "chapter": 4,
        "chapter_title": "The End",
        "title": "YOU BEAT MINECRAFT!",
        "text": (
            "The exit portal opens at the centre of the island.\n\n"
            "You step through.\n\n"
            "You appear back in your cozy base — the little wooden house with "
            "the flower by the door. Your bed. Your chests full of treasure. "
            "The crafting table where this whole adventure started.\n\n"
            "You walk outside. The sun is setting. Square clouds drift past. "
            "Somewhere in the distance, a cow moos.\n\n"
            "You punched a tree. You survived your first night. "
            "You mined diamonds, crossed the Nether, found the stronghold, "
            "and defeated the Ender Dragon.\n\n"
            "You beat Minecraft.\n\n"
            "THE END\n\n"
            "~ ~ ~ ~ ~ ~\n\n"
            "Thanks for playing, {name}!"
        ),
        "choices": [],
        "auto_next": None,
        "ending": "win",
    },
}
