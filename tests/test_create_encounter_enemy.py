"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
from unittest import TestCase
from unittest.mock import patch
from utils.create_encounter_enemy import create_encounter_enemy


class TestCreateEncounter(TestCase):
    @patch('random.choice')
    @patch('itertools.cycle')
    def test_create_encounter_instance(self, mock_cycle, mock_choice):
        mock_choice.return_value = ("Weak", 5)
        mock_cycle.side_effect = [
            iter(["Magikarp", "Bidoof", "Zubat"]),
            iter(["Splash", "Tackle", "Scream"])
        ]

        encounter = create_encounter_enemy()
        self.assertIsInstance(encounter, dict)

    @patch('random.choice')
    @patch('itertools.cycle')
    def test_create_encounter_keys(self, mock_cycle, mock_choice):
        mock_choice.return_value = ("Weak", 5)
        mock_cycle.side_effect = [
            iter(["Magikarp", "Bidoof", "Zubat"]),
            iter(["Splash", "Tackle", "Scream"])
        ]

        encounter = create_encounter_enemy()
        self.assertSetEqual(set(encounter.keys()), {"enemy_type", "pokemon_name", "name", "health", "attack_power",
                                                    "experience_award", "skill"})

    @patch('random.choice')
    @patch('itertools.cycle')
    def test_create_encounter_enemy_type(self, mock_cycle, mock_choice):
        mock_choice.return_value = ("Weak", 5)
        mock_cycle.side_effect = [
            iter(["Magikarp", "Bidoof", "Zubat"]),
            iter(["Splash", "Tackle", "Scream"])
        ]

        encounter = create_encounter_enemy()
        self.assertEqual(encounter['enemy_type'], "wild")

    @patch('random.choice')
    @patch('itertools.cycle')
    def test_create_encounter_pokemon_name(self, mock_cycle, mock_choice):
        mock_choice.return_value = ("Weak", 5)
        mock_cycle.side_effect = [
            iter(["Magikarp", "Bidoof", "Zubat"]),
            iter(["Splash", "Tackle", "Scream"])
        ]

        encounter = create_encounter_enemy()
        self.assertIn(encounter['pokemon_name'], ["Magikarp", "Bidoof", "Zubat"])

    @patch('random.choice')
    @patch('itertools.cycle')
    def test_create_encounter_name(self, mock_cycle, mock_choice):
        mock_choice.return_value = ("Weak", 5)
        mock_cycle.side_effect = [
            iter(["Magikarp", "Bidoof", "Zubat"]),
            iter(["Splash", "Tackle", "Scream"])
        ]

        encounter = create_encounter_enemy()
        self.assertIsInstance(encounter['name'], str)

    @patch('random.choice')
    @patch('itertools.cycle')
    def test_create_encounter_health(self, mock_cycle, mock_choice):
        mock_choice.return_value = ("Weak", 5)
        mock_cycle.side_effect = [
            iter(["Magikarp", "Bidoof", "Zubat"]),
            iter(["Splash", "Tackle", "Scream"])
        ]

        encounter = create_encounter_enemy()
        self.assertEqual(encounter['health'], 50)

    @patch('random.choice')
    @patch('itertools.cycle')
    def test_create_encounter_attack_power(self, mock_cycle, mock_choice):
        mock_choice.return_value = ("Weak", 5)
        mock_cycle.side_effect = [
            iter(["Magikarp", "Bidoof", "Zubat"]),
            iter(["Splash", "Tackle", "Scream"])
        ]

        encounter = create_encounter_enemy()
        self.assertEqual(encounter['attack_power'], 5)

    @patch('random.choice')
    @patch('itertools.cycle')
    def test_create_encounter_experience_award(self, mock_cycle, mock_choice):
        mock_choice.return_value = ("Weak", 5)
        mock_cycle.side_effect = [
            iter(["Magikarp", "Bidoof", "Zubat"]),
            iter(["Splash", "Tackle", "Scream"])
        ]

        encounter = create_encounter_enemy()
        self.assertEqual(encounter['experience_award'], 250)

    @patch('random.choice')
    @patch('itertools.cycle')
    def test_create_encounter_skill(self, mock_cycle, mock_choice):
        mock_choice.return_value = ("Weak", 5)
        mock_cycle.side_effect = [
            iter(["Magikarp", "Bidoof", "Zubat"]),
            iter(["Splash", "Tackle", "Scream"])
        ]

        encounter = create_encounter_enemy()
        self.assertIn(encounter['skill'], ["Splash", "Tackle", "Scream"])
