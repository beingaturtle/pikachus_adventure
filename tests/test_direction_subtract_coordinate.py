"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import unittest
import pygame
from game_gui.direction_subtract_coordinate import direction_subtract_coordinate


class TestDirectionSubtractCoordinate(unittest.TestCase):
    def test_left(self):
        player = pygame.Rect(0, 0, 10, 10)
        direction_subtract_coordinate(player, 'left')
        self.assertEqual(player.left, 10)

    def test_right(self):
        player = pygame.Rect(10, 0, 10, 10)
        direction_subtract_coordinate(player, 'right')
        self.assertEqual(player.right, 10)

    def test_up(self):
        player = pygame.Rect(0, 10, 10, 10)
        direction_subtract_coordinate(player, 'up')
        self.assertEqual(player.top, 20)

    def test_down(self):
        player = pygame.Rect(0, 10, 10, 10)
        direction_subtract_coordinate(player, 'down')
        self.assertEqual(player.bottom, 10)
