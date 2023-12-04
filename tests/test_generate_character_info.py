from unittest import TestCase
import os
import random
from game import generate_character_info

class TestGenerateCharacterInfo(TestCase):
    def test_valid_input(self):
        random_number = random.randint(1000, 9999)
        name = f"test_character-{random_number}"
        expected_output = {
            "name": name,
            "health": 100,
            "coordinates": (2, 1),
            "skill": "tackle",
            "attack_power": 10,
            "defense": 10,
            "keys": 0,
            "total_experience": 0
        }
        result = generate_character_info(name)
        self.assertEqual(result, expected_output)

    def test_file_creation(self):
        random_number = random.randint(1000, 9999)
        name = f"test_character-{random_number}"
        expected_file_path = os.path.join("saved", f"{name}_info.json")

        generate_character_info(name)
        file_exists = os.path.exists(expected_file_path)

        self.assertTrue(file_exists, f"The file {expected_file_path} does not exist.")
