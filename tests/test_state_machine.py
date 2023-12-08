import unittest
from utils.state_machine import state_machine
from pygame import Rect

class TestStateMachine(unittest.TestCase):
    def setUp(self):
        self.player = Rect(0, 0, 50, 50)
        self.character_info = {"bosses_beaten": 0, "health": 100}

    def test_live_game_state(self):
        self.assertEqual(state_machine(self.player, self.character_info), "live_game")

    def test_boss_state(self):
        self.player.topleft = (441, 188)
        self.assertEqual(state_machine(self.player, self.character_info), "boss_state")

    def test_save_state(self):
        self.player.topleft = (410, 25)
        self.assertEqual(state_machine(self.player, self.character_info), "save_state")

    def test_end_game_victory(self):
        self.character_info["bosses_beaten"] = 4
        self.assertEqual(state_machine(self.player, self.character_info), "end_game_victory")

    def test_end_game_loss(self):
        self.character_info["health"] = 0
        self.assertEqual(state_machine(self.player, self.character_info), "end_game_loss")