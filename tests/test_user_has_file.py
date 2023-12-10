"""
Pikachu's Adventure
Edro Gonzales A01257468
Ian Chan A00910012
"""
from unittest import TestCase
from utils.user_has_file import user_has_file
import os
import json


class TestUserHasFile(TestCase):
    @staticmethod
    def create_test_user_file(username):
        saved_directory_path = os.path.join(os.path.dirname(__file__), '..', 'saved')
        file_path = os.path.join(saved_directory_path, f"{username}_info.json")
        with open(file_path, "w") as file:
            json.dump({}, file)

    @staticmethod
    def delete_test_user_file(username):
        saved_directory_path = os.path.join(os.path.dirname(__file__), '..', 'saved')
        file_path = os.path.join(saved_directory_path, f"{username}_info.json")
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_user_file_edro_exists(self):
        test_username = "edro"
        self.create_test_user_file(test_username)
        self.assertTrue(user_has_file(test_username))
        self.delete_test_user_file(test_username)

    def test_user_file_exists(self):
        test_username = "test_character"
        self.create_test_user_file(test_username)
        self.assertTrue(user_has_file(test_username))
        self.delete_test_user_file(test_username)

    def test_user_file_does_not_exist(self):
        test_username = "nonexistent_user"
        self.assertFalse(user_has_file(test_username))
