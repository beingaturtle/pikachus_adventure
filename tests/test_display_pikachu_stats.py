import io
from unittest import TestCase
from unittest.mock import patch
from utils.display_pikachu_stats import display_pikachu_stats


class TestPikachuStats(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pikachu_stats_new_character(self, mock_output):
        new_character = {
            "name": "edro",
            "health": 100,
            "coordinates": (0, 0),
            "skill": "tackle",
            "attack_power": 10,
            "agility": 10,
            "keys": 0,
            "total_experience": 0,
            "bosses_beaten": 0
        }
        display_pikachu_stats(new_character)
        result = mock_output.getvalue()
        expected = (
            "Pikachu's stats:\n"
            "-----------------------------------------\n"
            "Health: 100\n"
            "Skill: tackle\n"
            "Number of Keys: 0\n"
            "Experience: 0\n"
            "Number of trainers to defeat: 4\n")
        self.assertEqual(expected, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pikachu_stats_played_character(self, mock_output):
        played_character = {
            "name": "ian",
            "health": 69,
            "coordinates": (4, 8),
            "skill": "iron tail",
            "attack_power": 30,
            "agility": 30,
            "keys": 6,
            "total_experience": 29,
            "bosses_beaten": 2
        }
        display_pikachu_stats(played_character)
        result = mock_output.getvalue()
        expected = (
            "Pikachu's stats:\n"
            "-----------------------------------------\n"
            "Health: 69\n"
            "Skill: iron tail\n"
            "Number of Keys: 6\n"
            "Experience: 29\n"
            "Number of trainers to defeat: 2\n")
        self.assertEqual(expected, result)
