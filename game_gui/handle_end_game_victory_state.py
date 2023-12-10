"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import sys
import pygame
from pygame import Surface
from game_gui.display_prompt import display_end_win_message


def handle_end_game_victory_state(screen: Surface) -> None:
    """
    Control the end game victory state of the game.

    :param screen: a pygame object representing the game screen
    :precondition: screen must be a pygame object representing the game screen
    :postcondition: control the end game victory state of the game
    """
    display_end_win_message(screen, f"Congratulations! You beat Trainer Chris Thompson! Press Enter...")
    display_end_win_message(screen, f"Your last save point is unchanged. Press Enter...")
    display_end_win_message(screen, f"Thanks for playing! - Edro and Ian. Press Enter...")
    display_end_win_message(screen, f"The game will now close. Press Enter...")
    pygame.quit()
    sys.exit()
