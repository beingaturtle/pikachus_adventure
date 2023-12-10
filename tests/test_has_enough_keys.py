"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
import unittest
from utils.initialize_bosses import has_enough_keys


class TestHasEnoughKeys(unittest.TestCase):
    def test_enough_keys_true(self):
        character_info = {"keys": 3}
        current_boss = {"keys_required": 3}
        result = has_enough_keys(character_info, current_boss)
        self.assertEqual(result, True)

    def test_not_enough_keys_false(self):
        character_info = {"keys": 2}
        current_boss = {"keys_required": 3}
        result = has_enough_keys(character_info, current_boss)
        self.assertEqual(result, None)
