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

    def test_level_up_once(self):
        update_character_level(self.character, 1000)
        self.assertEqual(self.character["total_experience"], 1000)
        self.assertEqual(self.character["level"], 1)
        self.assertEqual(self.character["attack_power"], 150)
        self.assertEqual(self.character["health"], 150)

    def test_level_up_multiple(self):
        update_character_level(self.character, 3000)
        self.assertEqual(self.character["total_experience"], 3000)
        self.assertEqual(self.character["level"], 3)
        self.assertEqual(self.character["attack_power"], 337.5)
        self.assertEqual(self.character["health"], 337.5)

    def test_no_level_up(self):
        update_character_level(self.character, 500)
        self.assertEqual(self.character["total_experience"], 500)
        self.assertEqual(self.character["level"], 0)
        self.assertEqual(self.character["attack_power"], 100)
        self.assertEqual(self.character["health"], 100)

    def test_exact_level_up(self):
        update_character_level(self.character, 2000)
        self.assertEqual(self.character["total_experience"], 2000)
        self.assertEqual(self.character["level"], 2)
        self.assertEqual(self.character["attack_power"], 225)
        self.assertEqual(self.character["health"], 225)
