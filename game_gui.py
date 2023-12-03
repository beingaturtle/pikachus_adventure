"""
Ian Chan A00910012
Edro Gonzales A01257468
"""
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Pikachu's Adventure!")

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
player = pygame.Rect((0, 0, PLAYER_WIDTH, PLAYER_HEIGHT))

SPEED = 2


run = True
while run:
    pygame.time.delay(5)
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if (key[pygame.K_a] or key[pygame.K_LEFT]) and player[0] > SPEED:
        player.move_ip(-SPEED, 0)
    elif (key[pygame.K_d] or key[pygame.K_RIGHT]) and player[0] < SCREEN_WIDTH - PLAYER_WIDTH + SPEED:
        player.move_ip(SPEED, 0)
    elif (key[pygame.K_w] or key[pygame.K_UP]) and player[1] > SPEED:
        player.move_ip(0, -SPEED)
    elif (key[pygame.K_s] or key[pygame.K_DOWN]) and player[1] < SCREEN_HEIGHT - PLAYER_HEIGHT + SPEED:
        player.move_ip(0, SPEED)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
