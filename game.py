"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import sys
import pygame

from utils.display_pikachu_stats import display_pikachu_stats
from utils.get_name import get_name
from utils.user_has_file import user_has_file
from utils.generate_character_info import generate_character_info
from utils.get_save_file import get_save_file

# create constants and set up screen and movement
SCREEN_WIDTH = 925
SCREEN_HEIGHT = 1050
GRID_SIZE = 11
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
clock = pygame.time.Clock()
PLAYER_WIDTH = 48
PLAYER_HEIGHT = 48
SPEED = 6
left = False
right = False
up = False
down = False
walkCount = 0
game_run = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# window title
pygame.display.set_caption("Pikachu's Adventure!")

# character image and size control
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

# direction character is facing
facing_left = False
facing_right = False
facing_up = False
facing_down = False

# establish character
player = None

def draw_character() -> None:
    """
    Draw the character on the screen based on the current state and direction it is facing.

    postcondition: character is drawn on the screen facing north, south, east, or west

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
    information_box(character_info)  # draw a rectangle to give more information like status, health, etc.

    pygame.display.update()

def show_intro_screen(trainer_name: str) -> None:
    """
    Display the introductory screen with a welcome message, game rules, and informs user to proceed with the game.

    :param trainer_name: a non-empty dictionary
    :precondition: character_info is a non-empty dictionary containing the user character information
    :precondition: character_info dictionary must contain a name key
    :postcondition: display a welcome message, game rules, and informs user to proceed with the game
    """
    intro_text_font = pygame.font.Font(None, 28)

    show_rules_screen = True

    while show_rules_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # transition to the main game loop when any key is pressed
                show_rules_screen = False

        screen.fill((0, 0, 0))

        if show_rules_screen:
            # rules screen
            welcome_text = intro_text_font.render("Welcome, ", True, (255, 255, 255))
            name_text = intro_text_font.render(trainer_name, True, (255, 0, 0))
            rules_lines = [
                "Here are some rules:",
                "- You may use WASD keys or arrow keys for movement.",
                "- You will see a hospital, where you can recover your HP and save your game.",
                "- To move onto the next area, you will need to collect keys by beating",
                " wild Pokemon. When you win a battle, you will get a chance of receiving a key.",
                "- Beat all the trainers by collecting keys and leveling up your Pikachu and",
                "attempt to beat the champion!",
                "",
                "",
                "Press any key to continue..."
            ]

            # Display "Welcome, " and the user's name
            screen.blit(welcome_text, (50, 80))
            screen.blit(name_text, (50 + welcome_text.get_width(), 80))

            for line_index, line in enumerate(rules_lines):
                if "Press any key to continue..." in line:
                    rules_text = intro_text_font.render(line, True, (28, 10, 194))
                else:
                    rules_text = intro_text_font.render(line, True, (255, 255, 255))

                screen.blit(rules_text, (50, 50 + (line_index + 2) * 50))  # Adjust the margin between each line

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)

def game_quit() -> None:
    """
    Exit the game by closing the window or pressing the Escape key.

    :postcondition: exits the game after closing the window or pressing the Escape key
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


   Handle keyboard input to update movement flags for the game character.

    This function checks for pressed keys using `pygame.key.get_pressed()` and updates
    global movement flags (`left`, `right`, `up`, `down`) accordingly. If keys
    corresponding to left, right, up, or down movement are pressed, the respective flag
    is set to True, and all other movement flags are set to False. If no movement keys
    are pressed, all movement flags are reset to False.

    :postcondition: receive keyboard input and update the movement of the character based on the pressed key
    :return:
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


TARGET_ROW = 5
TARGET_COLUMN = 5

def is_player_on_target_square() -> bool:
    """
    Check if the player is on the target square.

    :return: True if the player is on the target square, False otherwise.
    """
    target_x = TARGET_ROW * CELL_SIZE
    target_y = TARGET_COLUMN * CELL_SIZE
    return player.colliderect(pygame.Rect(target_x, target_y, CELL_SIZE, CELL_SIZE))

def display_prompt(pygame_screen) -> str:
    """
    Display a prompt with choices and return the user's selection.

    :param pygame_screen: The Pygame screen object.
    :return: The user's selection as a string.
    """
    font = pygame.font.Font(None, 36)
    choices = "Press 1 for Option A, 2 for Option B"
    text = font.render(choices, True, (255, 255, 255))
    pygame_screen.blit(text, (100, 100))
    pygame.display.update()

    choice = None
    while choice not in ['1', '2']:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choice = '1'
                elif event.key == pygame.K_2:
                    choice = '2'
    return choice


def information_box(character_status):
    pygame.draw.rect(screen, (255, 255, 204), (0, 925, SCREEN_WIDTH, SCREEN_HEIGHT - 925))
    display_pikachu_stats(screen, player, character_status)

    pygame.display.update()


def main():
    """Drives the program"""
    global game_run
    global player
    prompt_shown = False

    try:
        trainer_name = get_name(screen)
    except ValueError as e:
        print("Invalid Input: {}\nExiting by returning None".format(e), file=sys.stderr)
        return None

    user_has_profile = user_has_file(trainer_name)

    character_info = {}
    print("trainer_name", trainer_name)
    print("user_has_profile", user_has_profile)
    if not user_has_profile:
        character_info = generate_character_info(trainer_name)
    elif user_has_profile:
        character_info = get_save_file(trainer_name)

    player = pygame.Rect(
        (character_info['coordinates'][0], character_info['coordinates'][1], PLAYER_WIDTH, PLAYER_HEIGHT))

    show_intro_screen(character_info['name'])

    while game_run:
        clock.tick(40)

        game_quit()
        key_handle()
        movement()
        information_box(character_info)

        redraw_window(character_info)

        if is_player_on_target_square() and not prompt_shown:
            user_choice = display_prompt(screen)
            prompt_shown = True

        elif not is_player_on_target_square():
            prompt_shown = False
    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
