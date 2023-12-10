"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import pygame
import sys
from pygame import Surface
from pygame.time import Clock


def show_intro_screen(trainer_name: str, screen: Surface, clock: Clock) -> None:
    """
    Display the introductory screen with a welcome message, game rules, and informs user to proceed with the game.

    :param trainer_name: a string
    :param screen: pygame screen object where the name will be inputted and displayed
    :param clock: pygame clock object
    :precondition: trainer_name a non-empty string containing the user's name
    :precondition: screen is a pygame screen object representing the game window
    :precondition: clock is a pygame clock object representing the game clock
    :postcondition: display a welcome message, game rules, and informs user to proceed with the game
    """
    intro_text_font = pygame.font.Font(None, 28)

    show_rules_screen = True

    while show_rules_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # transition to the main game loop when any key is pressed
                show_rules_screen = False

        screen.fill((0, 0, 0))

        if show_rules_screen:
            # rules screen
            welcome_text = intro_text_font.render("Welcome, ", True, (255, 255, 255))
            name_text = intro_text_font.render(trainer_name, True, (255, 0, 0))
            rules_lines = [
                "Here are some rules:",
                "- You may use WASD keys or arrow keys for movement.",
                "- You will see a hospital, where you can recover your HP and save your game.",
                "- To move onto the next area, you will need to collect keys by beating",
                " wild Pokemon. When you win a battle, you will get a chance of receiving a key.",
                "- Beat all the trainers by collecting keys and leveling up your Pikachu and",
                "attempt to beat the champion!",
                "",
                "",
                "Press any key to continue..."
            ]

            # Display "Welcome, " and the user's name
            screen.blit(welcome_text, (50, 80))
            screen.blit(name_text, (50 + welcome_text.get_width(), 80))

            for line_index, line in enumerate(rules_lines):
                if "Press any key to continue..." in line:
                    rules_text = intro_text_font.render(line, True, (28, 10, 194))
                else:
                    rules_text = intro_text_font.render(line, True, (255, 255, 255))

                screen.blit(rules_text, (50, 50 + (line_index + 2) * 50))  # Adjust the margin between each line

        pygame.display.flip()
        pygame.display.update()
        clock.tick(30)
