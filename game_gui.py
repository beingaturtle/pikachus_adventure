"""
Ian Chan A00910012
Edro Gonzales A01257468
"""
import pygame
import sys

pygame.init()

# create constants and set up screen and movement
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
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


def redraw_window():
    global walkCount
    global facing_left
    global facing_right
    global facing_up
    global facing_down

    # update background
    screen.fill((0, 0, 0))

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


def show_intro_screen():
    intro_text_font = pygame.font.Font(None, 28)  # Adjust the font size if needed
    input_font = pygame.font.Font(None, 28)

    input_box = pygame.Rect(275, 450, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    input_prompt = True
    show_rules_screen = False

    while input_prompt or show_rules_screen:
        for game_start in pygame.event.get():
            if game_start.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if input_prompt and game_start.type == pygame.KEYDOWN:
                if active:
                    if game_start.key == pygame.K_RETURN:
                        # once the player presses 'Enter' key, transition to the main game loop
                        input_prompt = False
                        show_rules_screen = True
                    elif game_start.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += game_start.unicode

                elif game_start.key == pygame.K_RETURN:
                    # activate input box by pressing "Enter" key
                    active = not active
                    color = color_active if active else color_inactive

            elif show_rules_screen and game_start.type == pygame.KEYDOWN:
                # once the player presses any key on the rules screen, proceed to the main game loop
                show_rules_screen = False

        screen.fill((0, 0, 0))

        if input_prompt:
            # welcome text
            welcome_lines = [
                "Welcome to Pikachu's Adventure!",
                "You will start at the beginning where you will need to find keys to",
                "fight gym trainers. To find keys, you will encounter pokemon and must",
                "beat them to get a chance of getting an item. Progress through the",
                "entire map to fight the Pokemon Champion!"
            ]

            for line_index, line in enumerate(welcome_lines):
                welcome_text = intro_text_font.render(line, True, (255, 255, 255))
                screen.blit(welcome_text, (50, 100 + line_index * 50))  # Adjust the margin between each line

            instruction_text = intro_text_font.render("To read the rules, press your 'Enter' key and please input"
                                                      " your name.", True, (255, 255, 255))
            screen.blit(instruction_text, (50, 350))  # Adjust the position of text

            # Render the input box
            txt_surface = input_font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)

        elif show_rules_screen:
            # Rules screen
            rules_lines = [
                "Here are some rules:",
                "- You will see a hospital, where you can recover your HP and save your game.",
                "- To move onto the next area, you will need to collect keys by beating",
                " wild pokemon. When you win a battle, you will get a chance of receiving a key.",
                "- Beat all the trainers by collecting keys and leveling up your Pikachu and",
                "attempt to beat the champion!",
                "",
                "",
                "Press any key to continue..."
            ]

            for line_index, line in enumerate(rules_lines):
                rules_text = intro_text_font.render(line, True, (255, 255, 255))
                screen.blit(rules_text, (50, 50 + line_index * 50))  # Adjust the margin between each line

        pygame.display.flip()
        clock.tick(30)


# main_loop

show_intro_screen()

run = True
while run:
    clock.tick(40)

    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # handle key events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                left = True
                right = up = down = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                right = True
                left = up = down = False
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                up = True
                left = right = down = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                down = True
                left = right = up = False

        elif event.type == pygame.KEYUP:
            # reset the flags when the key is released
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                left = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                right = False
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                up = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                down = False

    # movement keys
    if left and player[0] > SPEED - SPEED:
        player.move_ip(-SPEED, 0)
        walkCount += 1
    elif right and player[0] < SCREEN_WIDTH - PLAYER_WIDTH + SPEED:
        player.move_ip(SPEED, 0)
        walkCount += 1
    elif up and player[1] > SPEED - SPEED:
        player.move_ip(0, -SPEED)
        walkCount += 1
    elif down and player[1] < SCREEN_HEIGHT - PLAYER_HEIGHT + SPEED:
        player.move_ip(0, SPEED)
        walkCount += 1

    redraw_window()

pygame.quit()
