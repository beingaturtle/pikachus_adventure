from pygame import Surface
from game_gui.display_prompt import display_prompt


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
    choice = display_prompt(screen, "A magikarp is challenging you to a duel. You can choose to fight for flee? Press 1 for fight, 2 for flee")

