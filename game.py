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
from utils.get_save_file import get_save_file
from game_gui.display_prompt import display_prompt
from game_gui.show_intro_screen import show_intro_screen
from game_gui.drawing import redraw_window
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, PLAYER_WIDTH, PLAYER_HEIGHT, SPEED

def load_character_images():
    """
    Load and scale character images for various movements.

    :return: a tuple containing lists of Pygame surfaces for each direction
    """
    walk_left = [
        pygame.transform.scale(pygame.image.load('./images/character/L1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
        pygame.transform.scale(pygame.image.load('./images/character/L2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
    ]
    walk_right = [
        pygame.transform.scale(pygame.image.load('./images/character/R1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
        pygame.transform.scale(pygame.image.load('./images/character/R2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
    ]
    walk_up = [
        pygame.transform.scale(pygame.image.load('./images/character/U1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
        pygame.transform.scale(pygame.image.load('./images/character/U2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
    ]
    walk_down = [
        pygame.transform.scale(pygame.image.load('./images/character/D1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
        pygame.transform.scale(pygame.image.load('./images/character/D2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
    ]
    char_right = pygame.transform.scale(pygame.image.load('./images/character/Rstill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
    char_left = pygame.transform.scale(pygame.image.load('./images/character/Lstill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
    char_up = pygame.transform.scale(pygame.image.load('./images/character/Ustill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
    char_down = pygame.transform.scale(pygame.image.load('./images/character/Dstill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))

    return walk_left, walk_right, walk_up, walk_down, char_right, char_left, char_up, char_down

def game_quit():
    """
    Exit the game by closing the window or pressing the Escape key.

    :postcondition: exit the game after closing the window or pressing the Escape key
   """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def movement(player, left, right, up, down):
    """
    Update the character position based on movement keys.

    :param player: a pygame.Rect object representing the player
    :param left: boolean indicating movement to the left
    :param right: boolean indicating movement to the right
    :param up: boolean indicating movement upwards
    :param down: boolean indicating movement downwards
    :precondition: left right up down should be booleans indicative of player direction
    :postcondition: character position updated based on movement keys
    :return: the walk count as an integer
    """
    walk_count = 0
    if left and player[0] > SPEED - SPEED * 2:
        player.move_ip(-SPEED, 0)
        walk_count += 1
    elif right and player[0] < SCREEN_WIDTH - PLAYER_WIDTH + SPEED:
        player.move_ip(SPEED, 0)
        walk_count += 1
    elif up and player[1] > SPEED - SPEED:
        player.move_ip(0, -SPEED)
        walk_count += 1
    elif down and player[1] < 925 - PLAYER_HEIGHT:
        player.move_ip(0, SPEED)
        walk_count += 1
    return walk_count

def key_handle():
    """
    Processes keyboard input to determine movement direction.

    :return: A tuple of booleans left, right, up, down indicating the movement direction
    """
    keys = pygame.key.get_pressed()
    left = keys[pygame.K_a] or keys[pygame.K_LEFT]
    right = keys[pygame.K_d] or keys[pygame.K_RIGHT]
    up = keys[pygame.K_w] or keys[pygame.K_UP]
    down = keys[pygame.K_s] or keys[pygame.K_DOWN]
    return left, right, up, down

def is_player_on_target_square(player, target_row, target_column):
    """
    Determines if the player has detected collisions.

    :param player: a pygame.Rect object representing the player
    :param target_row: the target row index as an integer
    :param target_column: the target column index as an integer
    :precondition: values provided are by pygame.Rect objects during live game
    :postcondition: determines if the player has detected collisions
    :return: true if the player is on the target square, otherwise False
    """
    target_x = target_row * CELL_SIZE
    target_y = target_column * CELL_SIZE
    return player.colliderect(pygame.Rect(target_x, target_y, CELL_SIZE, CELL_SIZE))

def main():
    """Drive the program"""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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

    target_row, target_column, prompt_shown = 5, 5, False

    while game_run:
        clock.tick(40)

        game_run = game_quit()
        left, right, up, down = key_handle()
        walk_count += movement(player, left, right, up, down)

        character_args = (walk_count, facing_left, facing_right, facing_up, facing_down, left, right, up, down, walk_left, walk_right, walk_up, walk_down, char_right, char_left, char_up, char_down)
        walk_count, facing_left, facing_right, facing_up, facing_down = redraw_window(character_info, screen, player, *character_args)

        if is_player_on_target_square(player, target_row, target_column) and not prompt_shown:
            display_prompt(screen)
            prompt_shown = True
        elif not is_player_on_target_square(player, target_row, target_column):
            prompt_shown = False

    pygame.quit()

if __name__ == '__main__':
    main()
