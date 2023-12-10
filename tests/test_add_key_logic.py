from unittest import TestCase
from unittest.mock import Mock, patch
import pygame
import random
from utils.add_key_logic import add_key_logic

class TestAddKeyLogic(TestCase):
    def setUp(self):
        pygame.init()
        self.dummy_display = pygame.display.set_mode((1, 1))

    def tearDown(self):
        pygame.quit()

    @patch('pygame.font.Font')
    @patch('random.random')
    def test_add_key_logic_key_earned(self, mock_random, mock_font):
        mock_screen = Mock()
        mock_font.return_value.render.return_value = Mock()

        character = {"keys": 0}
        mock_random.return_value = 0.6
        add_key_logic(mock_screen, character)

        self.assertEqual(character["keys"], 1)

    @patch('pygame.font.Font')
    @patch('random.random')
    def test_add_key_logic_key_not_earned(self, mock_random, mock_font):
        mock_screen = Mock()
        mock_font.return_value.render.return_value = Mock()

        character = {"keys": 0}
        mock_random.return_value = 0.7
        add_key_logic(mock_screen, character)

        self.assertEqual(character["keys"], 0)
