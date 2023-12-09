import sys
import pygame
from pygame import Surface


def display_boss_prompt(pygame_screen: Surface) -> str:
    """
    Display a prompt for saving the current state of character.

    :param pygame_screen: The pygame screen object
    :return: The user's selection as a string
    """
    font = pygame.font.Font(None, 36)
    text = font.render("You dare to challenge me? Press 1 for Yes, 2 for No", True, (255, 255, 255))
    pygame_screen.blit(text, (100, 100))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "1"
                elif event.key == pygame.K_2:
                    pygame_screen.fill((0, 0, 0))
                    pygame.display.flip()
                    return '2'

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
