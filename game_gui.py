"""
Ian Chan A00910012
Edro Gonzales A01257468
"""
import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Pikachu's Adventure!")

walkRight = [pygame.image.load('images/character/R1.png'), pygame.image.load('images/character/R2.png')]
walkLeft = [pygame.image.load('images/character/L1.png'), pygame.image.load('images/character/L2.png')]
walkUp = [pygame.image.load('images/character/U1.png'), pygame.image.load('images/character/U2.png')]
walkDown = [pygame.image.load('images/character/D1.png'), pygame.image.load('images/character/D2.png')]

charRight = pygame.image.load('images/character/Rstill.png')
charLeft = pygame.image.load('images/character/Lstill.png')
charUp = pygame.image.load('images/character/Ustill.png')
charDown = pygame.image.load('images/character/Dstill.png')

clock = pygame.time.Clock()
player_width = 0
player_column = 0
PLAYER_WIDTH = 24
PLAYER_HEIGHT = 24
SPEED = 2
left = False
right = False
up = False
down = False
walkCount = 0

# Direction character is facing
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

    # pygame.draw.rect(screen, (255, 0, 0), player)

    pygame.display.update()


# main_loop
run = True
while run:
    clock.tick(50)

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