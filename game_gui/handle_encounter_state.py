import random
from pygame import Surface
from itertools import cycle
from game_gui.display_prompt import display_prompt
from game_gui.battle import battle
from game_gui.flee import flee
from utils.create_encounter_enemy import create_encounter_enemy


def handle_encounter_state(screen: Surface, character_info: dict):
    """
    Handles the encounter logic of the gameplay.

    :param screen: pygame.Surface type representing the view of the game
    :param character_info: dictionary representing character information
    :precondition: screen must be passed in during live gameplay
    :precondition: character_info is a dictionary representing the character's health and other info
    :postcondition: provides user the choice to fight or flee from a fight
    :postcondition: user at any time can flee from the fight or attack
    :postcondition: modifies the character_info to reflect attack trade from enemy
    :postcondition: if health of the enemy is <= 0 then character gains experience
    :postcondition: character may be able to pick up a key after victory
    :postcondition: if character is below 0 hp in the fight, then the game will exit
    """
    encounter_enemy = create_encounter_enemy()

    choice = display_prompt(screen, f"A {encounter_enemy['name']} is challenging you to a duel. You can choose to fight for flee? Press 1 for fight, 2 for flee", 22)
    if choice == "1":
        battle(screen, character_info, encounter_enemy)
    else:
        flee(screen)

