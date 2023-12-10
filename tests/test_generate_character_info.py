from unittest import TestCase
import os
import random
import json
from utils.generate_character_info import generate_character_info

class TestGenerateCharacterInfo(TestCase):
    def test_valid_input(self):
        random_number = random.randint(1000, 9999)
        name = f"test_character-{random_number}"
        expected_output = {
            "name": name,
            "health": 100,
            "coordinates": [2, 1],
            "skill": "tackle",
            "attack_power": 10,
            "agility": 10,
            "keys": 0,
            "total_experience": 0,
            "bosses_beaten": 0,
            "level": 0  # Add the expected 'level' key and value
        }
        result = generate_character_info(name)
        self.assertEqual(result, expected_output)

    def test_file_creation(self):
        random_number = random.randint(1000, 9999)
        name = f"test_character-{random_number}"
        expected_file_path = os.path.join(os.path.dirname(__file__), '..', 'saved', f"{name}_info.json")  # Update the expected file path

        expected_output = generate_character_info(name)
        file_exists = os.path.exists(expected_file_path)

        self.assertTrue(file_exists, f"The file {expected_file_path} does not exist.")

        with open(expected_file_path, "r") as file:
            file_content = json.load(file)

        self.assertEqual(file_content, expected_output)
