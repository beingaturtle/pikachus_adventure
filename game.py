"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import sys
import pygame

from game_gui.display_prompt import display_only_message, display_end_win_message  # will remove soon
from game_gui.handle_end_game_victory_state import handle_end_game_victory_state

from utils.get_name import get_name
from utils.initialize_bosses import initialize_bosses
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
from game_gui.handle_encounter_state import handle_encounter_state
from game_gui.handle_boss_state import handle_boss_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT


def handle_end_game_loss_state(_):
    # TODO: end game loss logic
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
    boss_info = initialize_bosses()

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

        for boundary_rect in boundaries:
            check_and_adjust_collision(player, boundary_rect, left, right, up, down)

        state_status = state_machine(player, character_info, boss_info)

        if state_status == "end_game_victory":
            handle_end_game_victory_state(screen, character_info, screen)

        current_boss_location = tuple(boss_info[character_info["bosses_beaten"]]["coordinates"])

        walk_count, facing_left, facing_right, facing_up, facing_down = redraw_window(character_info, screen, player,
                                                                                      current_boss_location,
                                                                                      *character_args)

        if state_status == "boss_state":
            handle_boss_state(screen, player, character_info, boss_info, facing_left, facing_right, facing_up,
                              facing_down)
        elif state_status == "save_state":
            handle_save_state(screen, player, character_info)
        elif state_status == "encounter_status":
            handle_encounter_state(screen, character_info)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
