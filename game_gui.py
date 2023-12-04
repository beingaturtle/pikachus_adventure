"""
Ian Chan A00910012
Edro Gonzales A01257468
"""
import pygame
import sys
from game import get_name, generate_character_info

pygame.init()

# create constants and set up screen and movement
SCREEN_WIDTH = 925
SCREEN_HEIGHT = 925
GRID_SIZE = 11
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE
clock = pygame.time.Clock()
player_width = 0
player_column = 0
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

pygame.display.set_caption("Pikachu's Adventure!")

# character size control
walkRight = [
    pygame.transform.scale(pygame.image.load('images/character/R1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load('images/character/R2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
]
walkLeft = [
    pygame.transform.scale(pygame.image.load('images/character/L1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load('images/character/L2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
]
walkUp = [
    pygame.transform.scale(pygame.image.load('images/character/U1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load('images/character/U2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
]
walkDown = [
    pygame.transform.scale(pygame.image.load('images/character/D1.png'), (PLAYER_WIDTH, PLAYER_HEIGHT)),
    pygame.transform.scale(pygame.image.load('images/character/D2.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
]

charRight = pygame.transform.scale(pygame.image.load('images/character/Rstill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
charLeft = pygame.transform.scale(pygame.image.load('images/character/Lstill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
charUp = pygame.transform.scale(pygame.image.load('images/character/Ustill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))
charDown = pygame.transform.scale(pygame.image.load('images/character/Dstill.png'), (PLAYER_WIDTH, PLAYER_HEIGHT))

# direction character is facing
facing_left = False
facing_right = False
facing_up = False
facing_down = False

# character
player = pygame.Rect((player_width, player_column, PLAYER_WIDTH, PLAYER_HEIGHT))

# character_info
character_info = ""


def draw_character():
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


def redraw_window():
    # update background and draw grid
    screen.fill((0, 0, 0))
    for row in range(GRID_SIZE):
        for height in range(GRID_SIZE):
            pygame.draw.rect(screen, (255, 255, 255),
                             (row * CELL_SIZE, height * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    draw_character()  # draw the character

    pygame.display.update()


def show_intro_screen():
    global character_info  # Add this line to use the global variable

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
            name_text = intro_text_font.render(character_info['name'], True, (255, 0, 0))
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


def game_quit():
    global game_run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_run = False


def movement():
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
    elif down and player[1] < SCREEN_HEIGHT - PLAYER_HEIGHT:
        player.move_ip(0, SPEED)
        walkCount += 1


def key_handle():
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


def main():
    global game_run
    global character_info

    # get the user's name using the function from game.py
    trainer_name = get_name()

    # generate character information using the function from game.py
    character_info = generate_character_info(trainer_name)

    show_intro_screen()  # Remove the argument here

    while game_run:
        clock.tick(40)

        game_quit()
        key_handle()
        movement()

        redraw_window()

    pygame.quit()


if __name__ == '__main__':
    pygame.init()
    main()
