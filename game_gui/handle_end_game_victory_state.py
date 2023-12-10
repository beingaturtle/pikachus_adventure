import sys
import pygame
from game_gui.display_prompt import display_end_win_message


def handle_end_game_victory_state(boss_info, character_info, screen):
    display_end_win_message(screen, f"Congratulations! You beat Trainer Chris Thompson! Press Enter...")
    display_end_win_message(screen, f"You will return back to your last save point. Press Enter...")
    display_end_win_message(screen, f"Thanks for playing! - Edro and Ian. Press Enter...")
    display_end_win_message(screen, f"The game will now close. Press Enter...")
    pygame.quit()
    sys.exit()