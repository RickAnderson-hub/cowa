ITEMS = {
    "mission_map": {
        "id": "mission_map",
        "name": "Mission Map",
        "icon": "[MAP]",
        "description": "A star chart showing the route to Planet Zorbax.",
    },
    "stun_blaster": {
        "id": "stun_blaster",
        "name": "Stun Blaster",
        "icon": "[BLASTER]",
        "description": "Shoots a harmless blue beam. Aliens REALLY don't like it!",
    },
    "alien_candy": {
        "id": "alien_candy",
        "name": "Alien Candy",
        "icon": "[CANDY]",
        "description": "Smells like strawberries and looks like purple rocks.",
    },
    "space_suit_patch": {
        "id": "space_suit_patch",
        "name": "Space Suit Patch",
        "icon": "[PATCH]",
        "description": "A sticky patch that fixes holes in space suits.",
    },
    "jetpack": {
        "id": "jetpack",
        "name": "Jetpack",
        "icon": "[JETPACK]",
        "description": "A tiny rocket you strap to your back. Whoooosh!",
    },
    "crystal_key": {
        "id": "crystal_key",
        "name": "Crystal Key",
        "icon": "[KEY]",
        "description": "A glowing blue crystal that fits special alien locks.",
    },
    "robot_friend": {
        "id": "robot_friend",
        "name": "Robot Friend",
        "icon": "[ROBOT]",
        "description": "A small helper robot who says 'BEEP BOOP' a lot.",
    },
    "star_badge": {
        "id": "star_badge",
        "name": "Star Badge",
        "icon": "[BADGE]",
        "description": "A shiny badge that proves you are a true Space Explorer.",
    },
}

