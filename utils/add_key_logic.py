import random
import pygame
from pygame import Surface


def add_key_logic(screen: Surface, character: dict):
    """
    Add key to character.

    :param screen: pygame.Surface object containing gameplay
    :param character: dictionary containing character stats information
    :precondition: pygame.Surface is provided live gameplay
    :precondition: character dictionary contains character stats information
    :postcondition: rolls for a 70% chance to see if user earns a key from fight
    :postcondition: updates character information if they got a key
    :postcondition: displays message on pygame display for is user got a key or not
    """
    font = pygame.font.Font(None, 36)
    has_key = random.random() < 0.40
    key_increment = 1 if has_key else 0
    character["keys"] += key_increment
    key_message = "You have earned a key" if has_key else "You were not able to find a key"
    text = font.render(key_message, True, (255, 255, 255))
    screen.blit(text, (10, 80))