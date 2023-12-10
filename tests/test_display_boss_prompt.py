import unittest
from unittest.mock import patch, Mock
import pygame
from game_gui.display_boss_prompt import display_boss_prompt


class TestDisplayBossPrompt(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.dummy_display = pygame.display.set_mode((1, 1))

    def tearDown(self):
        pygame.quit()

    @patch('pygame.font.Font')
    @patch('pygame.event.get')
    @patch('pygame.display.update')
    def test_display_boss_prompt_1(self, mock_update, mock_event_get, mock_font):
        mock_screen = Mock()
        mock_render = Mock()
        mock_font.return_value.render = mock_render

        mock_event_get.return_value = [Mock(type=pygame.KEYDOWN, key=pygame.K_1)]
        boss = {"name": "Trainer Edro Gonzales"}

        result = display_boss_prompt(mock_screen, boss)
        self.assertEqual(result, "1")

    @patch('pygame.font.Font')
    @patch('pygame.event.get')
    @patch('pygame.display.update')
    def test_display_boss_prompt_2(self, mock_update, mock_event_get, mock_font):
        mock_screen = Mock()
        mock_render = Mock()
        mock_font.return_value.render = mock_render

        mock_event_get.return_value = [Mock(type=pygame.KEYDOWN, key=pygame.K_2)]
        boss = {"name": "Trainer Ian Chan"}

        result = display_boss_prompt(mock_screen, boss)
        self.assertEqual(result, "2")

    @patch('pygame.font.Font')
    @patch('pygame.event.get')
    @patch('pygame.display.update')
    @patch('pygame.display.flip')
    def test_display_boss_prompt_quit_event(self, mock_flip, mock_update, mock_event_get, mock_font):
        mock_screen = Mock()
        mock_render = Mock()
        mock_font.return_value.render = mock_render

        mock_event_get.return_value = [Mock(type=pygame.QUIT)]
        boss = {"name": "Trainer Ian Chan"}

        with self.assertRaises(SystemExit):
            display_boss_prompt(mock_screen, boss)