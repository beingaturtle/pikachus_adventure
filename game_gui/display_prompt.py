import pygame

def display_prompt(pygame_screen) -> str:
    """
    Display a prompt with choices and return the user's selection.

    :param pygame_screen: The pygame screen object
    :return: The user's selection as a string
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
