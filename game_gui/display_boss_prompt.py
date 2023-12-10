"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import sys
import pygame
from pygame import Surface


def display_boss_prompt(pygame_screen: Surface, current_boss: dict) -> str:
    """
    Displays a message from the boss and prompts the user to fight or not.

    :param pygame_screen: a pygame screen object
    :param current_boss: the current boss is the boss that the user is currently facing
    :precondition: pygame_screen must be a pygame screen object
    :precondition: current_boss must be a non-empty dictionary containing information about the current boss
    :postcondition: displays a message from the boss and prompts the user to fight or not
    :return: a string representing the user's choice
    """
    font = pygame.font.Font(None, 36)

    if current_boss['name'] == "Trainer Edro Gonzales":
        text = font.render("Name's Pedro without the P. You dare to fight? Press 1 for Yes, 2 for No",
                           True, (255, 255, 255))
    elif current_boss['name'] == "Trainer Ian Chan":
        text = font.render("It is I, Ian. You will lose if you try to fight me. Press 1 for Yes, 2 for No",
                           True, (255, 255, 255))
    elif current_boss['name'] == "Trainer Richard M":
        text = font.render("I am Richard and I will destroy you. Press 1 for Yes, 2 for No", True,
                           (255, 255, 255))
    elif current_boss['name'] == "Trainer Chris Thompson":
        text = font.render("I'm Chris, let me make a cup of tea before I quiz you. Press 1 for Yes, 2 for No",
                           True, (255, 255, 255))
    else:
        text = font.render("You have defeated all the bosses. You win!", True, (255, 255, 255))
    pygame_screen.blit(text, (20, 100))
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
