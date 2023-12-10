import pygame
from pygame import Rect


def direction_subtract_coordinate(player: Rect, direction: str) -> None:
    """
    Subtract the coordinate of the player based on the direction it is facing by 10 pixels.

    :param player: a pygame object representing the player
    :param direction: a string representing the direction the player is facing
    :precondition: player must be a pygame object representing the player
    :precondition: drawn_character must be a pygame object that draws the player
    :postcondition: player's coordinate is subtracted by 10 pixels based on the direction it is facing
    >>> character = pygame.Rect(0, 0, 10, 10)
    >>> direction_subtract_coordinate(character, 'left')
    >>> character
    <rect(10, 0, 10, 10)>

    >>> character = pygame.Rect(0, 10, 15, 15)
    >>> direction_subtract_coordinate(character, 'up')
    >>> character
    <rect(0, 20, 15, 15)>
    """
    if direction == 'left':
        player.left += 10
    elif direction == 'right':
        player.right -= 10
    elif direction == 'up':
        player.top += 10
    elif direction == 'down':
        player.bottom -= 10
