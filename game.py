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
from utils.initialize_bosses import initialize_bosses
from game_gui.display_prompt import display_prompt
from game_gui.show_intro_screen import show_intro_screen
from game_gui.information_box import information_box
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, CELL_SIZE, PLAYER_WIDTH, PLAYER_HEIGHT, SPEED

walkCount = 0

left = False
right = False
up = False
down = False

game_run = True

facing_left = False
facing_right = False
facing_up = False
facing_down = False

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
clock = pygame.time.Clock()

pygame.display.set_caption("Pikachu's Adventure!")

walkRight = [
    pygame.transform.scale(pygame.image.load('./images/character/R1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load('./images/character/R2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
]
walkLeft = [
    pygame.transform.scale(pygame.image.load('./images/character/L1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load('./images/character/L2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
]
walkUp = [
    pygame.transform.scale(pygame.image.load('./images/character/U1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load('./images/character/U2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
]
walkDown = [
    pygame.transform.scale(pygame.image.load('./images/character/D1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load('./images/character/D2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
]

charRight = pygame.transform.scale(pygame.image.load('./images/character/Rstill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
charLeft = pygame.transform.scale(pygame.image.load('./images/character/Lstill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
charUp = pygame.transform.scale(pygame.image.load('./images/character/Ustill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
charDown = pygame.transform.scale(pygame.image.load('./images/character/Dstill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))

def draw_character() -> None:
    """
    Draw the character on the screen based on the current state and direction it is facing.

    :postcondition: character is drawn on the screen facing north, south, east, or west
    """
    global walkCount
    global facing_left
    global facing_right
    global facing_up
    global facing_down

    # create character
    if walkCount >= 12:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount // 6], (player[0], player[1]))
        facing_left = True
        facing_right = facing_up = facing_down = False
    elif right:
        screen.blit(walkRight[walkCount // 6], (player[0], player[1]))
        facing_right = True
        facing_left = facing_up = facing_down = False
    elif up:
        screen.blit(walkUp[walkCount // 6], (player[0], player[1]))
        facing_up = True
        facing_left = facing_right = facing_down = False
    elif down:
        screen.blit(walkDown[walkCount // 6], (player[0], player[1]))
        facing_down = True
        facing_left = facing_right = facing_up = False
    else:
        if facing_right:
            screen.blit(charRight, (player[0], player[1]))
        elif facing_left:
            screen.blit(charLeft, (player[0], player[1]))
        elif facing_up:
            screen.blit(charUp, (player[0], player[1]))
        elif facing_down:
            screen.blit(charDown, (player[0], player[1]))
        else:
            screen.blit(charRight, (player[0], player[1]))

    walkCount += 1

    pygame.display.update()


def redraw_window(character_info) -> None:
    """
    Create a 11x11 game board and refresh the display with an updated background

    :postcondition: create a 11x11 game board and refresh the display with an updated background
    """
    screen.fill((0, 0, 0))
    for row in range(GRID_SIZE):
        for height in range(GRID_SIZE):
            pygame.draw.rect(screen, (255, 255, 255),
                             (row * CELL_SIZE, height * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    draw_character()  # draw the character
    information_box(character_info, screen, player)

    pygame.display.update()

def game_quit() -> None:
    """
    Exit the game by closing the window or pressing the Escape key.

    :postcondition: exit the game after closing the window or pressing the Escape key
    """
    global game_run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_run = False


def movement() -> None:
    """
    Update the character position based on movement keys.

    :postcondition: update character position based on movement keys
    """
    global left, right, up, down, player, walkCount

    # movement keys
    if left and player[0] > SPEED - SPEED * 2:
        player.move_ip(-SPEED, 0)
        walkCount += 1
    elif right and player[0] < SCREEN_WIDTH - PLAYER_WIDTH + SPEED:
        player.move_ip(SPEED, 0)
        walkCount += 1
    elif up and player[1] > SPEED - SPEED:
        player.move_ip(0, -SPEED)
        walkCount += 1
    elif down and player[1] < 925 - PLAYER_HEIGHT:
        player.move_ip(0, SPEED)
        walkCount += 1


def key_handle() -> None:
    """
    Receive keyboard input based on the pressed key to update movement for the character.


    :postcondition: receive keyboard input and update the movement of the character based on the pressed key
    """
    global left, right, up, down

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        left = True
        right = up = down = False
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        right = True
        left = up = down = False
    elif keys[pygame.K_w] or keys[pygame.K_UP]:
        up = True
        left = right = down = False
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        down = True
        left = right = up = False
    else:
        # reset all flags if no movement keys are pressed
        left = right = up = down = False


def is_player_on_target_square(target_row, target_column) -> bool:
    """
    Check if the player is on the target square.

    :return: True if the player is on the target square, otherwise, False
    """
    target_x = target_row * CELL_SIZE
    target_y = target_column * CELL_SIZE
    return player.colliderect(pygame.Rect(target_x, target_y, CELL_SIZE, CELL_SIZE))

def main():
    """Drives the program"""
    global game_run
    global player
    target_row = 5
    target_column = 5
    prompt_shown = False

    try:
        trainer_name = get_name(screen)
    except ValueError as e:
        print("Invalid Input: {}\nExiting by returning None".format(e), file=sys.stderr)
        return None

    user_has_profile = user_has_file(trainer_name)

    character_info = {}
    if not user_has_profile:
        character_info = generate_character_info(trainer_name)
    elif user_has_profile:
        character_info = get_save_file(trainer_name)

    bosses = initialize_bosses()
    current_boss = bosses[character_info["bosses_beaten"]]
    boss_fight = False

    player = pygame.Rect(
        (character_info['coordinates'][0], character_info['coordinates'][1], PLAYER_WIDTH, PLAYER_HEIGHT))

    show_intro_screen(character_info['name'], screen, clock)

    while game_run:
        clock.tick(40)

        game_quit()
        key_handle()
        movement()
        information_box(character_info, screen, player)

        redraw_window(character_info)

        if is_player_on_target_square(target_row, target_column) and not prompt_shown:
            user_choice = display_prompt(screen)
            prompt_shown = True

        elif not is_player_on_target_square(target_row, target_column):
            prompt_shown = False
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
