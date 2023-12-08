import pygame


def display_prompt(pygame_screen, state_status) -> str:
    """
    Display a prompt with choices and return the user's selection.

    :param pygame_screen: The pygame screen object
    :param state_status: The pygame screen object
    :return: The user's selection as a string
    """
    font = pygame.font.Font(None, 36)
    choices = f"{state_status}: Press 1 for Option A, 2 for Option B"
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

    pygame_screen.fill((0, 0, 0))
    pygame.display.flip()
    return choice


def flee(screen, choice, player):
    if choice == '2':
        font = pygame.font.Font(None, 36)
        text = font.render("You ran away safely!", True, (255, 255, 255))
        screen.blit(text, (100, 100))
        pygame.display.update()
        pygame.time.delay(2000)
        player.left -= 10


