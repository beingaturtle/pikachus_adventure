"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
from pygame import Rect
from unittest import TestCase
from utils.state_machine import is_collision


class TestIsCollision(TestCase):

    def test_collision_true(self):
        player = Rect(100, 100, 150, 150)
        area = (150, 150)
        self.assertTrue(is_collision(player, area))

    def test_collision_false(self):
        player = Rect(100, 100, 50, 50)
        area = (200, 200)
        self.assertFalse(is_collision(player, area))

    def test_edge_collision(self):
        player = Rect(10, 10, 50, 50)
        area = (20, 20)
        self.assertTrue(is_collision(player, area))
