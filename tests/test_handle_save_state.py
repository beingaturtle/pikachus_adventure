"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import json
import os
import unittest
from unittest.mock import patch, MagicMock
import pygame
from game_gui.handle_save_state import handle_save_state


class TestHandleSaveState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.font.init()

    def setUp(self):
        self.screen = MagicMock()
        self.player = pygame.Rect(0, 0, 50, 50)
        self.character_info = {'name': 'test_character', 'level': 10, 'health': 100}
        self.saved_directory_path = os.path.join(os.path.dirname(__file__), '..', 'saved')
        self.file_name = os.path.join(self.saved_directory_path, "test_character_info.json")
        os.makedirs(self.saved_directory_path, exist_ok=True)
        initial_data = {'name': 'test_character', 'level': 5, 'health': 50}
        with open(self.file_name, 'w') as file:
            json.dump(initial_data, file)

    def test_handle_save_state(self):
        with patch('game_gui.handle_save_state.display_save_prompt', return_value="1"), \
             patch('pygame.font.Font'), \
             patch('pygame.display.update'), \
             patch('pygame.display.set_mode'):
            handle_save_state(self.screen, self.player, self.character_info)
            with open(self.file_name, 'r') as file:
                saved_data = json.load(file)
                self.assertEqual(saved_data, self.character_info)

    def tearDown(self):
        os.remove(self.file_name)

    @classmethod
    def tearDownClass(cls):
        pygame.font.quit()
        pygame.quit()
