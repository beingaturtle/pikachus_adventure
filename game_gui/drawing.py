import pygame
from pygame import Surface, Rect

from constants import GRID_SIZE, CELL_SIZE
from game_gui.information_box import information_box
from game_gui.boundaries import boundary_top, boundary_middle, boundary_bottom, boundary_left, boundary_right


def redraw_window(character_info: dict, screen: Surface, player: Rect, *args):
    """
    Create a 11x11 game board and refresh the display with an updated background during gameplay.

    :postcondition: create a 11x11 game board and refresh the display with an updated background during gameplay
    """
    screen.fill((0, 0, 0))
    for row in range(GRID_SIZE):
        for height in range(GRID_SIZE):
            pygame.draw.rect(screen, (255, 255, 255),
                             (row * CELL_SIZE, height * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    updated_args = draw_character(screen, player, *args)
    boundary_left(screen), boundary_right(screen), boundary_top(screen), boundary_middle(screen), boundary_bottom(screen)
    information_box(character_info, screen, player)

    pygame.display.update()
    return updated_args


def draw_character(screen, player, *args):
    """
    Draw the character on the screen based on the current state and direction it is facing.

    :postcondition: character is drawn on the screen facing north, south, east, or west
    """
    walk_count, facing_left, facing_right, facing_up, facing_down, left, right, up, down, walk_left, walk_right, walk_up, walk_down, char_right, char_left, char_up, char_down = args
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

    pygame.display.update()
    return walk_count, facing_left, facing_right, facing_up, facing_down
