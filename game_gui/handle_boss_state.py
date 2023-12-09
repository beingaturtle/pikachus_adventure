from game_gui.battle import battle
from game_gui.direction_subtract_coordinate import direction_subtract_coordinate
from game_gui.display_boss_prompt import display_boss_prompt
from game_gui.display_prompt import display_only_message
from game_gui.flee import flee
from utils.initialize_bosses import has_enough_keys


def handle_boss_state(screen, player, character_info, boss_info, facing_left, facing_right, facing_up, facing_down):

    current_boss = boss_info[character_info["bosses_beaten"]]

    directions = {
        'left': facing_left,
        'right': facing_right,
        'up': facing_up,
        'down': facing_down
    }
    direction = next((key for key, value in directions.items() if value), '')

    if has_enough_keys(character_info, current_boss):
        choice = display_boss_prompt(screen)

        if choice == '1':

            battle(screen, character_info, current_boss)

            direction_subtract_coordinate(player, direction)
        else:
            flee(screen)

            direction_subtract_coordinate(player, direction)
    else:
        boss_speech = f"{current_boss['name']}: You do not have enough keys to fight me. Press Enter to continue."
        display_only_message(screen, boss_speech)
        direction_subtract_coordinate(player, direction)