"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
from pygame import Surface, Rect

from game_gui.battle import battle
from game_gui.direction_subtract_coordinate import direction_subtract_coordinate
from game_gui.display_boss_prompt import display_boss_prompt
from game_gui.display_prompt import display_only_message
from game_gui.flee import flee
from utils.initialize_bosses import has_enough_keys


def handle_boss_state(screen: Surface, player: Rect, character_info: dict, boss_info: dict, facing_left: dict,
                      facing_right: dict, facing_up: dict, facing_down: dict) -> None:
    """
    Control the boss state of the game.

    :param screen: a pygame Surface
    :param player: a pygame Rect
    :param character_info: a non-empty dictionary
    :param boss_info: a non-empty dictionary
    :param facing_left: a non-empty dictionary
    :param facing_right: a non-empty dictionary
    :param facing_up: a non-empty dictionary
    :param facing_down: a non-empty dictionary
    :precondition: screen must be a pygame Surface
    :precondition: player must be a pygame Rect
    :precondition: character_info must be a non-empty dictionary
    :precondition: boss_info must be a non-empty dictionary
    :precondition: facing_left must be a non-empty dictionary
    :precondition: facing_right must be a non-empty dictionary
    :precondition: facing_up must be a non-empty dictionary
    :precondition: facing_down must be a non-empty dictionary
    :postcondition: control the boss state of the game
    """

    current_boss = boss_info[character_info["bosses_beaten"]]

    directions = {
        'left': facing_left,
        'right': facing_right,
        'up': facing_up,
        'down': facing_down
    }
    direction = next((key for key, value in directions.items() if value), '')

    if has_enough_keys(character_info, current_boss):
        choice = display_boss_prompt(screen, current_boss)

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
