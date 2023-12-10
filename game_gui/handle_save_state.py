"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
from pygame import Surface, Rect
import pygame
import os
import json


def display_save_prompt(pygame_screen: Surface) -> str:
    """
    Display a prompt for saving the current state of character.

    :param pygame_screen: a pygame object representing the screen
    :precondition: pygame_screen is a pygame object representing the screen
    :postcondition: display a prompt for saving the current state of character
    :return: the user's selection as a string
    """
    font = pygame.font.Font(None, 36)
    text = font.render("Save game? Press 1 for Yes, 2 for No", True, (255, 255, 255))
    pygame_screen.blit(text, (100, 100))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "1"
                elif event.key == pygame.K_2:
                    return "2"


def handle_save_state(screen: Surface, player: Rect, character_info: dict) -> None:
    """
    Save the state of the character.

    :param screen: pygame.Surface object containing information regarding the gameplayer
    :param player: pygame.Rect object representing the character within the pygame model
    :param character_info: character_info object containing information about the character
    :precondition: screen is provided during the gameplay
    :precondition: character_info is a dictionary containing information about character
    :postcondition: character_info is snapshotted and stored into the relevant json file
    """
    if display_save_prompt(screen) == "1":
        character_info["health"] = 100
        saved_directory_path = os.path.join(os.path.dirname(__file__), '..', 'saved')
        file_name = os.path.join(saved_directory_path, f"{character_info['name']}_info.json")
        with open(file_name, "w") as file_object:
            json.dump(character_info, file_object)
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Your health has been restored and your information saved.", True, (255, 255, 255))
        screen.blit(text, (100, 100))
        pygame.display.update()
        pygame.time.delay(1500)

    player.left -= 10
    player.top += 10
