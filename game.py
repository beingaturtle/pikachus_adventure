"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import sys
import pygame

from utils.get_name import get_name
from utils.user_has_file import user_has_file
from utils.generate_character_info import generate_character_info
from utils.state_machine import state_machine
from utils.get_save_file import get_save_file
from game_gui.show_intro_screen import show_intro_screen
from game_gui.drawing import redraw_window
from game_gui.game_quit import game_quit
from game_gui.key_handle import key_handle
from game_gui.movement import movement
from game_gui.load_character_images import load_character_images
from game_gui.handle_save_state import handle_save_state
from game_gui.boundaries import (check_and_adjust_collision, boundary_top, boundary_middle, boundary_bottom,
                                 boundary_left, boundary_right)
from game_gui.display_prompt import display_prompt
from game_gui.flee import flee
from game_gui.battle import battle
from game_gui.direction_subtract_coordinate import direction_subtract_coordinate
from game_gui.display_boss_prompt import display_boss_prompt

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT


def handle_boss_state(screen, player, character_info, facing_left, facing_right, facing_up, facing_down):
    # TODO: boss_fight logic
    choice = display_boss_prompt(screen)
    enemy = {
        "health": 100,
        "attack_power": 110
    }

    directions = {
        'left': facing_left,
        'right': facing_right,
        'up': facing_up,
        'down': facing_down
    }
    direction = next((key for key, value in directions.items() if value), '')

    if choice == '1':

        battle(screen, character_info, enemy)

        direction_subtract_coordinate(player, direction)
    else:
        flee(screen)

        direction_subtract_coordinate(player, direction)


def handle_encounter_state(screen):
    # TODO: encounter logic
    display_prompt(screen, "encounter_status")


def handle_end_game_loss_state(_):
    # TODO: end game loss logic
    return


def handle_end_game_victory_state(_):
    # TODO: end game victory logic
    return


def main():
    """Drive the program"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
    boundaries = [boundary_top(screen), boundary_middle(screen), boundary_bottom(screen), boundary_left(screen),
                  boundary_right(screen)]
    pygame.display.set_caption("Pikachu's Adventure!")
    clock = pygame.time.Clock()

    walk_left, walk_right, walk_up, walk_down, char_right, char_left, char_up, char_down = load_character_images()

    walk_count = 0
    facing_left = facing_right = facing_up = facing_down = False
    game_run = True

    try:
        trainer_name = get_name(screen)
        user_has_profile = user_has_file(trainer_name)
        character_info = generate_character_info(trainer_name) if not user_has_profile else get_save_file(trainer_name)
    except ValueError as e:
        print("Invalid Input: {}\nExiting by returning None".format(e), file=sys.stderr)
        return None

    player = pygame.Rect(character_info['coordinates'][0], character_info['coordinates'][1], PLAYER_WIDTH,
                         PLAYER_HEIGHT)

    show_intro_screen(character_info['name'], screen, clock)

    while game_run:
        clock.tick(40)

        game_run = game_quit()
        left, right, up, down = key_handle()
        walk_count += movement(player, left, right, up, down)

        character_args = (
            walk_count, facing_left, facing_right, facing_up, facing_down, left, right, up, down, walk_left, walk_right,
            walk_up, walk_down, char_right, char_left, char_up, char_down)
        walk_count, facing_left, facing_right, facing_up, facing_down = redraw_window(character_info, screen, player,
                                                                                      *character_args)

        for boundary_rect in boundaries:
            check_and_adjust_collision(player, boundary_rect, left, right, up, down)

        state_status = state_machine(player, character_info)
        print("state_status: ", state_status)

        if state_status == "boss_state":
            handle_boss_state(screen, player, character_info, facing_left, facing_right, facing_up, facing_down)
        elif state_status == "save_state":
            handle_save_state(screen, player, character_info)
        elif state_status == "encounter_status":
            handle_encounter_state(screen)
        elif state_status == "end_game_loss":
            handle_end_game_victory_state(screen)
        elif state_status == "end_game_victory":
            handle_end_game_victory_state(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
