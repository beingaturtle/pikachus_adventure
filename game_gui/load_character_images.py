import pygame
from constants import PLAYER_WIDTH, PLAYER_HEIGHT

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
