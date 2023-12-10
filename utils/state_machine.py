import pygame
import random
from pygame import Rect
from constants import CELL_SIZE

def is_collision(player, area):
    """
    Decides during gameplay if the user is experiencing a collision.

    :param player: player is a pygame.Rect object and provides information on character in game
    :param area: area is a tuple representing the location they are at
    :precondition: function being called during gameplay
    :precondition: player must be a pygame.Rect object
    :precondition: area is a tuple with x and y locations
    :postcondition: checks if player is within given rectangle and returns a boolean
    :return: True if player is within given rectangle and then False otherwise

    True
    """
    return player.colliderect(pygame.Rect(area[0], area[1], CELL_SIZE, CELL_SIZE))

def state_machine(player: Rect, character_info: dict, boss_info: tuple) -> str:
    """
    Determines the state of the game.

    :param player: pygame.Rect object
    :param character_info: dictionary object containing character information
    :param boss_info: tuple containing all boss information
    :precondition: player must be a pygame.Rect object that represents the info of the current character
    :postcondition: boss_info must be a tuple containing all boss information
    :postcondition: if player is moving around and not in any state return live_play
    :postcondition: if player is on a boss location then return boss state
    :postcondition: if player is on a hospital tile then return save state
    :postcondition: if player is on in a wild encounter then return wild encounter
    :postcondition: if player has beaten all the bosses then return end game victory
    :postcondition: if player has lost all health then return end game loss
    :return: string representing state of the user
    """
    if character_info["bosses_beaten"] == 4:
        return "end_game_victory"

    next_boss = character_info["bosses_beaten"]
    current_boss = boss_info[next_boss]
    boss_location = current_boss['coordinates']

    areas = {
        "save_state": (410, 25),
        "boss_state": boss_location,
    }

    for state, area_list in areas.items():
        if is_collision(player, area_list):
            return state

    if random.random() < 0.005:
        return "encounter_status"
    elif character_info["health"] <= 0:
        return "end_game_loss"

    return "live_game"