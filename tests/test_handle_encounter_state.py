"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import unittest
from unittest.mock import patch
import pygame
from game_gui.handle_encounter_state import handle_encounter_state


class TestHandleEncounterState(unittest.TestCase):
    @patch('game_gui.handle_encounter_state.create_encounter_enemy')
    @patch('game_gui.handle_encounter_state.display_prompt', return_value='1')
    @patch('game_gui.handle_encounter_state.battle')
    @patch('game_gui.handle_encounter_state.flee')
    def test_choice_1(self, mock_flee, mock_battle, mock_display_prompt,
                      mock_create_encounter_enemy):
        screen = pygame.Surface((800, 600))
        character_info = {"bosses_beaten": 0}
        mock_enemy = {"name": "Trainer Edro Gonzales"}
        mock_create_encounter_enemy.return_value = mock_enemy

        handle_encounter_state(screen, character_info)

        mock_create_encounter_enemy.assert_called_once()
        mock_display_prompt.assert_called_once_with(screen, f"A {mock_enemy['name']} is challenging you to a duel. "
                                                            f"You can choose to fight for flee? Press 1 for fight, "
                                                            f"2 for flee", 22)
        mock_battle.assert_called_once_with(screen, character_info, mock_enemy)
        mock_flee.assert_not_called()
