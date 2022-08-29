import logging
import sys


def init_logging():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


# Bot

PYAUTOGUI_SLEEP_SECONDS_BETWEEN_CALLS = 1
START_SLEEP_SECONDS = 10

DO_OPEN_MONKEYS = True

CLICK_ON_MATCHING_CONFIDENCE = 0.9
WAIT_FOR_MATCHING_CONFIDENCE = 0.9525

RELOAD_TOWER_COUNTER = 3

CHECK_LEVEL_UP_COUNTER = 30
CHECK_GAME_PAUSED_COUNTER = 30
CHECK_DEFEATED_COUNTER = 20

LOGS_DIR = '_logs'

# Menu
BUTTON_MENU_PLAY = 'resources/menu/button_menu_play.png'
BUTTON_MENU_MAPS_EXPERT = 'resources/menu/button_menu_maps_expert.png'
BUTTON_MENU_EASY_DIFF = 'resources/menu/button_menu_easy_diff.png'
BUTTON_MENU_STANDARD_MODE = 'resources/menu/button_menu_standard_mode.png'

BUTTON_GAME_START = 'resources/menu/button_game_start.png'
BUTTON_GAME_FAST_FORWARD = 'resources/menu/button_game_fast_forward.png'
BUTTON_GAME_NEXT = 'resources/menu/button_game_next.png'
BUTTON_GAME_TO_HOME = 'resources/menu/button_game_to_home.png'
BUTTON_GAME_RESTART = 'resources/menu/button_game_restart.png'
BUTTON_GAME_RESTART_CONFIRM = 'resources/menu/button_game_confirm_restart.png'
BUTTON_GAME_FREEPLAY = 'resources/menu/button_game_freeplay.png'

PROMPT_DEFEAT = 'resources/menu/prompt_defeat.png'
PROMPT_LEVEL_UP = 'resources/menu/prompt_level_up.png'
PROMPT_MONKEY_KNOWLEDGE = 'resources/menu/prompt_monkey_knowledge.png'

PROMPT_OVERWRITE = 'resources/menu/prompt_overwrite.png'
BUTTON_OVERWRITE_OK = 'resources/menu/button_overwrite_ok.png'

# Events
COLLECTION_XS = range(50, 1500, 50)
COLLECTION_Y = 450

BUTTON_EVENT_COLLECT = 'resources/menu/button_event_collect.png'
BUTTON_EVENT_CONTINUE = 'resources/menu/button_event_continue.png'

# Towers
TOWER_NINJA_UPGRADE = 'resources/towers/ninja/upgrade_{}_{}.png'
TOWER_SUPER_UPGRADE = 'resources/towers/super/upgrade_{}_{}.png'

# Heroes
HERO_SELECTED_OBYN_0 = 'resources/towers/heroes/obyn_0.png'
HERO_SELECTED_OBYN_1 = 'resources/towers/heroes/obyn_1.jpg'
HERO_SELECTED_OBYN_2 = 'resources/towers/heroes/obyn_2.jpg'

HERO_SELECTED = {'obyn': [HERO_SELECTED_OBYN_0, HERO_SELECTED_OBYN_1, HERO_SELECTED_OBYN_2]}

# Maps

# Dark Castle
MAPS_DARK_CASTLE = 'resources/maps/dark_castle/map.png'

MAPS_POS_DARK_CASTLE_INTERSECTION_TOP = 'resources/maps/dark_castle/intersection_top_path.png'
MAPS_POS_DARK_CASTLE_INTERSECTION_BOTTOM = 'resources/maps/dark_castle/intersection_bottom_path.png'
MAPS_POS_DARK_CASTLE_TOP_LEFT_MAIN_ROAD = 'resources/maps/dark_castle/top_left_main_road.png'

MAPS_ROUND_DARK_CASTLE_4 = 'resources/maps/dark_castle/round_4.png'  # 23
MAPS_ROUND_DARK_CASTLE_20 = 'resources/maps/dark_castle/round_20.png'  # 163

# Hotkeys
HOTKEY_UPGRADE_1 = ','
HOTKEY_UPGRADE_2 = '.'
HOTKEY_UPGRADE_3 = '/'
HOTKEY_UPGRADES = [HOTKEY_UPGRADE_1, HOTKEY_UPGRADE_2, HOTKEY_UPGRADE_3]

HOTKEY_HERO = 'u'
HOTKEY_TOWER_NINJA = 'd'
HOTKEY_TOWER_SUPER_MONKEY = 's'
