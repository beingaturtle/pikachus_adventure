"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import sys
import random
import pygame

from pygame import Rect
from utils.get_name import get_name
from utils.user_has_file import user_has_file
from utils.generate_character_info import generate_character_info
from utils.get_save_file import get_save_file
from game_gui.show_intro_screen import show_intro_screen
from game_gui.drawing import redraw_window
from game_gui.game_quit import game_quit
from game_gui.key_handle import key_handle
from game_gui.movement import movement
from game_gui.load_character_images import load_character_images
from game_gui.boundaries import (check_and_adjust_collision, boundary_top, boundary_middle, boundary_bottom,
                                 boundary_left, boundary_right)
from game_gui.display_prompt import display_prompt
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, CELL_SIZE

def is_collision(player, area):
    """
    Decides during gameplay if the user is a experiencing a collision.

    :param player: player is a pygame.Rect object and provides information on character in game
    :param area:
    :return:
    """
    return player.colliderect(pygame.Rect(area[0], area[1], CELL_SIZE, CELL_SIZE))

def state_machine(player: Rect, character_info: dict) -> str:
    """
    Determines the state of the game.

    :param player: pygame.Rect object
    :param character_info: dictionary object containing character information
    :precondition: player must be a pygame.Rect object that represents the info of the current character
    :postcondition: if player is moving around and not in any state return live_play
    :postcondition: if player is on a boss location then return boss state
    :postcondition: if player is on a hospital tile then return save state
    :postcondition: if player is on in a wild encounter then return wild encounter
    :postcondition: if player has beaten all the bosses then return end game victory
    :postcondition: if player has lost all health then return end game loss
    :return: string representing state of user
    """
    areas = {
        "save_state": [(410, 25)],
        "boss_state": [(441, 188), (668, 422), (442, 633), (38, 829)],
    }

    for state, area_list in areas.items():
        for area in area_list:
            if is_collision(player, area):
                return state

    if random.random() < 0.01:
        return "encounter_status"

    elif character_info["bosses_beaten"] == 4:
        return "end_game_victory"
    elif character_info["health"] <= 0:
        return "end_game_loss"

    return "live_game"

def handle_boss_state(screen):
    # TODO: boss_fight logic
    display_prompt(screen, "boss_status")

def handle_save_state(screen):
    # TODO: hospital + save logic
    display_prompt(screen, "save_state")

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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    boundaries = [boundary_top(screen), boundary_middle(screen), boundary_bottom(screen), boundary_left(screen),
                  boundary_right(screen)]
    # boundaries
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

    player = pygame.Rect(character_info['coordinates'][0], character_info['coordinates'][1], PLAYER_WIDTH, PLAYER_HEIGHT)
    show_intro_screen(character_info['name'], screen, clock)

    while game_run:
        clock.tick(40)

        game_run = game_quit()
        left, right, up, down = key_handle()
        walk_count += movement(player, left, right, up, down)

        character_args = (walk_count, facing_left, facing_right, facing_up, facing_down, left, right, up, down, walk_left, walk_right, walk_up, walk_down, char_right, char_left, char_up, char_down)
        walk_count, facing_left, facing_right, facing_up, facing_down = redraw_window(character_info, screen, player, *character_args)

        for boundary_rect in boundaries:
            check_and_adjust_collision(player, boundary_rect, left, right, up, down)

        state_actions = {
            "boss_state": handle_boss_state,
            "save_state": handle_save_state,
            "encounter_state": handle_encounter_state,
            "end_game_loss_state": handle_end_game_loss_state,
            "end_game_victory_state": handle_end_game_victory_state
        }

        state_status = state_machine(player, character_info)

        if state_status in state_actions:
            state_actions[state_status](screen)

    pygame.quit()

if __name__ == '__main__':
    main()
