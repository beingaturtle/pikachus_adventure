"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import pygame


def game_quit() -> bool:
    """
    Exit the game by closing the window or pressing the Escape key.

    :postcondition: exit the game after closing the window or pressing the Escape key
    :return: False if the window is closed or the Escape key is pressed, True otherwise
   """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
