"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
from unittest import TestCase
from utils.update_character_level import update_character_level


class TestUpdateCharacterLevel(TestCase):
    def setUp(self):
        self.character = {
            "total_experience": 0,
            "level": 0,
            "attack_power": 100,
            "health": 100
        }

    def test_level_up_experience(self):
        update_character_level(self.character, 1000)
        self.assertEqual(self.character["total_experience"], 1000)

    def test_level_up_level(self):
        update_character_level(self.character, 1000)
        self.assertEqual(self.character["level"], 1)

    def test_level_up_attack_power(self):
        update_character_level(self.character, 1000)
        self.assertEqual(self.character["attack_power"], 150)

    def test_level_up_health(self):
        update_character_level(self.character, 1000)
        self.assertEqual(self.character["health"], 150)

    def test_multiple_level_up_experience(self):
        update_character_level(self.character, 3000)
        self.assertEqual(self.character["total_experience"], 3000)

    def test_multiple_level_up_level(self):
        update_character_level(self.character, 3000)
        self.assertEqual(self.character["level"], 3)

    def test_multiple_level_up_attack_power(self):
        update_character_level(self.character, 3000)
        self.assertEqual(self.character["attack_power"], 337.5)

    def test_multiple_level_up_health(self):
        update_character_level(self.character, 3000)
        self.assertEqual(self.character["health"], 337.5)

    def test_no_level_up_experience(self):
        update_character_level(self.character, 500)
        self.assertEqual(self.character["total_experience"], 500)

    def test_no_level_up_level(self):
        update_character_level(self.character, 500)
        self.assertEqual(self.character["level"], 0)

    def test_no_level_up_attack_power(self):
        update_character_level(self.character, 500)
        self.assertEqual(self.character["attack_power"], 100)

    def test_no_level_up_health(self):
        update_character_level(self.character, 500)
        self.assertEqual(self.character["health"], 100)

    def test_exact_level_up_experience(self):
        update_character_level(self.character, 2000)
        self.assertEqual(self.character["total_experience"], 2000)

    def test_exact_level_up_level(self):
        update_character_level(self.character, 2000)
        self.assertEqual(self.character["level"], 2)

    def test_exact_level_up_attack_power(self):
        update_character_level(self.character, 2000)
        self.assertEqual(self.character["attack_power"], 225)

    def test_exact_level_up_health(self):
        update_character_level(self.character, 2000)
        self.assertEqual(self.character["health"], 225)
