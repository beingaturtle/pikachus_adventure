"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import pygame
from pygame import Surface, Rect


def display_pikachu_stats(pygame_screen: Surface, player: Rect, character_info: dict) -> None:
    """
    Display Pikachu's current stats.

    :param pygame_screen: pygame screen object where the name will be inputted and displayed
    :param player: pygame rect object where the object represents Pikachu's coordinates and size
    :param character_info: a non-empty dictionary
    :precondition: pygame_screen must be a pygame screen object representing the game screen
    :precondition: player must be a pygame rect object representing Pikachu's coordinates and size
    :precondition: character_info must be a non-empty dictionary containing the user character information
    :postcondition: display Pikachu's current stats
    """
    font = pygame.font.Font(None, 25)
    # text = font.render(f"Pikachu's stats:", True, (0, 0, 0))
    # pygame_screen.blit(text, (10, 935))

    stats = [
        f"Coordinates: {player.x, player.y}",
        f"Health: {character_info['health']}",
        f"Level: {character_info['level']}",
        f"Skill: {character_info['skill']}",
        f"Number of Keys: {character_info['keys']}",
        f"Experience: {character_info['total_experience']}",
        f"Number of trainers to defeat: {4 - character_info['bosses_beaten']}"
    ]

    for index, stat in enumerate(stats):
        stat_text = font.render(stat, True, (0, 0, 0))
        pygame_screen.blit(stat_text, (10, 935 + index * 14))

    pygame.display.update()
