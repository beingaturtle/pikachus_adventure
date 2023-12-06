from unittest import TestCase
from utils.user_has_file import user_has_file

class TestUserHasFile(TestCase):
    def test_user_file_exists(self):
        test_username = "test_character"
        self.assertTrue(user_has_file(test_username))

    def test_user_file_does_not_exist(self):
        test_username = "nonexistent_user"
        self.assertFalse(user_has_file(test_username))
