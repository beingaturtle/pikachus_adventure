from unittest import TestCase
from utils.get_save_file import get_save_file

class TestGetSaveFile(TestCase):
    def test_get_save_file_existing_user(self):
        trainer_name = "user_exist"
        expected = {
            "name": trainer_name,
            "health": 100,
            "coordinates": [2, 1],
            "skill": "tackle",
            "attack_power": 10,
            "defense": 10,
            "keys": 0,
            "total_experience": 0,
            "bosses_beaten": 0
        }
        result = get_save_file(trainer_name)

        self.assertEqual(expected, result)
