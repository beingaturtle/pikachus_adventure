from unittest import TestCase
from unittest.mock import patch
from utils.create_encounter_enemy import create_encounter

class TestCreateEncounter(TestCase):

    @patch('random.choice')
    def test_create_encounter(self, mock_choice):
        mock_choice.return_value = ("Weak", 5)

        encounter = create_encounter()

        self.assertIsInstance(encounter, dict)


        self.assertSetEqual(set(encounter.keys()), {"descriptor", "name", "health", "attack_power", "experience_award"})

        self.assertIsInstance(encounter['descriptor'], str)
        self.assertIsInstance(encounter['name'], str)
        self.assertIsInstance(encounter['health'], int)
        self.assertIsInstance(encounter['attack_power'], int)
        self.assertIsInstance(encounter['experience_award'], int)

        self.assertIn(encounter['name'], ["Magikarp", "Bidoof", "Zubat"])
        self.assertEqual(encounter['descriptor'], "Weak")
        self.assertEqual(encounter['attack_power'], 5)
