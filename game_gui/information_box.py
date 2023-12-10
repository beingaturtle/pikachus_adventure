"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import pygame
from pygame import Surface, Rect
from utils.display_pikachu_stats import display_pikachu_stats
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def information_box(character_status: dict, screen: Surface, player: Rect) -> None:
    """
    Displays an informative box at the bottom of the screen to show Pikachu's status.

    :param character_status: a non-empty dictionary
    :param screen: pygame screen object where the name will be inputted and displayed
    :param player: pygame player object representing the character location
    :precondition: character_status must be a non-empty dictionary that represents Pikachu's status
    :precondition: screen must be a pygame screen object
    :precondition: player must be a pygame player object representing the character location
    :postcondition: display an informative box at the bottom of the screen to show Pikachu's status
    """
    pygame.draw.rect(screen, (255, 255, 204), (0, 925, SCREEN_WIDTH, SCREEN_HEIGHT - 925))
    display_pikachu_stats(screen, player, character_status)

    pygame.display.update()
