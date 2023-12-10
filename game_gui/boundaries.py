import pygame
from pygame import Surface, Rect


def boundary_top(screen: Surface) -> pygame.Rect:
    """
    Draw the top boundary of the game board.

    :param screen: a pygame object representing the game window
    :precondition: screen must be a pygame object representing the game window
    :postcondition: draw the top boundary of the game board
    :return: a pygame object representing the top boundary of the game board
    >>> boundary_top_screen_first = pygame.display.set_mode((1280, 960))
    >>> boundary_top(boundary_top_screen_first)
    <rect(465, -5, 5, 193)>

    >>> boundary_top_screen_second = pygame.display.set_mode((800, 600))
    >>> boundary_top(boundary_top_screen_second)
    <rect(465, -5, 5, 193)>
    """
    boundary_x = 465
    boundary_y = -5
    boundary_height = 193
    boundary_length = 5

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (150, 75, 0), border)

    return border


def boundary_middle(screen: Surface) -> pygame.Rect:
    """
    Draw the middle boundary of the game board.

    :param screen: a pygame object representing the game window
    :precondition: screen must be a pygame object representing the game window
    :postcondition: draw the middle boundary of the game board
    :return: a pygame object representing the middle boundary of the game board
    >>> boundary_middle_screen_first = pygame.display.set_mode((1280, 960))
    >>> boundary_middle(boundary_middle_screen_first)
    <rect(465, 253, 5, 380)>

    >>> boundary_middle_screen_second = pygame.display.set_mode((800, 600))
    >>> boundary_middle(boundary_middle_screen_second)
    <rect(465, 253, 5, 380)>
    """
    boundary_x = 465
    boundary_y = 253
    boundary_height = 380
    boundary_length = 5

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (150, 75, 0), border)

    return border


def boundary_bottom(screen: Surface) -> pygame.Rect:
    """
    Draw the bottom boundary of the game board.

    :param screen: a pygame object representing the game window
    :precondition: screen must be a pygame object representing the game window
    :postcondition: draw the bottom boundary of the game board
    :return: a pygame object representing the bottom boundary of the game board
    >>> boundary_bottom_screen_first = pygame.display.set_mode((1280, 960))
    >>> boundary_bottom(boundary_bottom_screen_first)
    <rect(465, 693, 5, 234)>

    >>> boundary_bottom_screen_second = pygame.display.set_mode((800, 600))
    >>> boundary_bottom(boundary_bottom_screen_second)
    <rect(465, 693, 5, 234)>
    """
    boundary_x = 465
    boundary_y = 693
    boundary_height = 234
    boundary_length = 5

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (150, 75, 0), border)

    return border


def boundary_left(screen: Surface) -> pygame.Rect:
    """
    Draw the left boundary of the game board.

    :param screen: a pygame object representing the game window
    :precondition: screen must be a pygame object representing the game window
    :postcondition: draw the left boundary of the game board
    :return: a pygame object representing the left boundary of the game board
    >>> boundary_left_screen_first = pygame.display.set_mode((1280, 960))
    >>> boundary_left(boundary_left_screen_first)
    <rect(-8, 460, 676, 5)>

    >>> boundary_left_screen_second = pygame.display.set_mode((800, 600))
    >>> boundary_left(boundary_left_screen_second)
    <rect(-8, 460, 676, 5)>
    """
    boundary_x = -8
    boundary_y = 460
    boundary_length = 676
    boundary_height = 5

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (150, 75, 0), border)

    return border


def boundary_right(screen: Surface) -> pygame.Rect:
    """
    Draw the right boundary of the game board.

    :param screen: a pygame object representing the game window
    :precondition: screen must be a pygame object representing the game window
    :postcondition: draw the right boundary of the game board
    :return: a pygame object representing the right boundary of the game board
    >>> boundary_right_screen_first = pygame.display.set_mode((1280, 960))
    >>> boundary_right(boundary_right_screen_first)
    <rect(728, 460, 616, 5)>

    >>> boundary_right_screen_second = pygame.display.set_mode((800, 600))
    >>> boundary_right(boundary_right_screen_second)
    <rect(728, 460, 616, 5)>
    """
    boundary_x = 728
    boundary_y = 460
    boundary_length = 616
    boundary_height = 5

    border = pygame.Rect(boundary_x, boundary_y, boundary_length, boundary_height)

    pygame.draw.rect(screen, (150, 75, 0), border)

    return border


def check_and_adjust_collision(player: Rect, boundary_rect: Rect, left: bool, right: bool, up: bool, down: bool) -> \
        None:
    """
    Check if the player is colliding with a certain boundary and stop the player's movement from crossing the boundary.

    :param player: a pygame object representing the player
    :param boundary_rect: a pygame object representing the boundary
    :param left: a boolean representing if the player is moving left
    :param right: a boolean representing if the player is moving right
    :param up: a boolean representing if the player is moving up
    :param down: a boolean representing if the player is moving down
    :precondition: player must be a pygame object representing the player
    :precondition: boundary_rect must be a pygame object representing the boundary
    :precondition: left must be a boolean representing if the player is moving left
    :precondition: right must be a boolean representing if the player is moving right
    :precondition: up must be a boolean representing if the player is moving up
    :precondition: down must be a boolean representing if the player is moving down
    :postcondition: check if the player is colliding with a boundary and stop the player's movement from passing the
                    boundary
    >>> first_player = pygame.Rect(0, 0, 10, 10)
    >>> boundary_rectangle = pygame.Rect(0, 0, 10, 10)
    >>> check_and_adjust_collision(first_player, boundary_rectangle, True, False, False, False)
    >>> first_player
    <rect(10, 0, 10, 10)>

    >>> second_player = pygame.Rect(100, 100, 10, 10)
    >>> boundary_rectangle = pygame.Rect(100, 100, 10, 10)
    >>> check_and_adjust_collision(second_player, boundary_rectangle, False, False, False, True)
    >>> second_player
    <rect(100, 90, 10, 10)>
    """
    if player.colliderect(boundary_rect):
        if left:
            player.left = boundary_rect.right
        elif right:
            player.right = boundary_rect.left
        elif up:
            player.top = boundary_rect.bottom
        elif down:
            player.bottom = boundary_rect.top
