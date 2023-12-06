import pygame
import re

def get_name(screen) -> str:
    """
    Gets the name of the user within a Pygame window.

    :param screen: Pygame screen object where the name will be inputted and displayed.
    :postcondition: user is prompted for username in the Pygame window.
    :postcondition: checks if username has anything besides numbers, letters, hyphens, and underscores.
    :return: string representing the typed username of user.
    :raise ValueError: if username has anything besides numbers, letters, hyphens, and underscores.
    """

    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if not re.match(r'^[a-zA-Z\d_-]+$', text):
                            raise ValueError("Name must not have any spaces and contain only letters, numbers, underscores '_', or hyphens '-'")
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((255, 255, 255))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

    return text
