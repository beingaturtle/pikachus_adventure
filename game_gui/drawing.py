import pygame
import os
from pygame import Surface, Rect
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game_gui.information_box import information_box
from game_gui.boundaries import boundary_top, boundary_middle, boundary_bottom, boundary_left, boundary_right


def redraw_window(character_info: dict, screen: Surface, player: Rect, current_boss_location: (int, int), *args: tuple
                  ) -> tuple:
    """
    Create a game board and refresh the display with an updated background during gameplay.

    :param character_info: a dictionary
    :param screen: a pygame.Surface object representing the game window
    :param player: a pygame.Rect object representing the player
    :param current_boss_location: tuple of two elements representing boss location
    :param args: positional arguments related to drawing objects on the screen
    :precondition: character_info must be a non-empty dictionary representing the character's information
    :precondition: screen must be a pygame object representing the game window
    :precondition: player must be a pygame object representing the player
    :precondition: current_boss_location must be a tuple of two x and y coordinates
    :precondition: args must be a series of arguments related to drawing objects on the screen
    :postcondition: create a game board and refresh the display with an updated background during gameplay
    """
    background_image_path = os.path.join(os.path.dirname(__file__), '..', 'images', 'background', 'background.png')
    background_image = pygame.image.load(background_image_path).convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    screen.blit(background_image, (0, 0))

    updated_args = draw_character(screen, player, *args)

    font = pygame.font.SysFont("", 100)
    hospital_text = font.render('B', True, (255, 255, 255))
    screen.blit(hospital_text, current_boss_location)

    font = pygame.font.SysFont("", 100)
    hospital_text = font.render('H', True, (255, 255, 255))
    screen.blit(hospital_text, (410, 25))

    (boundary_left(screen), boundary_right(screen), boundary_top(screen), boundary_middle(screen),
     boundary_bottom(screen))

    information_box(character_info, screen, player)

    return updated_args


def draw_character(screen: Surface, player: Rect, *args) -> tuple:
    """
    Draw the character on the screen based on the current state and direction it is facing.

    :param screen: a pygame object representing the game window
    :param player: a pygame object representing the player
    :param args: positional arguments related to drawing objects on the screen
    :precondition: screen must be a pygame object representing the game window
    :precondition: player must be a pygame object representing the player
    :precondition: args must be a series of arguments related to drawing character objects on the screen
    :postcondition: character is drawn on the screen facing north, south, east, or west
    """
    (walk_count, facing_left, facing_right, facing_up, facing_down, left, right, up, down, walk_left, walk_right,
     walk_up, walk_down, char_right, char_left, char_up, char_down) = args

    if walk_count >= 12:
        walk_count = 0

    if left:
        screen.blit(walk_left[walk_count // 6], (player[0], player[1]))
        facing_left = True
        facing_right = facing_up = facing_down = False
    elif right:
        screen.blit(walk_right[walk_count // 6], (player[0], player[1]))
        facing_right = True
        facing_left = facing_up = facing_down = False
    elif up:
        screen.blit(walk_up[walk_count // 6], (player[0], player[1]))
        facing_up = True
        facing_left = facing_right = facing_down = False
    elif down:
        screen.blit(walk_down[walk_count // 6], (player[0], player[1]))
        facing_down = True
        facing_left = facing_right = facing_up = False
    else:
        if facing_right:
            screen.blit(char_right, (player[0], player[1]))
        elif facing_left:
            screen.blit(char_left, (player[0], player[1]))
        elif facing_up:
            screen.blit(char_up, (player[0], player[1]))
        elif facing_down:
            screen.blit(char_down, (player[0], player[1]))
        else:
            screen.blit(char_right, (player[0], player[1]))

    walk_count += 1

    return walk_count, facing_left, facing_right, facing_up, facing_down
