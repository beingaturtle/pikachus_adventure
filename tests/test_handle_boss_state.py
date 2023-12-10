"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import unittest
from unittest.mock import patch
import pygame
from game_gui.handle_boss_state import handle_boss_state


class TestHandleBossState(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.dummy_display = pygame.display.set_mode((1, 1))

    def tearDown(self):
        pygame.quit()

    @patch('game_gui.handle_boss_state.has_enough_keys', return_value=True)
    @patch('game_gui.handle_boss_state.display_boss_prompt', return_value='1')
    @patch('game_gui.handle_boss_state.battle')
    @patch('game_gui.handle_boss_state.flee')
    @patch('game_gui.handle_boss_state.display_only_message')
    @patch('game_gui.handle_boss_state.direction_subtract_coordinate')
    def test_handle_boss_state_has_enough_keys(self, mock_direction_subtract_coordinate, _, __, mock_battle,
                                               mock_display_boss_prompt, mock_has_enough_keys):
        screen = pygame.Surface((800, 600))
        player = pygame.Rect(0, 0, 50, 50)
        character_info = {"bosses_beaten": 0}
        boss_info = {0: {"name": "Trainer Edro Gonzales"}}
        facing_left = {"left": True}
        facing_right = {"right": False}
        facing_up = {"up": False}
        facing_down = {"down": False}

        handle_boss_state(screen, player, character_info, boss_info, facing_left, facing_right, facing_up, facing_down)

        mock_has_enough_keys.assert_called_once_with(character_info, boss_info[character_info["bosses_beaten"]])
        mock_display_boss_prompt.assert_called_once_with(screen, boss_info[character_info["bosses_beaten"]])
        mock_battle.assert_called_once_with(screen, character_info, boss_info[character_info["bosses_beaten"]])
        mock_direction_subtract_coordinate.assert_called_once_with(player, 'left')

    @patch('game_gui.handle_boss_state.has_enough_keys', return_value=False)
    @patch('game_gui.handle_boss_state.display_boss_prompt')
    @patch('game_gui.handle_boss_state.battle')
    @patch('game_gui.handle_boss_state.flee')
    @patch('game_gui.handle_boss_state.display_only_message')
    @patch('game_gui.handle_boss_state.direction_subtract_coordinate')
    def test_handle_boss_state_not_enough_keys(self, mock_direction_subtract_coordinate,
                                               mock_display_only_message, _, __, ___, mock_has_enough_keys):
        screen = pygame.Surface((1080, 900))
        player = pygame.Rect(0, 0, 70, 70)
        character_info = {"bosses_beaten": 2}
        boss_info = {2: {"name": "Trainer Richard M"}}
        facing_left = {"left": False}
        facing_right = {"right": False}
        facing_up = {"up": False}
        facing_down = {"down": False}

        handle_boss_state(screen, player, character_info, boss_info, facing_left, facing_right, facing_up, facing_down)

        mock_has_enough_keys.assert_called_once_with(character_info, boss_info[character_info["bosses_beaten"]])
        mock_display_only_message.assert_called_once_with(screen,
                                                          f"{boss_info[character_info['bosses_beaten']]['name']}"
                                                          f": You do not have enough keys to fight me. "
                                                          f"Press Enter to continue.")
        mock_direction_subtract_coordinate.assert_called_once_with(player, 'left')
