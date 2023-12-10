"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
from unittest import TestCase
from utils.state_machine import state_machine
from pygame import Rect


class TestStateMachine(TestCase):
    def setUp(self):
        self.player = Rect(0, 0, 50, 50)
        self.character_info = {"bosses_beaten": 0, "health": 100}
        self.boss_info = (
            {
                "enemy_type": "boss",
                "name": "Trainer Edro Gonzales",
                "health": 100,
                "coordinates": [453, 189],
                "skill": "Splash",
                "pokemon_name": "Magikarp",
                "attack_power": 10,
                "agility": 10,
                "keys_required": 3,
                "experience_award": 500
            },
            {
                "enemy_type": "boss",
                "name": "Trainer Ian Chan",
                "health": 100,
                "coordinates": [675, 441],
                "skill": "Quick Attack",
                "pokemon_name": "Rattata",
                "attack_power": 20,
                "agility": 20,
                "keys_required": 6,
                "experience_award": 500
            },
        )

    def test_live_game_state(self):
        self.assertEqual(state_machine(self.player, self.character_info, self.boss_info), "live_game")

    def test_boss_state(self):
        self.player.topleft = (441, 188)
        self.assertEqual(state_machine(self.player, self.character_info, self.boss_info), "boss_state")

    def test_save_state(self):
        self.player.topleft = (410, 25)
        self.assertEqual(state_machine(self.player, self.character_info, self.boss_info), "save_state")

    def test_end_game_victory(self):
        self.character_info["bosses_beaten"] = 4
        self.assertEqual(state_machine(self.player, self.character_info, self.boss_info), "end_game_victory")

    def test_end_game_loss(self):
        self.character_info["health"] = 0
        self.assertEqual(state_machine(self.player, self.character_info, self.boss_info), "end_game_loss")
