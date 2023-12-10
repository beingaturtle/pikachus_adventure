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


def display_only_message(pygame_screen: Surface, message: str):
    font = pygame.font.Font(None, 22)
    text = font.render(message,
                       True, (0, 0, 0))
    pygame_screen.blit(text, (250, 950))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return


def display_end_win_message(pygame_screen: Surface, message: str):
    pygame_screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 30)
    text = font.render(message,
                       True, (255, 255, 255))
    pygame_screen.blit(text, (100, 350))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                return
