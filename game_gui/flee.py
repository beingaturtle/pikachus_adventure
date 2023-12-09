"""
ADD A DOCSTRING
"""
import pygame


def flee(screen, player) -> None:
    font = pygame.font.Font(None, 36)
    text = font.render("You ran away safely!", True, (255, 255, 255))
    screen.blit(text, (100, 100))
    pygame.display.update()
    pygame.time.delay(2000)
    player.left -= 10


def main():
    pass


if __name__ + "__main__":
    main()
