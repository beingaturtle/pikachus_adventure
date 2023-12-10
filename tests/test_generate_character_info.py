"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
from unittest import TestCase
import os
import random
import json
from utils.generate_character_info import generate_character_info


class TestGenerateCharacterInfo(TestCase):
    def test_valid_input_name(self):
        random_number = random.randint(1000, 9999)
        name = f"test_character-{random_number}"
        result = generate_character_info(name)
        self.assertEqual(result["name"], name)

    def test_valid_input_health(self):
        name = "test_character"
        result = generate_character_info(name)
        self.assertEqual(result["health"], 100)

    def test_valid_input_coordinates(self):
        name = "test_character"
        result = generate_character_info(name)
        self.assertEqual(result["coordinates"], [2, 1])

    def test_valid_input_skill(self):
        name = "test_character"
        result = generate_character_info(name)
        self.assertEqual(result["skill"], "tackle")

    def test_valid_input_attack_power(self):
        name = "test_character"
        result = generate_character_info(name)
        self.assertEqual(result["attack_power"], 10)

    def test_valid_input_agility(self):
        name = "test_character"
        result = generate_character_info(name)
        self.assertEqual(result["agility"], 10)

    def test_valid_input_keys(self):
        name = "test_character"
        result = generate_character_info(name)
        self.assertEqual(result["keys"], 0)

    def test_valid_input_total_experience(self):
        name = "test_character"
        result = generate_character_info(name)
        self.assertEqual(result["total_experience"], 0)

    def test_valid_input_bosses_beaten(self):
        name = "test_character"
        result = generate_character_info(name)
        self.assertEqual(result["bosses_beaten"], 0)

    def test_valid_input_level(self):
        name = "test_character"
        result = generate_character_info(name)
        self.assertEqual(result["level"], 0)

    def test_file_creation_exists(self):
        random_number = random.randint(1000, 9999)
        name = f"test_character-{random_number}"
        generate_character_info(name)
        expected_file_path = os.path.abspath(f"../saved/{name}_info.json")
        file_exists = os.path.exists(expected_file_path)

        self.assertTrue(file_exists)

    def test_file_content_match(self):
        random_number = random.randint(1000, 9999)
        name = f"test_character-{random_number}"
        expected_file_path = os.path.join(os.path.dirname(__file__), '..', 'saved', f"{name}_info.json")

        expected_output = generate_character_info(name)

        with open(expected_file_path, "r") as file:
            file_content = json.load(file)

        self.assertEqual(file_content, expected_output)
