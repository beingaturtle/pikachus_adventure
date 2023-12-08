import pygame
from constants import CELL_SIZE


def is_player_on_target_square(player, target_row, target_column):
    """
    Determines if the player has detected collisions.

    :param player: a pygame object representing the player
    :param target_row: the target row index as an integer
    :param target_column: the target column index as an integer
    :precondition: values provided are by pygame.Rect objects during live game
    :postcondition: determines if the player has detected collisions
    :return: true if the player is on the target square, otherwise False
    """
    target_x = target_row * CELL_SIZE
    target_y = target_column * CELL_SIZE
    return player.colliderect(pygame.Rect(target_x, target_y, CELL_SIZE, CELL_SIZE))
