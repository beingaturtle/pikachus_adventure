"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import unittest
from unittest.mock import patch, MagicMock
import pygame
from game_gui.game_quit import game_quit


class TestGameQuit(unittest.TestCase):
    @patch('pygame.event.get')
    def test_quit_event(self, mock_event_get):
        mock_event = MagicMock()
        mock_event.type = pygame.QUIT
        mock_event_get.return_value = [mock_event]

        result = game_quit()

        self.assertEqual(result, False)

    @patch('pygame.event.get')
    def test_quit_escape_key(self, mock_event_get):
        mock_event = MagicMock()
        mock_event.type = pygame.KEYDOWN
        mock_event.key = pygame.K_ESCAPE
        mock_event_get.return_value = [mock_event]

        result = game_quit()

        self.assertEqual(result, False)

    @patch('pygame.event.get')
    def test_no_quit_event(self, mock_event_get):
        mock_event = MagicMock()
        mock_event.type = pygame.KEYDOWN
        mock_event.key = pygame.K_a
        mock_event_get.return_value = [mock_event]

        result = game_quit()

        self.assertEqual(result, True)
