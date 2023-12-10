from unittest import TestCase
from unittest.mock import patch
from utils.create_encounter_enemy import create_encounter_enemy

class TestCreateEncounter(TestCase):

    @patch('random.choice')
    @patch('itertools.cycle')
    def test_create_encounter(self, mock_cycle, mock_choice):
        mock_choice.return_value = ("Weak", 5)
        mock_cycle.side_effect = [
            iter(["Magikarp", "Bidoof", "Zubat"]),  # For enemy_names
            iter(["splash", "tackle", "scream"])   # For skill
        ]

        encounter = create_encounter_enemy()

        self.assertIsInstance(encounter, dict)

        self.assertSetEqual(set(encounter.keys()), {"enemy_type", "pokemon_name", "name", "health", "attack_power", "experience_award", "skill"})

        self.assertEqual(encounter['enemy_type'], "wild")
        self.assertIn(encounter['pokemon_name'], ["Magikarp", "Bidoof", "Zubat"])
        self.assertIsInstance(encounter['name'], str)
        self.assertEqual(encounter['health'], 50)
        self.assertEqual(encounter['attack_power'], 5)
        self.assertEqual(encounter['experience_award'], 250)
        self.assertIn(encounter['skill'], ["splash", "tackle", "scream"])
