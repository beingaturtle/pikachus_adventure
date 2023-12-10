"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import pygame
from pygame import Surface


def flee(screen: Surface) -> None:
    """
    Displays a message to the user that they have successfully fled from the battle.

    :param screen: a pygame Surface object
    :precondition: screen must be a pygame Surface object
    :postcondition: displays a message to the user that they have successfully fled from the battle
    """
    font = pygame.font.Font(None, 36)
    text = font.render("You ran away safely!", True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text, (100, 100))
    pygame.display.update()
    pygame.time.delay(500)
