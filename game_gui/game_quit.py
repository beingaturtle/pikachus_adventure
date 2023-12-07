import pygame

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