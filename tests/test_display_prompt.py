"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
from unittest import TestCase
from unittest.mock import Mock, patch
import pygame
from game_gui.display_prompt import display_prompt


class TestDisplayPrompt(TestCase):
    def setUp(self):
        pygame.init()
        self.dummy_display = pygame.display.set_mode((1, 1))

    def tearDown(self):
        pygame.quit()

    @patch('pygame.font.Font')
    @patch('pygame.display.update')
    @patch('pygame.event.get')
    def test_display_prompt_k1_key(self, mock_event_get, _, mock_font):
        mock_screen = Mock()
        mock_render = Mock()
        mock_font.return_value.render = mock_render

        mock_event_get.return_value = [Mock(type=pygame.KEYDOWN, key=pygame.K_1)]

        response = display_prompt(mock_screen, "Test Message 1")
        self.assertEqual(response, "1")

    @patch('pygame.font.Font')
    @patch('pygame.display.update')
    @patch('pygame.event.get')
    def test_display_prompt_k2_key(self, mock_event_get, _, mock_font):
        mock_screen = Mock()
        mock_render = Mock()
        mock_font.return_value.render = mock_render

        mock_event_get.return_value = [Mock(type=pygame.KEYDOWN, key=pygame.K_2)]

        response = display_prompt(mock_screen, "Test Message 2")
        self.assertEqual(response, "2")

    @patch('pygame.font.Font')
    @patch('pygame.display.update')
    @patch('pygame.event.get')
    def test_display_prompt_quit_event(self, mock_event_get, _, mock_font):
        mock_screen = Mock()
        mock_render = Mock()
        mock_font.return_value.render = mock_render

        mock_event_get.return_value = [Mock(type=pygame.QUIT)]

        with self.assertRaises(SystemExit):
            display_prompt(mock_screen, "Test Message 3")
