"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import unittest
from unittest.mock import patch, Mock
from game_gui.boundaries import boundary_top


class TestBoundaryTop(unittest.TestCase):
    @patch('pygame.Rect')
    @patch('pygame.draw.rect')
    def test_boundary_top(self, mock_draw_rect, mock_rect):
        screen_mock = Mock()
        mock_rect_instance = mock_rect.return_value

        result = boundary_top(screen_mock)

        mock_rect.assert_called_once_with(465, -5, 5, 193)
        mock_draw_rect.assert_called_once_with(screen_mock, (150, 75, 0), mock_rect_instance)
        self.assertEqual(result, mock_rect_instance)
            