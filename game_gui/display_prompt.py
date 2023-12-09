import sys
import pygame
from pygame import Surface


def display_prompt(pygame_screen: Surface, message: str, size: int = 32) -> str:
    """
    Display a prompt for saving the current state of character.

    :param pygame_screen: The pygame screen object
    :param message: string message to display
    :param size: int representing size of font
    :precondition: pygame_screen must be a pygame.Surface object provided during gameplay
    :precondition: message is a string to be displayed for the user
    :postcondition: grabs the choice from a user in the form of a key action event
    :postcondition: allows users to be able to quit from the game window
    :return: the user's selection as a string
    """
    font = pygame.font.Font(None, size)
    text = font.render(message,
                       True, (255, 255, 255))
    pygame_screen.blit(text, (100, 100))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "1"
                elif event.key == pygame.K_2:
                    return '2'

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
