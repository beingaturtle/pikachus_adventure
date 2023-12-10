"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
from unittest import TestCase
from unittest.mock import patch, Mock

from game_gui.battle import display_fight_or_flee


class TestDisplayFightOrFlee(TestCase):
    @patch('pygame.display.update')
    @patch('pygame.font.Font')
    def test_display_fight_or_flee_font(self, mock_font, mock_update):
        screen_mock = Mock()
        test_message = "Test Message"
        mock_font_instance = mock_font.return_value
        mock_render = Mock()
        mock_font_instance.render.return_value = mock_render

        display_fight_or_flee(screen_mock, test_message)

        mock_font_instance.render.assert_called_once_with(test_message, True, (255, 255, 255))
        screen_mock.blit.assert_called_once_with(mock_render, (10, 90))
        mock_update.assert_called_once()
