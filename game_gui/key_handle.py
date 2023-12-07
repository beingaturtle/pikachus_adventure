import pygame

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