STORY = {

    # ──────────────────────────────────────────────────────────────────
    # CHAPTER 1 — BLAST OFF!
    # ──────────────────────────────────────────────────────────────────

    "ch1_intro": {
        "id": "ch1_intro",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "Welcome, Space Explorer!",
        "text": (
            "You are {name}, the bravest cadet at the Galactic Space Academy!\n\n"
            "Today is the most exciting day of your life. A mysterious signal has been "
            "detected from Planet Zorbax — a planet no human has ever visited. "
            "The Academy has chosen YOU for the mission!\n\n"
            "Your spaceship, the Shooting Star, is fueled up and ready. "
            "Mission Control is counting on you. The galaxy is counting on you!\n\n"
            "Are you ready? Your adventure begins NOW!"
        ),
        "choices": [
            {
                "label": "Head to the Launch Pad!",
                "next": "ch1_launch_pad",
                "requires_item": None,
                "gives_item": None,
            }
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch1_launch_pad": {
        "id": "ch1_launch_pad",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "The Launch Pad",
        "text": (
            "The Shooting Star gleams in the morning sunlight. It's silver and "
            "blue with a big star painted on the side. Steam hisses from the "
            "engines. The countdown clock reads T-minus 10 minutes!\n\n"
            "Hanging by the hatch is your space suit — and clipped to it, "
            "a Space Suit Patch kit. Standard issue for every mission. "
            "Next to it is a black briefcase labeled 'MISSION BRIEFING — TOP SECRET'.\n\n"
            "You grab the patch kit and clip it to your belt. You'll want that "
            "if anything goes wrong out there.\n\n"
            "What do you do next?"
        ),
        "choices": [
            {
                "label": "Climb straight into the rocket — no time to waste!",
                "next": "ch1_inside_rocket",
                "requires_item": None,
                "gives_item": "space_suit_patch",
            },
            {
                "label": "Check the mission briefcase first.",
                "next": "ch1_briefcase",
                "requires_item": None,
                "gives_item": "space_suit_patch",
            },
            {
                "label": "Chat with the launch technician — ask if the ship is ready.",
                "next": "ch1_launch_chat",
                "requires_item": None,
                "gives_item": "space_suit_patch",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch1_launch_chat": {
        "id": "ch1_launch_chat",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "A Word with the Technician",
        "text": (
            "The launch technician turns around. He has a clipboard, a hard hat "
            "slightly too big for his head, and the expression of someone who "
            "has not slept in several days.\n\n"
            "'Is the ship ready?' you ask.\n\n"
            "He looks at the clipboard. Then at the ship. Then at the clipboard again.\n\n"
            "'Okay so,' he says, 'the main engines are DEFINITELY fine. "
            "The fuel gauge is... probably accurate. The autopilot has some "
            "quirks but nothing major. And that rattling noise? Classic. "
            "Classic rocket noise. Very normal. Nothing to worry about.'\n\n"
            "He pats you firmly on the shoulder.\n\n"
            "'You are going to be GREAT. Probably. We believe in you. "
            "I believe in you. The whole team believes in you. "
            "Now please get in the rocket before I think about it too hard.'\n\n"
            "Somehow, you feel completely ready."
        ),
        "choices": [],
        "auto_next": "ch1_inside_rocket",
        "ending": None,
    },

    "ch1_briefcase": {
        "id": "ch1_briefcase",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "Top Secret!",
        "text": (
            "You snap open the briefcase. Inside is a glowing star chart — "
            "a map of the entire galaxy with a route to Planet Zorbax marked "
            "in bright red. There's a note attached:\n\n"
            "'Good luck, Explorer. This map will show you the way when you are "
            "lost among the stars. — Mission Control'\n\n"
            "You fold the map carefully and tuck it inside your space suit. "
            "Now THAT could come in handy!"
        ),
        "choices": [
            {
                "label": "Climb into the rocket!",
                "next": "ch1_inside_rocket",
                "requires_item": None,
                "gives_item": "mission_map",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch1_inside_rocket": {
        "id": "ch1_inside_rocket",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "Inside the Shooting Star",
        "text": (
            "You strap yourself into the pilot's seat. Hundreds of buttons and "
            "flashing lights surround you. A big red lever is labeled 'LAUNCH'.\n\n"
            "Mission Control crackles over the radio:\n\n"
            "'T-minus 60 seconds, Explorer. All systems... wait. Hold on. "
            "We're picking up something strange. One of your engines is making "
            "a very weird noise. It sounds like... a cat purring? No wait, "
            "that's definitely NOT normal.'\n\n"
            "Sure enough, you hear it — a low, rattling CLUNK from beneath you."
        ),
        "choices": [
            {
                "label": "Put on your space suit and go check the engine yourself.",
                "next": "ch1_fix_engine",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Ask Mission Control what to do.",
                "next": "ch1_call_control",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Just pull the launch lever — that noise is DEFINITELY fine.",
                "next": "ch1_reckless_launch",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch1_reckless_launch": {
        "id": "ch1_reckless_launch",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "That Was Not Fine.",
        "text": (
            "You grab the big red lever labeled LAUNCH and YANK.\n\n"
            "For a moment, nothing happens.\n\n"
            "Then the weird engine noise goes from 'concerning' to 'ALARMING' "
            "to 'EXTREMELY NOT GOOD' in about two seconds. "
            "The whole rocket starts to shake. Then rattle. "
            "Then shake AND rattle simultaneously.\n\n"
            "Mission Control: 'Explorer, we're picking up some unusual "
            "engine readings—'\n\n"
            "BANG.\n\n"
            "Not a small bang. A VERY LARGE BANG.\n\n"
            "The Shooting Star tips sideways off the launch pad. "
            "Very slowly. In complete silence.\n\n"
            "It lands with an enormous crash. Steam everywhere. "
            "Somewhere, an alarm is going off very sadly.\n\n"
            "Mission Control says nothing for a very long time.\n\n"
            "Then, quietly: '...We may need to reschedule the mission.'"
        ),
        "choices": [],
        "auto_next": None,
        "ending": "lose",
        "lose_reason": "Always check your engine before launching!",
    },

    "ch1_call_control": {
        "id": "ch1_call_control",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "Mission Control",
        "text": (
            "You radio Mission Control. There is a very long pause.\n\n"
            "'Uhhhh...' says the Mission Control scientist.\n"
            "'Hmmmm...' says another one.\n"
            "'We're going to be honest with you,' they finally say. 'None of "
            "us have ever heard an engine make THAT sound before. You're going "
            "to have to go check it yourself. Sorry!'\n\n"
            "They hang up. Helpful.\n\n"
            "You'll have to check that engine yourself after all."
        ),
        "choices": [
            {
                "label": "Fine! Put on the space suit and check the engine.",
                "next": "ch1_fix_engine",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch1_fix_engine": {
        "id": "ch1_fix_engine",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "Engine Trouble",
        "text": (
            "You crawl under the rocket with a flashlight. The engine looks "
            "fine... except for a small tear in the heat shield. You dig "
            "through the toolkit and find a roll of space-grade sticky patches — "
            "and tucked right at the back, a Stun Blaster, still in its case. "
            "Standard issue for alien encounters, apparently.\n\n"
            "PATCH! PATCH! PATCH!\n\n"
            "You slap three patches on the heat shield and shimmy back inside. "
            "The rattling stops. You pocket the Stun Blaster.\n\n"
            "Mission Control cheers: 'AMAZING! You fixed it! You are genuinely "
            "the best space explorer we have ever sent into space!'"
        ),
        "choices": [
            {
                "label": "Get back in the pilot seat — it's launch time!",
                "next": "ch1_countdown",
                "requires_item": None,
                "gives_item": "stun_blaster",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch1_countdown": {
        "id": "ch1_countdown",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "T-Minus 10...",
        "text": (
            "You buckle in. The countdown begins.\n\n"
            "TEN... NINE... EIGHT...\n\n"
            "The whole rocket shakes and rumbles.\n\n"
            "SEVEN... SIX... FIVE...\n\n"
            "You grip the armrests tightly.\n\n"
            "FOUR... THREE... TWO... ONE...\n\n"
            "BLAST OFF!!!\n\n"
            "The engines ROAR and you are pressed back into your seat as the "
            "Shooting Star rockets into the sky. The ground falls away below "
            "you. The sky turns from blue to purple to black. "
            "You are in SPACE!"
        ),
        "choices": [],
        "auto_next": "ch1_asteroid_belt",
        "ending": None,
    },

    "ch1_asteroid_belt": {
        "id": "ch1_asteroid_belt",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "Asteroid Belt!",
        "text": (
            "Space is AMAZING. Stars everywhere! You float a little in your "
            "seat (even with the seatbelt on).\n\n"
            "Then the radar starts BEEPING like crazy.\n\n"
            "WARNING! ASTEROID BELT AHEAD!\n\n"
            "Thousands of giant spinning rocks fill the screen. "
            "The route to Planet Zorbax goes right through them!\n\n"
            "You could try to fly straight through — risky but faster. "
            "Or you could fly around the belt — safe but it'll take much longer."
        ),
        "choices": [
            {
                "label": "Fly through the asteroid belt! I'm a great pilot!",
                "next": "ch1_asteroid_dodge",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Go around the belt. Safety first!",
                "next": "ch1_asteroid_around",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Check the Mission Map — maybe there's a safe route through.",
                "next": "ch1_map_shortcut",
                "requires_item": "mission_map",
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch1_map_shortcut": {
        "id": "ch1_map_shortcut",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "Hidden Corridor!",
        "text": (
            "You unfold the star chart. There — almost invisible among the "
            "asteroid density lines — a thin dotted path marked in green ink. "
            "A hidden corridor, carved out by an ancient comet millions of "
            "years ago. The rocks here are sparse, the gaps wide.\n\n"
            "You ease the Shooting Star into the corridor. "
            "Giant glittering asteroids drift past on either side, close enough "
            "to see their craters, but never close enough to hit. "
            "One is shaped like a rubber duck. You take a photo.\n\n"
            "And then — open space. The belt is behind you, "
            "and the ship doesn't have a scratch.\n\n"
            "'Explorer,' says Mission Control, 'that was SMOOTH.'"
        ),
        "choices": [],
        "auto_next": "ch1_deep_space",
        "ending": None,
    },

    "ch1_asteroid_dodge": {
        "id": "ch1_asteroid_dodge",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "INCOMING!",
        "text": (
            "You grab the controls and DIVE IN.\n\n"
            "WHOOSH — barrel-roll past a boulder the size of a school bus!\n"
            "ZOOM — spin on your axis and thread a gap barely wider than the ship!\n"
            "CLANG — a rock clips your left wing. Alarms blare. You overcorrect. "
            "The ship SPINS.\n\n"
            "For one terrifying second you see nothing but tumbling grey rock in "
            "every direction.\n\n"
            "Then — open space.\n\n"
            "You're through. Somehow.\n\n"
            "Your hands won't stop shaking. The damage readout is flashing: "
            "HULL INTEGRITY — SECTION C — WARNING.\n\n"
            "Mission Control, sounding terrified: 'Explorer. You just — we saw that — "
            "the asteroid actually HIT you — HOW ARE YOU ALIVE RIGHT NOW?'\n\n"
            "You stare at the warning light. Something is going to need fixing."
        ),
        "choices": [
            {
                "label": "Press on. Report the damage and keep going.",
                "next": "ch1_oxygen_alarm",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch1_oxygen_alarm": {
        "id": "ch1_oxygen_alarm",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "HULL BREACH!",
        "text": (
            "BWAAAAAAMP! BWAAAAAAMP!\n\n"
            "Every red light in the cockpit turns on at once.\n\n"
            "HULL BREACH — SECTION C. OXYGEN LOSS DETECTED.\n\n"
            "The rock punched a hole the size of your thumb clean through the hull. "
            "Air is hissing out into space. The oxygen gauge is dropping fast.\n\n"
            "Mission Control, very fast: 'Explorer. Hull breach confirmed. "
            "Oxygen dropping. You have three minutes. SEAL IT NOW.'\n\n"
            "You scan the cockpit. You have to act NOW."
        ),
        "choices": [
            {
                "label": "Use your Space Suit Patch — slap it over the breach RIGHT NOW!",
                "next": "ch1_patch_fix",
                "requires_item": "space_suit_patch",
                "gives_item": None,
                "removes_item": "space_suit_patch",
            },
            {
                "label": "Grab the emergency foam canister from under the seat!",
                "next": "ch1_foam_fix",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Ignore it — you'll deal with it later.",
                "next": "ch1_death_oxygen",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch1_death_oxygen": {
        "id": "ch1_death_oxygen",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "Out of Air...",
        "text": (
            "You decide to deal with the hull breach later.\n\n"
            "That was a mistake.\n\n"
            "The oxygen gauge drops. 50%. 40%. You start to feel dizzy. "
            "The lights seem brighter. Your fingers go a little numb.\n\n"
            "30%.\n\n"
            "Mission Control is shouting but it sounds far away, like they're "
            "at the other end of a very long corridor.\n\n"
            "20%.\n\n"
            "You reach toward the controls. Your hand moves very slowly.\n\n"
            "The stars outside are very beautiful. You think about that.\n\n"
            "You take a breath. There's almost nothing to breathe.\n\n"
            "The Shooting Star drifts on, quiet and dark, through the stars."
        ),
        "choices": [],
        "auto_next": None,
        "ending": "lose",
        "lose_reason": "You ran out of oxygen. Always fix a hull breach!",
    },

    "ch1_patch_fix": {
        "id": "ch1_patch_fix",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "Sealed!",
        "text": (
            "You rip the patch from your kit and SLAM it over the breach.\n\n"
            "The hissing stops. The oxygen gauge steadies.\n\n"
            "You sink back into your seat and breathe — slowly, deliberately — "
            "for about thirty full seconds.\n\n"
            "'Seal confirmed,' says Mission Control. Their voice is shaking.\n\n"
            "Your Space Suit Patch is gone. Used up. Hopefully that's the last "
            "thing that needs patching for a while.\n\n"
            "You get back to flying. Ahead, stars blur past... and then the radio "
            "crackles with something that is definitely not Mission Control.\n\n"
            "A high-pitched bubbly voice: 'BZZZT — glorp — WELCOME, SMALL PINK "
            "SPACE CREATURE — glorp — WE HAVE SEEN YOUR SHINY FLYING ROCK — BZZZT'\n\n"
            "A green-blue planet fills your screen. Zorbax."
        ),
        "choices": [],
        "auto_next": "ch2_orbit",
        "ending": None,
    },

    "ch1_foam_fix": {
        "id": "ch1_foam_fix",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "Sealed (Mostly)!",
        "text": (
            "You drop to your knees and rummage under the pilot's seat.\n\n"
            "Yellow canister. EMERGENCY FOAM SEALANT. You never noticed it before. "
            "Currently the most beautiful object in the universe.\n\n"
            "You jam the nozzle into the breach and PRESS.\n\n"
            "FFFSSSSSHH! Orange foam erupts from the can, expands, and fills the gap. "
            "The hissing dies to a whisper, then nothing.\n\n"
            "Oxygen gauge: 69%. Mission Control: 'Seal is holding. Technically.'\n\n"
            "You don't ask about the other 31%. Some things are better unknown. "
            "You name the orange foam blob Gerald.\n\n"
            "The radio crackles with something that is not Mission Control.\n\n"
            "A bubbly, kazoo-like voice: 'BZZZT — glorp — WELCOME, SMALL PINK "
            "SPACE CREATURE — glorp — WE HAVE SEEN YOUR SHINY FLYING ROCK — BZZZT'\n\n"
            "A green-blue planet fills your screen. Zorbax."
        ),
        "choices": [],
        "auto_next": "ch2_orbit",
        "ending": None,
    },

    "ch1_asteroid_around": {
        "id": "ch1_asteroid_around",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "The Long Way Around",
        "text": (
            "Smart thinking! You swing the Shooting Star wide around the asteroid "
            "belt. It takes a few extra hours, but the view is spectacular — "
            "the asteroids glow gold and silver as the sun hits them.\n\n"
            "You even spot a tiny asteroid shaped exactly like a rubber duck. "
            "You take a photo to show your family later.\n\n"
            "Safe and sound, you come out the other side of the belt. "
            "Planet Zorbax is straight ahead!"
        ),
        "choices": [
            {
                "label": "Full speed to Planet Zorbax!",
                "next": "ch1_deep_space",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch1_deep_space": {
        "id": "ch1_deep_space",
        "chapter": 1,
        "chapter_title": "Blast Off!",
        "title": "A Strange Signal...",
        "text": (
            "Deep space surrounds you. A billion stars twinkle in every direction.\n\n"
            "Suddenly, the radio crackles. But it isn't Mission Control. "
            "The voice is high-pitched and bubbly, like talking underwater while "
            "someone is also playing a kazoo:\n\n"
            "'BZZZT — glorp — WELCOME, SMALL PINK SPACE CREATURE — glorp — "
            "WE HAVE SEEN YOUR SHINY FLYING ROCK — glorp — PLEASE DO NOT "
            "BRING ANY CATS — BZZZT'\n\n"
            "The signal cuts out. You stare at the radio for a long time.\n\n"
            "A green-blue planet fills your screen. That must be Zorbax.\n\n"
            "Here goes nothing!"
        ),
        "choices": [],
        "auto_next": "ch2_orbit",
        "ending": None,
    },

    # ──────────────────────────────────────────────────────────────────
    # CHAPTER 2 — PLANET ZORBAX
    # ──────────────────────────────────────────────────────────────────

    "ch2_orbit": {
        "id": "ch2_orbit",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "Orbiting Zorbax",
        "text": (
            "You circle the planet once. It is BEAUTIFUL — swirling green "
            "clouds, purple oceans, and patches of sparkling silver forest.\n\n"
            "The radar shows lots of heat signatures below — cities? Camps? "
            "Whoever lives here, there are a LOT of them.\n\n"
            "You start your descent."
        ),
        "choices": [
            {
                "label": "Begin landing sequence!",
                "next": "ch2_landing_crash",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch2_landing_crash": {
        "id": "ch2_landing_crash",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "BRACE FOR IMPACT!",
        "text": (
            "Zorbax's atmosphere hits you like a wall — the ship bucks and "
            "SCREAMS as it punches through banks of green cloud at completely "
            "the wrong angle.\n\n"
            "You fight the controls. They're not listening.\n\n"
            "Through the viewscreen: a flat clearing. You HURL the ship toward it. "
            "Almost — almost—\n\n"
            "KERRRRCRRASH!\n\n"
            "You bounce off a boulder, clip a silver tree, and the ship SLIDES — "
            "sparks flying, alien soil spraying — directly toward the edge "
            "of a cliff.\n\n"
            "The drop below is a very, very long way down.\n\n"
            "You have exactly one second."
        ),
        "choices": [
            {
                "label": "EMERGENCY BRAKES — everything you've got!",
                "next": "ch2_landing_saved",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Yank the nose HARD — spin the ship to bleed speed!",
                "next": "ch2_landing_saved",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Aim for the alien forest — the trees will cushion the crash!",
                "next": "ch2_landing_forest",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch2_landing_forest": {
        "id": "ch2_landing_forest",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "Into the Forest!",
        "text": (
            "You wrench the controls toward the silver-leafed forest at the "
            "edge of the clearing and HOLD ON.\n\n"
            "CRUNCH — the first tree hits the nose like a huge springy cushion. "
            "The ship bounces. Straight up. "
            "Then comes back down and hits ANOTHER tree.\n\n"
            "BOINNNG.\n\n"
            "Back up. Back down. Third tree.\n\n"
            "BOINNNG.\n\n"
            "On the third bounce, the Shooting Star sails gently through a gap "
            "in the canopy and settles — perfectly upright — in a sunny clearing.\n\n"
            "You look out the window. A dozen small green aliens are standing "
            "at the treeline. They watched the whole thing. "
            "They are completely motionless.\n\n"
            "Then they look at each other. Then back at you.\n\n"
            "Then they all start doing the alien version of a standing ovation — "
            "antennae spinning wildly, tiny capes flapping."
        ),
        "choices": [],
        "auto_next": "ch2_alien_welcome",
        "ending": None,
    },

    "ch2_landing_saved": {
        "id": "ch2_landing_saved",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "That Was Close.",
        "text": (
            "The ship jolts. Grinds. Slows.\n\n"
            "Stops.\n\n"
            "You look out the viewscreen.\n\n"
            "Two metres from the edge.\n\n"
            "You sit with your hands gripping the controls for a very long time. "
            "Then, very slowly, you open the hatch.\n\n"
            "The air smells like cinnamon. The ship has a dent the size of a "
            "bathtub in the hull and half a silver tree stuck in the landing gear. "
            "But you're alive. And you're on an alien planet.\n\n"
            "'HA!' you say, to the cliff. To the planet. To the universe in general.\n\n"
            "Nobody needs to know how the landing actually went."
        ),
        "choices": [],
        "auto_next": "ch2_alien_welcome",
        "ending": None,
    },

    "ch2_alien_welcome": {
        "id": "ch2_alien_welcome",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "First Contact!",
        "text": (
            "You turn around slowly and find yourself face-to-face with "
            "five aliens.\n\n"
            "They are small — about waist-height — with big round purple eyes, "
            "bright green skin, and three tiny antennae each. They are wearing "
            "what look like tiny bow ties and capes. Very fancy.\n\n"
            "They stare at you. You stare at them.\n\n"
            "One of them opens their mouth and makes the kazoo-underwater noise "
            "from the radio. The others nod seriously.\n\n"
            "What do you do?"
        ),
        "choices": [
            {
                "label": "Give a big friendly wave and smile!",
                "next": "ch2_friendly_aliens",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Hide behind the ship immediately.",
                "next": "ch2_hiding",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Shout 'BACK OFF!' and wave your arms to scare them away!",
                "next": "ch2_death_aliens",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch2_death_aliens": {
        "id": "ch2_death_aliens",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "That Was Not a Good Idea.",
        "text": (
            "You wave your arms and shout.\n\n"
            "The aliens stare at you.\n\n"
            "They look at each other. Back at you. They make a sound — "
            "not the happy kazoo noise. A different one. Lower. Slower.\n\n"
            "All five of them take a step back.\n\n"
            "Then all five of them raise tiny devices that look like they might "
            "be communication tools, but definitely aren't.\n\n"
            "You realise, a moment too late, that on Planet Zorbax, waving "
            "your arms and shouting is the traditional way to challenge "
            "someone to a duel.\n\n"
            "You have just challenged FIVE ALIENS at once.\n\n"
            "It turns out they take duels very seriously here.\n\n"
            "The mission ends here, on a beautiful alien planet, "
            "surrounded by very offended aliens in bow ties.\n\n"
            "Next time: wave nicely."
        ),
        "choices": [],
        "auto_next": None,
        "ending": "lose",
        "lose_reason": "First contact rule: be friendly! Shouting is a duel challenge on Zorbax.",
    },

    "ch2_hiding": {
        "id": "ch2_hiding",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "Hiding!",
        "text": (
            "You duck behind the ship and hold very still.\n\n"
            "There is a long silence.\n\n"
            "Then a tiny green face appears around the corner of the ship, "
            "right at your level, enormous purple eyes staring directly at you.\n\n"
            "It tilts its head.\n\n"
            "You realize that aliens on their own planet probably know "
            "where you are.\n\n"
            "The alien waves cheerfully. Three times. Very enthusiastically.\n\n"
            "Okay. Maybe they ARE friendly."
        ),
        "choices": [
            {
                "label": "Wave back. Okay, hi aliens!",
                "next": "ch2_friendly_aliens",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch2_friendly_aliens": {
        "id": "ch2_friendly_aliens",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "New Friends!",
        "text": (
            "The aliens go WILD when you wave! They jump up and down, "
            "spin their antennae, and make excited kazoo noises.\n\n"
            "The tallest one (still only waist-high) steps forward and holds "
            "out a tiny fist. You bump it. This was apparently the right thing "
            "to do — they all cheer.\n\n"
            "One of them runs off and comes back carrying a small bag. They "
            "reach in and offer you something: small purple rocks that smell "
            "exactly like strawberries.\n\n"
            "Alien candy! You try one. It tastes like strawberries mixed with "
            "birthday cake. INCREDIBLE. You keep the bag."
        ),
        "choices": [
            {
                "label": "Follow the aliens to their village.",
                "next": "ch2_alien_market",
                "requires_item": None,
                "gives_item": "alien_candy",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch2_alien_market": {
        "id": "ch2_alien_market",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "The Zorbax Market",
        "text": (
            "The alien village is amazing — tiny dome-shaped houses that glow "
            "from the inside, trees with silver leaves, and a bustling market "
            "full of aliens selling all kinds of strange things.\n\n"
            "One stall catches your eye immediately: hanging from the frame "
            "is a jetpack — and not just any jetpack. It has booster rockets, "
            "a cup holder, and flashing lights. It is the coolest thing "
            "you have ever seen.\n\n"
            "The alien running the stall points at the jetpack, then at you, "
            "then rubs their fingers together in the universal sign for 'trade'.\n\n"
            "They want something in return. They look at you hopefully — "
            "do you have anything worth swapping?"
        ),
        "choices": [
            {
                "label": "Trade your Mission Map for the jetpack!",
                "next": "ch2_has_jetpack",
                "requires_item": "mission_map",
                "gives_item": "jetpack",
            },
            {
                "label": "You have nothing to offer. Politely shake your head.",
                "next": "ch2_no_jetpack",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Offer your Stun Blaster as trade!",
                "next": "ch2_blaster_trade",
                "requires_item": "stun_blaster",
                "gives_item": None,
                "removes_item": "stun_blaster",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch2_blaster_trade": {
        "id": "ch2_blaster_trade",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "The Blaster Trade",
        "text": (
            "You pull out the Stun Blaster and hold it up.\n\n"
            "The alien's eyes go ENORMOUS. Their antennae shoot straight up. "
            "They lean so far over the counter they nearly fall off their stool.\n\n"
            "They take the blaster very carefully with both hands, turn it over, "
            "examine every detail, then point it at a nearby market stall "
            "and — before you can say anything — PRESS THE BUTTON.\n\n"
            "ZZZAP! The blue beam hits a display of floating snack-pods. "
            "They all fall asleep simultaneously and drift gently to the ground. "
            "The stall owner looks from the stall to the alien to you. "
            "Then they start laughing.\n\n"
            "All the other aliens start laughing. "
            "The alien tests the stun beam again on a hat stand. Also asleep.\n\n"
            "'MOST FASCINATING THING I HAVE EVER SEEN,' they announce, "
            "and immediately hand you the jetpack. Deal done."
        ),
        "choices": [
            {
                "label": "Strap on the jetpack!",
                "next": "ch2_volcano",
                "requires_item": None,
                "gives_item": "jetpack",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch2_has_jetpack": {
        "id": "ch2_has_jetpack",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "Jetpack!",
        "text": (
            "Deal! You hand over the map and the alien hands you the jetpack "
            "with what is definitely a huge grin (hard to tell with three "
            "antennae, but it feels right).\n\n"
            "You strap it on. It fits perfectly. You press the TEST button "
            "and WHOOOOOOSH — you fly three metres straight up and hover "
            "there for a second before gently coming back down.\n\n"
            "Every alien in the market stops and stares at you. "
            "Then they all burst into the most enthusiastic kazoo-cheering "
            "you have ever heard.\n\n"
            "One of the aliens tugs your sleeve and points toward a distant "
            "rumbling volcano. There are caves up there that glow at night — "
            "supposedly full of something amazing."
        ),
        "choices": [
            {
                "label": "Fly up to the volcano caves!",
                "next": "ch2_volcano",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch2_no_jetpack": {
        "id": "ch2_no_jetpack",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "Climbing the Hard Way",
        "text": (
            "The alien shrugs — no trade, no jetpack. But they seem friendly "
            "enough anyway, and point you toward a distant rumbling volcano, "
            "making gestures that suggest 'there's something amazing up there'.\n\n"
            "Without a jetpack, you have to climb. Hand over hand, up the "
            "rocky slope. Your arms ache. A small alien runs alongside you "
            "on the ground, cheering you on. Very helpful. Very small.\n\n"
            "Eventually you haul yourself up to the cave entrance, "
            "breathless but proud."
        ),
        "choices": [
            {
                "label": "Go into the volcano cave!",
                "next": "ch2_volcano",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch2_volcano": {
        "id": "ch2_volcano",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "The Volcano",
        "text": (
            "The cave entrance glows blue and purple. Inside, you can see "
            "crystals growing from the walls like giant blue icicles.\n\n"
            "But the cave is also very deep, and it's getting darker...\n\n"
            "Your radio crackles: Mission Control is picking up "
            "a signal from MUCH deeper in the cave. And also a signal "
            "from orbit — a HUGE structure up in space that wasn't there before.\n\n"
            "What do you do?"
        ),
        "choices": [
            {
                "label": "Explore deeper into the crystal cave.",
                "next": "ch2_crystal_cave",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Signal your ship and head back to space.",
                "next": "ch2_signal_ship",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Call into the cave — see if anything answers.",
                "next": "ch2_cave_shout",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch2_cave_shout": {
        "id": "ch2_cave_shout",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "Hello?",
        "text": (
            "You cup your hands around your mouth and shout into the cave:\n\n"
            "'HELLO?'\n\n"
            "Your voice bounces off a million crystals. "
            "HELLO hello hello hello...\n\n"
            "Silence.\n\n"
            "Then — deep in the cave, something SHINES. "
            "Just for a second. Brighter than before. Like something heard you "
            "and wanted you to know.\n\n"
            "You stare at the glow. The glow seems to stare back.\n\n"
            "Then a small alien steps out from behind a crystal near the entrance — "
            "one of the village aliens, who must have followed you. "
            "They look at the glow. They look at you. "
            "Their antennae wiggle with great urgency, pointing deeper into the cave.\n\n"
            "Whatever is in there, the alien thinks you should find it."
        ),
        "choices": [],
        "auto_next": "ch2_crystal_cave",
        "ending": None,
    },

    "ch2_signal_ship": {
        "id": "ch2_signal_ship",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "Back to the Ship",
        "text": (
            "You head back to the Shooting Star. The aliens wave you off with "
            "great enthusiasm. As you lift off, they stand in a circle "
            "and wave their antennae — which you are now completely certain "
            "is their version of a standing ovation.\n\n"
            "In orbit, the giant structure looms closer. It looks like a "
            "space station — but one that's been abandoned for a very long time. "
            "Overgrown with something glowing. Mysterious.\n\n"
            "You didn't find the crystal key, but you'll find another way in."
        ),
        "choices": [
            {
                "label": "Fly toward the space station.",
                "next": "ch3_station_approach",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch2_crystal_cave": {
        "id": "ch2_crystal_cave",
        "chapter": 2,
        "chapter_title": "Planet Zorbax",
        "title": "The Crystal Cave",
        "text": (
            "You venture deeper. The crystals grow bigger and BIGGER until "
            "they're taller than houses, glowing brilliant blue.\n\n"
            "At the very heart of the cave, you find a pedestal. "
            "On it sits a single crystal, perfectly shaped like a key — "
            "with the symbol of a space station engraved on the handle.\n\n"
            "You pick it up. It hums in your hand. The cave seems to glow "
            "BRIGHTER for a moment, like it's happy for you.\n\n"
            "Your radio crackles: 'Explorer! That space station just powered on. "
            "We think that key is what OPENS it. Get up here!'"
        ),
        "choices": [
            {
                "label": "Rush back to the Shooting Star and head for the station!",
                "next": "ch3_station_approach",
                "requires_item": None,
                "gives_item": "crystal_key",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    # ──────────────────────────────────────────────────────────────────
    # CHAPTER 3 — THE ABANDONED SPACE STATION
    # ──────────────────────────────────────────────────────────────────

    "ch3_station_approach": {
        "id": "ch3_station_approach",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "Station Omega",
        "text": (
            "The space station is ENORMOUS. It's shaped like a ring with a "
            "giant dome in the middle. Glowing green vines (SPACE vines) "
            "cover most of it. Some of the lights are flickering on — "
            "like it just woke up after a very long sleep.\n\n"
            "The name on the side reads: STATION OMEGA.\n\n"
            "There are two docking bays on opposite sides of the ring.\n\n"
            "Bay A has a working light and looks easy to dock with. "
            "Bay B is darker, but your sensors are picking up something "
            "alive in there..."
        ),
        "choices": [
            {
                "label": "Dock at Bay A — the lit, easy one.",
                "next": "ch3_bay_a",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Dock at Bay B — find out what's alive in there.",
                "next": "ch3_bay_b",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Orbit the station once first — look for any clues or other docking points.",
                "next": "ch3_orbit_station",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch3_orbit_station": {
        "id": "ch3_orbit_station",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "One Orbit",
        "text": (
            "You ease the Shooting Star into a slow orbit around the station. "
            "The sensors sweep the hull as you go.\n\n"
            "Interesting. Etchings on the metal — old mission logs, names, dates, "
            "tiny drawings of stars and ships. Someone lived here once and "
            "wanted the universe to know.\n\n"
            "And there — on the far side of the ring — a third docking bay. "
            "Bay C. No lights. Sensors say it's pressurised though, "
            "and there's a faint power reading. Emergency supplies, maybe. "
            "Long forgotten.\n\n"
            "Mission Control: 'Explorer, we can see Bay C. "
            "No one's been in there for a long time, but it looks intact.'"
        ),
        "choices": [
            {
                "label": "Dock at Bay C.",
                "next": "ch3_bay_c",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch3_bay_c": {
        "id": "ch3_bay_c",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "Bay C — Emergency Stores",
        "text": (
            "Bay C is dusty. Very dusty. "
            "Your footprints are the first in a very long time.\n\n"
            "Shelves run the length of the room — stacked with sealed containers. "
            "Emergency rations, mostly. The labels are in an alien language "
            "but the expiry dates are... hard to read. You decide not to eat any.\n\n"
            "In the corner: a metal locker, slightly dented. You yank it open.\n\n"
            "Inside, hanging on a hook, is a security blaster. Old model, "
            "dusty grip — but the charge indicator glows green. "
            "Still working after all these years.\n\n"
            "You pick it up. Feels solid. Reliable. Good."
        ),
        "choices": [
            {
                "label": "Take the blaster and head to the Main Hall.",
                "next": "ch3_main_hall",
                "requires_item": None,
                "gives_item": "stun_blaster",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch3_bay_a": {
        "id": "ch3_bay_a",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "Bay A",
        "text": (
            "Bay A docking goes smoothly. You step into a long corridor. "
            "Emergency lights cast everything in orange. Dust floats in the air. "
            "It's been empty for a LONG time.\n\n"
            "You find a map on the wall. The Control Room is at the centre "
            "of the station. You'll need to pass through the Main Hall to get there.\n\n"
            "Just you and the eerie silence. Let's go."
        ),
        "choices": [
            {
                "label": "Head through the corridor to the Main Hall.",
                "next": "ch3_main_hall",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch3_bay_b": {
        "id": "ch3_bay_b",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "Bay B — Something Alive!",
        "text": (
            "You dock carefully. In the dark of Bay B, your flashlight "
            "finds... a small robot.\n\n"
            "It's about the size of a backpack, boxy and dented, with "
            "two big round optical sensors (its 'eyes'). It looks at you "
            "and says, very quietly: 'BEEP BOOP?'\n\n"
            "It's been alone here for a very long time. It looks so sad.\n\n"
            "You reach out your hand. It rolls forward and bumps against "
            "your palm. 'BEEP BOOP!' (Happy version.)\n\n"
            "You've got a robot friend now. It rolls along beside you "
            "as you head into the station."
        ),
        "choices": [
            {
                "label": "Head to the Main Hall with your new robot friend.",
                "next": "ch3_main_hall",
                "requires_item": None,
                "gives_item": "robot_friend",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch3_main_hall": {
        "id": "ch3_main_hall",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "The Main Hall",
        "text": (
            "The Main Hall is a huge domed room. The ceiling is glass and "
            "stars are visible above. Old space maps cover the walls. "
            "In the centre is a big round table with dusty chairs.\n\n"
            "Suddenly: BLARING ALARMS! RED LIGHTS!\n\n"
            "A robotic voice from the walls booms: 'INTRUDER ALERT. "
            "SECURITY DRONES ACTIVATED. INTRUDER ALERT.'\n\n"
            "Two floating metal security drones appear from side corridors, "
            "spinning and beeping. They're heading toward you!\n\n"
            "What do you do?"
        ),
        "choices": [
            {
                "label": "Use the Stun Blaster to stop the drones!",
                "next": "ch3_laser_battle",
                "requires_item": "stun_blaster",
                "gives_item": None,
            },
            {
                "label": "Dive under the table and hide!",
                "next": "ch3_hiding_drones",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Talk to the drones — try to explain you're friendly.",
                "next": "ch3_bluff_drones",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "CHARGE at them with bare hands! AAARRGH!",
                "next": "ch3_death_drones",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch3_death_drones": {
        "id": "ch3_death_drones",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "Drones: 2. Explorer: 0.",
        "text": (
            "You charge at the drones with your bare hands.\n\n"
            "The first drone dodges left.\n\n"
            "The second drone dodges right.\n\n"
            "You run directly between them and smack face-first into the wall.\n\n"
            "The drones look at you lying on the floor. "
            "One of them emits a very long, very flat 'BEEEEEP.' "
            "The robotic voice says: 'THREAT LEVEL: EXTREMELY LOW.'\n\n"
            "Both drones fire their stun beams simultaneously.\n\n"
            "You wake up three hours later, back in your ship, "
            "which the drones have very helpfully pushed out of the docking bay. "
            "The station doors are sealed. A small sign has been placed on them.\n\n"
            "It says: PLEASE DO NOT RETURN.\n\n"
            "The mission is over. The drones were just doing their job."
        ),
        "choices": [],
        "auto_next": None,
        "ending": "lose",
        "lose_reason": "Security drones are not impressed by shouting. Try talking or hiding next time.",
    },

    "ch3_laser_battle": {
        "id": "ch3_laser_battle",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "Stun Blaster Battle!",
        "text": (
            "You whip out the Stun Blaster and take aim!\n\n"
            "ZZZZAP! A blue beam hits Drone #1. It spins, sparks, "
            "and then beeps in a confused sort of way before floating gently "
            "to the ground, asleep.\n\n"
            "ZZZZAP! Drone #2 sees what happened and tries to zoom away — "
            "but you're quicker. It too wobbles and sinks to the floor, "
            "letting out a single sad 'BOOP'.\n\n"
            "The alarms stop. Silence falls.\n\n"
            "On one of the sleeping drones, you notice a shiny star-shaped "
            "badge pinned to its chassis — looks like an achievement badge "
            "for 'BEST SECURITY.' You take it. You earned it."
        ),
        "choices": [
            {
                "label": "Continue to the Control Room.",
                "next": "ch3_control_room",
                "requires_item": None,
                "gives_item": "star_badge",
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch3_hiding_drones": {
        "id": "ch3_hiding_drones",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "Under the Table",
        "text": (
            "You hit the floor and slide under the table in one desperate motion.\n\n"
            "The drones sweep the room. Sensor beams cut left, right, left — "
            "scanning every corner. Every shadow.\n\n"
            "One drone drifts toward the table.\n\n"
            "Slower.\n\n"
            "Slower.\n\n"
            "It stops directly in front of you. The sensor hums. Something "
            "in its programming knows something is here.\n\n"
            "The beam lowers. It scans under the table. Directly across "
            "your left hand.\n\n"
            "You do not move a single muscle.\n\n"
            "The second drone crashes into a toppled chair at the far side of "
            "the room. The first one spins away to investigate.\n\n"
            "You breathe. Just barely.\n\n"
            "The drones circle twice more, then retreat. 'THREAT LEVEL REDUCED. "
            "RETURNING TO STANDBY.'\n\n"
            "You crawl out covered in dust, heart pounding like a drum. "
            "You are NEVER hiding under a table again."
        ),
        "choices": [
            {
                "label": "Hurry to the Control Room before they come back!",
                "next": "ch3_control_room",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch3_bluff_drones": {
        "id": "ch3_bluff_drones",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "Talking to Drones",
        "text": (
            "You hold up your hands and say, very clearly:\n\n"
            "'I am not an intruder. I am a Space Explorer from Earth. "
            "I am here to help. Please calm down.'\n\n"
            "The drones stop. They tilt at you. One emits a low beeep.\n\n"
            "The robotic voice says: 'UNRECOGNISED SPECIES. CROSS-REFERENCING... "
            "CROSS-REFERENCING... NO MATCH. DEFAULTING TO: PROBABLY FINE.'\n\n"
            "Both drones beep once each and float peacefully back to their posts.\n\n"
            "You talk your way out of a robot fight. Genius."
        ),
        "choices": [
            {
                "label": "Head to the Control Room.",
                "next": "ch3_control_room",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch3_control_room": {
        "id": "ch3_control_room",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "The Control Room",
        "text": (
            "The Control Room door is at the end of a long corridor. "
            "It's HUGE — metal, ancient, covered in warning symbols.\n\n"
            "In the centre of the door is a lock shaped like a crystal.\n\n"
            "Next to the door is a dusty panel with wires hanging out of it "
            "— someone could probably hack into it, but it looks VERY complicated.\n\n"
            "Mission Control radios in: 'Explorer, we can see on your camera — "
            "that lock looks exactly like the crystal key shape. "
            "But if you don't have a key, there's also a manual override panel...'"
        ),
        "choices": [
            {
                "label": "Use the Crystal Key to open the door!",
                "next": "ch3_key_door",
                "requires_item": "crystal_key",
                "gives_item": None,
            },
            {
                "label": "Hack the override panel.",
                "next": "ch3_hack_panel",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Ask your Robot Friend to interface with the station computer.",
                "next": "ch3_robot_access",
                "requires_item": "robot_friend",
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch3_robot_access": {
        "id": "ch3_robot_access",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "Robot to the Rescue",
        "text": (
            "You point your robot friend at the wall beside the door. "
            "It considers this for a moment, then rolls forward "
            "and finds a small port, half-hidden behind a panel, "
            "that you would never have noticed on your own.\n\n"
            "It plugs in with a satisfying click.\n\n"
            "BEEP. BOOP. BEEP BEEP BOOP BOOP BEEEEP.\n\n"
            "Its eyes flash. It's working through the station's systems — "
            "past the old security layers, past the locked archives, "
            "right down to the maintenance override buried at the very bottom.\n\n"
            "The door slides open. Smooth. Quiet. No grinding, no drama. "
            "Just a soft hum and a gentle puff of old air.\n\n"
            "The robot unplugs itself and turns to you.\n\n"
            "'BEEP BOOP,' it says. Proudly."
        ),
        "choices": [],
        "auto_next": "ch3_hull_breach",
        "ending": None,
    },

    "ch3_key_door": {
        "id": "ch3_key_door",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "The Crystal Key Works!",
        "text": (
            "You slot the crystal key into the lock. It fits PERFECTLY. "
            "The crystal glows, the door hums, and then — with a deep satisfying "
            "CLUNK — it swings open.\n\n"
            "Inside the Control Room, screens flicker to life. Maps of the "
            "galaxy cover every wall. And right in the centre is a giant "
            "holographic message floating in the air:\n\n"
            "'IF YOU ARE READING THIS: DANGER. A FLEET OF ALIEN SHIPS IS "
            "HEADING TO THIS PART OF THE GALAXY. THEY ARE NOT DANGEROUS. "
            "THEY JUST REALLY, REALLY WANT TO SAY HELLO. "
            "BUT THERE ARE A LOT OF THEM. GOOD LUCK.'\n\n"
            "Your radar lights up. They're already here."
        ),
        "choices": [],
        "auto_next": "ch3_hull_breach",
        "ending": None,
    },

    "ch3_hack_panel": {
        "id": "ch3_hack_panel",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "Hacking the Panel",
        "text": (
            "You study the wires. Mission Control coaches you through it.\n\n"
            "'Okay, find the blue wire.' You find it.\n"
            "'Now the green one.' Got it.\n"
            "'Now... cross them while pressing the big button and saying "
            "the words OPEN SESAME.'\n\n"
            "You try it. The door makes an unhappy grinding noise and opens "
            "exactly 30 centimetres — just wide enough for you to squeeze through.\n\n"
            "Inside, the Control Room is full of screens and galaxy maps. "
            "A holographic message pulses:\n\n"
            "'IF YOU ARE READING THIS: A FLEET OF ALIEN SHIPS IS COMING. "
            "THEY JUST WANT TO SAY HELLO. THERE ARE VERY MANY OF THEM. GOOD LUCK.'\n\n"
            "Your radar lights up. They're already here."
        ),
        "choices": [],
        "auto_next": "ch3_hull_breach",
        "ending": None,
    },

    "ch3_hull_breach": {
        "id": "ch3_hull_breach",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "The Station is Breaking Apart!",
        "text": (
            "You're halfway down the corridor back to your ship when the "
            "station LURCHES.\n\n"
            "The lights die. Emergency red takes over.\n\n"
            "Then: a deep grinding MOAN through the walls. Decades of neglect "
            "catching up all at once. A section of outer hull — old, corroded, "
            "never meant to last this long — CRACKS.\n\n"
            "The suction is immediate. Papers, dust, and one very old coffee mug "
            "fly past your head toward the breach and disappear into space.\n\n"
            "You grab the door frame. Your feet lift off the ground.\n\n"
            "At the far end of the corridor: an emergency blast door, slowly "
            "grinding closed. Automatically. It will not wait for you.\n\n"
            "You have maybe twenty seconds."
        ),
        "choices": [
            {
                "label": "SPRINT. Full speed. GO NOW.",
                "next": "ch3_escaped_breach",
                "requires_item": None,
                "gives_item": None,
                "removes_item": "stun_blaster",
            },
            {
                "label": "Pull yourself hand-over-hand along the wall grips — fast but controlled.",
                "next": "ch3_escaped_breach",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Strap on the Jetpack and FLY to the blast door!",
                "next": "ch3_escaped_breach",
                "requires_item": "jetpack",
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch3_escaped_breach": {
        "id": "ch3_escaped_breach",
        "chapter": 3,
        "chapter_title": "The Abandoned Space Station",
        "title": "Made It!",
        "text": (
            "You clear the blast door.\n\n"
            "It slams shut behind you with a sound like a cannon.\n\n"
            "You land on the floor of the safe corridor and stay there for a "
            "moment, staring at the ceiling.\n\n"
            "On the other side of the blast door, that section of the station "
            "is now open to space.\n\n"
            "You allow yourself five full seconds of just lying there.\n\n"
            "Then: your ship. You need to get to your ship.\n\n"
            "You run."
        ),
        "choices": [],
        "auto_next": "ch4_alien_mothership",
        "ending": None,
    },

    # ──────────────────────────────────────────────────────────────────
    # CHAPTER 4 — THE FINAL MISSION
    # ──────────────────────────────────────────────────────────────────

    "ch4_alien_mothership": {
        "id": "ch4_alien_mothership",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "The Mothership",
        "text": (
            "You burst out of the station airlock and the Shooting Star's "
            "engines catch — and then you see it.\n\n"
            "THE SHIP.\n\n"
            "It is the size of a small city. It has engines the size of "
            "office buildings. It fills your entire viewscreen, humming with "
            "the deep thrum of something that could probably push a moon. "
            "There is an enormous smiley face painted on the front, which "
            "would be charming if it wasn't also POINTED DIRECTLY AT YOU.\n\n"
            "Warning lights flood your cockpit. "
            "WEAPONS LOCK. WEAPONS LOCK. FOURTEEN TARGETING BEAMS ACTIVE.\n\n"
            "Mission Control, barely above a whisper: 'Explorer. Don't. Move.'\n\n"
            "A single smaller ship ejects from the mothership and glides toward "
            "you. It stops just in front of your cockpit window. A hatch opens.\n\n"
            "Inside: a very tall alien in a gold uniform with the most impressive "
            "antennae you have ever seen. They stare at you. At your battered, "
            "dented, visibly-repaired ship.\n\n"
            "Very slowly, they raise one hand.\n\n"
            "And wave."
        ),
        "choices": [
            {
                "label": "Hold completely still and wave back. Slowly. Carefully.",
                "next": "ch4_weapons_lock",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "FLOOR IT — maximum engine speed — get away NOW!",
                "next": "ch4_death_flee",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Broadcast a message of peace on all emergency radio channels.",
                "next": "ch4_emergency_radio",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch4_emergency_radio": {
        "id": "ch4_emergency_radio",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "On All Frequencies",
        "text": (
            "You key up every frequency on the radio panel — all of them, "
            "from emergency channel one to the very last one that nobody "
            "ever uses — and you speak very clearly:\n\n"
            "'Hello. I'm a Space Explorer from Earth. I come in peace. "
            "Also I am very small and my ship is a bit battered. "
            "Please do not shoot.'\n\n"
            "Silence. The targeting beams stay on.\n\n"
            "Then — the targeting beams start blinking. All fourteen of them. "
            "In a pattern. Like a rhythm.\n\n"
            "Mission Control, very quietly: 'Explorer... I think they're laughing?'\n\n"
            "The mothership's main screen lights up. A face fills your window — "
            "tall, gold-uniformed, magnificent antennae — and the alien captain "
            "is absolutely, unmistakably, completely delighted.\n\n"
            "The targeting beams keep blinking. It is definitely laughing."
        ),
        "choices": [
            {
                "label": "Wave hello!",
                "next": "ch4_weapons_lock",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch4_death_flee": {
        "id": "ch4_death_flee",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "You Can't Outrun a City.",
        "text": (
            "You slam the throttle forward.\n\n"
            "The Shooting Star's engines scream.\n\n"
            "For about two seconds, you are moving quite fast.\n\n"
            "The mothership — which is the size of a small city with engines "
            "the size of office buildings — does not move for those two seconds.\n\n"
            "Then it moves.\n\n"
            "You are caught by a tractor beam before you've gone half a kilometre. "
            "The Shooting Star stops dead. Every screen shows the same thing: "
            "a very large alien face, looking extremely disappointed.\n\n"
            "They waited fourteen million space-miles to say hello.\n\n"
            "They waved.\n\n"
            "And you ran away.\n\n"
            "'BZZZT — glorp — WE JUST WANTED TO BE FRIENDS — glorp — BZZZT'\n\n"
            "They tow your ship back to Earth. Mission Control doesn't ask "
            "many questions. The aliens never call again.\n\n"
            "Next time: wave back."
        ),
        "choices": [],
        "auto_next": None,
        "ending": "lose",
        "lose_reason": "You can't outrun a mothership. When a giant alien fleet waves at you, wave back!",
    },

    "ch4_weapons_lock": {
        "id": "ch4_weapons_lock",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "Fourteen Targeting Beams",
        "text": (
            "You raise one hand. Very slowly. And wave.\n\n"
            "The alien watches you. The weapons lock tone keeps beeping. "
            "Fourteen beams still active.\n\n"
            "You keep waving. And then — because you genuinely cannot help "
            "yourself — you smile.\n\n"
            "The alien tilts their head. They look at your ship. "
            "At the enormous dents along the hull. At the piece of silver tree "
            "still jammed in the landing gear. At the general state of the ship, "
            "which has clearly had a journey.\n\n"
            "They look back at you.\n\n"
            "They make a sound. A sort of kazoo-mixed-with-laughter noise. "
            "They make it louder. Then louder still.\n\n"
            "All fourteen targeting beams switch off simultaneously.\n\n"
            "'BZZZT — glorp — WHAT HAPPENED TO YOUR SHIP — glorp — YOU ARE "
            "THE SMALLEST AND MOST BATTERED SPACE CREATURE WE HAVE EVER SEEN "
            "— glorp — WE LOVE IT — BZZZT'\n\n"
            "Your translation device kicks in. Radio channel: open."
        ),
        "choices": [
            {
                "label": "Open the channel. Introduce yourself.",
                "next": "ch4_captain_alien",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch4_captain_alien": {
        "id": "ch4_captain_alien",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "The Alien Captain",
        "text": (
            "The alien captain speaks. It sounds like a kazoo playing a "
            "very formal symphony. Your translation device struggles... "
            "and then kicks in:\n\n"
            "'GREETINGS, SMALL PINK SPACE CREATURE! WE ARE THE ZORBIANS. "
            "WE HAVE TRAVELLED FOURTEEN MILLION SPACE-MILES TO FIND YOU. "
            "WE HAVE A QUESTION OF THE GREATEST IMPORTANCE.'\n\n"
            "They lean forward very seriously.\n\n"
            "'...Do you have any snacks? We have been travelling for a very "
            "long time and we are quite hungry.'\n\n"
            "A long pause.\n\n"
            "'Also, we would like to be friends with your planet. But "
            "mainly: the snacks.'"
        ),
        "choices": [
            {
                "label": "Give them the Alien Candy from Planet Zorbax!",
                "next": "ch4_candy_gift",
                "requires_item": "alien_candy",
                "gives_item": None,
            },
            {
                "label": "You have no snacks — challenge them to a dance-off instead!",
                "next": "ch4_dance_off",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Show them your Star Badge — you defeated their own security drones!",
                "next": "ch4_badge_show",
                "requires_item": "star_badge",
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch4_badge_show": {
        "id": "ch4_badge_show",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "The Badge",
        "text": (
            "You reach into your suit and hold up the star badge you took "
            "from the sleeping security drone. 'BEST SECURITY,' it says, "
            "in small engraved letters.\n\n"
            "The Captain goes completely still.\n\n"
            "Every single antenna on their head stops moving.\n\n"
            "Very quietly: '...Is that... a Station Omega security drone badge?'\n\n"
            "'Yes,' you say.\n\n"
            "Another very long pause.\n\n"
            "'YOU DEFEATED THE STATION OMEGA SECURITY DRONES. AND TOOK. THEIR BADGE.'\n\n"
            "You nod.\n\n"
            "The Captain turns to the rest of the bridge and says something in Zorbian. "
            "There is a moment of complete silence across the entire mothership.\n\n"
            "Then: absolute uproar. Cheering, kazoo fanfares, "
            "at least one alien fainting dramatically.\n\n"
            "'WE HAVE BEEN TRYING TO RETIRE THOSE DRONES FOR FORTY YEARS. "
            "FORTY! YEARS! THEY KEPT REFUSING! THEY SAID THEY WERE TOO IMPORTANT! "
            "AND YOU — ONE SMALL PINK CREATURE — YOU JUST — IN ONE VISIT —'\n\n"
            "The Captain can barely speak through the laughter.\n\n"
            "'YOU ARE A LEGEND. WE DECLARE FRIENDSHIP IMMEDIATELY. NO FURTHER QUESTIONS.'"
        ),
        "choices": [
            {
                "label": "Accept the title!",
                "next": "ch4_alliance",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch4_candy_gift": {
        "id": "ch4_candy_gift",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "The Best Snack",
        "text": (
            "You hold up the bag of alien candy from Planet Zorbax.\n\n"
            "The Captain's antennae go STRAIGHT UP. Their eyes get wide. "
            "They grab the radio and shout something in Zorbian and "
            "the entire mothership shakes — it sounds like the biggest "
            "kazoo celebration in history.\n\n"
            "'THIS IS ZORBAX CANDY! THE FINEST FOOD IN THE GALAXY! "
            "WHERE DID YOU GET THIS?!'\n\n"
            "'From your friends on Planet Zorbax,' you say. 'They said hi.'\n\n"
            "The Captain stares at you for a moment and then bursts into "
            "what you can only describe as happy crying.\n\n"
            "'WE HAVE MISSED THEM SO MUCH. YOU HAVE BROUGHT US A GIFT FROM HOME.'\n\n"
            "All fourteen million ships in the fleet play a kazoo fanfare.\n\n"
            "The Captain straightens up: 'We would very much like to be friends "
            "with your Earth. You have earned it.'"
        ),
        "choices": [
            {
                "label": "Accept the friendship! Set course for Earth!",
                "next": "ch4_alliance",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch4_dance_off": {
        "id": "ch4_dance_off",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "Dance Off!",
        "text": (
            "You think fast. 'No snacks,' you say, 'but I can offer... "
            "a DANCE COMPETITION.'\n\n"
            "The captain blinks. Then their antennae wiggle.\n\n"
            "'A dance competition?' they say slowly. 'We have not done one "
            "of those in forty space-years.'\n\n"
            "The music starts — some sort of twelve-trumpet alien jazz. "
            "You do your best dance moves. The Captain watches seriously. "
            "Then they stand up and start doing the wildest dance you have "
            "ever seen in your life — antennae spinning, cape flying, "
            "three tiny hops followed by a full spin.\n\n"
            "Their crew goes absolutely bananas.\n\n"
            "The Captain stops, breathing hard, and announces: 'You started it. "
            "We finished it. THAT MAKES YOU OUR FRIEND.'\n\n"
            "Apparently that's how it works."
        ),
        "choices": [
            {
                "label": "Excellent! Accept the friendship and head for Earth!",
                "next": "ch4_alliance",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch4_alliance": {
        "id": "ch4_alliance",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "The Galactic Alliance",
        "text": (
            "The Captain reaches through your airlock and shakes your hand "
            "with three of their four hands at once (very formal, apparently).\n\n"
            "'On behalf of fourteen million Zorbian ships, we declare friendship "
            "with the people of Earth. You are brave and also a good dancer.'\n\n"
            "Your radio explodes with noise from Mission Control. Cheering, "
            "crying, someone playing a trumpet badly, a dog barking for some reason.\n\n"
            "The Captain smiles: 'We will escort you home. Is there anything "
            "else you need for the journey?'"
        ),
        "choices": [
            {
                "label": "Ask your Robot Friend to help plot the fastest route home.",
                "next": "ch4_robot_boost",
                "requires_item": "robot_friend",
                "gives_item": None,
            },
            {
                "label": "You're ready — head for home!",
                "next": "ch4_homeward",
                "requires_item": None,
                "gives_item": None,
            },
            {
                "label": "Ask the Zorbians if they could help repair the Shooting Star first.",
                "next": "ch4_ship_repair",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch4_ship_repair": {
        "id": "ch4_ship_repair",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "The Repair Crew",
        "text": (
            "'Actually,' you say, 'my ship is a little... worn. "
            "Do you think your engineers could take a look?'\n\n"
            "The Captain makes one call.\n\n"
            "Fifty tiny Zorbian engineers arrive in minutes. "
            "They swarm the Shooting Star, arguing enthusiastically with each other "
            "about the most interesting way to fix things. "
            "Two of them get into a debate about the dent that lasts six minutes. "
            "A third one just fixes the dent while the others are still arguing.\n\n"
            "Forty-five minutes later, the Shooting Star gleams like it just "
            "rolled off the factory floor. The dents are gone. "
            "The hull is smooth and bright. The silver tree has been carefully "
            "removed from the landing gear and — this is a very nice touch — "
            "replanted in a small pot and placed in the cockpit as a souvenir.\n\n"
            "Your robot friend supervised the whole operation and beeped "
            "approvingly at regular intervals.\n\n"
            "The lead engineer gives you a thumbs up. (They had clearly "
            "looked up what thumbs up means. Very touching.)"
        ),
        "choices": [
            {
                "label": "Thank them and head for home!",
                "next": "ch4_homeward",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch4_robot_boost": {
        "id": "ch4_robot_boost",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "BEEP BOOP!",
        "text": (
            "Your robot friend rolls up to the navigation console and plugs in.\n\n"
            "'BEEP BOOP!'\n\n"
            "The screens fill with calculations. The robot has found a shortcut "
            "through a fold in space that cuts the journey time in half!\n\n"
            "The Zorbian Captain watches this and says, awed: "
            "'That small box robot knows warp mathematics?!'\n\n"
            "'BEEP BOOP,' says the robot modestly.\n\n"
            "'WE WANT ONE,' says the Captain.\n\n"
            "You promise to introduce them to each other properly when you get home. "
            "The robot does a little spin of delight."
        ),
        "choices": [
            {
                "label": "Punch it — go to warp speed!",
                "next": "ch4_homeward",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch4_homeward": {
        "id": "ch4_homeward",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "Heading Home",
        "text": (
            "The Shooting Star turns toward the blue dot in the distance — Earth.\n\n"
            "All around you, fourteen million Zorbian ships form an escort. "
            "Their lights blink in patterns that Mission Control later figures out "
            "means 'SAFE TRAVELS, SMALL PINK FRIEND'.\n\n"
            "You lean back in your seat. Stars streak past as you hit top speed.\n\n"
            "You went to space. You fixed an engine, survived an asteroid belt, "
            "made friends with aliens, explored an ancient station, "
            "and just negotiated the first friendship between Earth and "
            "another civilization.\n\n"
            "Not bad for one day's work."
        ),
        "choices": [],
        "auto_next": "ch4_earth_approach",
        "ending": None,
    },

    "ch4_earth_approach": {
        "id": "ch4_earth_approach",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "Earth Ahead!",
        "text": (
            "Earth fills your entire screen. Blue oceans, white clouds, "
            "green land. Home.\n\n"
            "Your radio is going haywire. Every news station on Earth is "
            "broadcasting the fleet of alien ships. The whole world is watching.\n\n"
            "Mission Control, very emotional: 'Explorer... you did it. "
            "You really did it. We're picking up something on the radio "
            "from all the world's cities — they're cheering for you.'\n\n"
            "The Zorbian Captain pops up on screen one last time: "
            "'We will return in one Earth-year with gifts and better snacks. "
            "Also, your planet is very pretty. Tell the oceans we said hello.'\n\n"
            "You radio Earth: 'Shooting Star to Mission Control. "
            "I am coming home. And I brought friends.'"
        ),
        "choices": [
            {
                "label": "Begin final descent. BRING IT HOME!",
                "next": "ch4_ending_win",
                "requires_item": None,
                "gives_item": None,
            },
        ],
        "auto_next": None,
        "ending": None,
    },

    "ch4_ending_win": {
        "id": "ch4_ending_win",
        "chapter": 4,
        "chapter_title": "The Final Mission",
        "title": "Hero of the Galaxy!",
        "text": (
            "The Shooting Star touches down in the middle of a huge open field. "
            "The door opens and the roar of cheering hits you like a wall.\n\n"
            "Thousands of people are there. Cameras everywhere. Signs that say "
            "'WE LOVE YOU, EXPLORER' and 'BEST SPACE KID EVER'.\n\n"
            "The Head of the Academy steps forward and pins a medal on your chest. "
            "It's shaped like a star. It's the biggest star you've ever seen.\n\n"
            "'You made first contact with an alien civilisation,' she says. "
            "'You made friends. You brought home hope. You are the greatest "
            "Space Explorer who has ever lived.'\n\n"
            "Fourteen million Zorbian ships in orbit blink their lights all at once "
            "in a pattern that spells, in English: 'WE AGREE.'\n\n"
            "You did it. You REALLY did it.\n\n"
            "THE END\n\n"
            "~ ~ ~ ~ ~ ~\n\n"
            "Thanks for playing, Space Explorer!"
        ),
        "choices": [],
        "auto_next": None,
        "ending": "win",
    },
}
