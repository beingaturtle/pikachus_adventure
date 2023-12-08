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

def state_machine(player: Rect, character_info: dict) -> str:
    """
    Determines the state of the game.

    :param player: pygame.Rect object
    :param character_info: dictionary object containing character information
    :precondition: player must be a pygame.Rect object that represents the info of the current character
    :postcondition: if player is moving around and not in any state return live_play
    :postcondition: if player is on a boss location then return boss state
    :postcondition: if player is on a hospital tile then return save state
    :postcondition: if player is on in a wild encounter then return wild encounter
    :postcondition: if player has beaten all the bosses then return end game victory
    :postcondition: if player has lost all health then return end game loss
    :return: string representing state of user
    """
    areas = {
        "save_state": [(410, 25)],
        "boss_state": [(441, 188), (668, 422), (442, 633), (38, 829)],
    }

    for state, area_list in areas.items():
        for area in area_list:
            if is_collision(player, area):
                return state

    if random.random() < 0.01:
        return "encounter_status"

    elif character_info["bosses_beaten"] == 4:
        return "end_game_victory"
    elif character_info["health"] <= 0:
        return "end_game_loss"

    return "live_game"