from unittest import TestCase
from unittest.mock import patch
from game import get_name

class TestGetName(TestCase):
    @patch('builtins.input', return_value='Ash Ketchum')
    def test_get_name_valid(self, _):
        expected_name = 'Ash Ketchum'
        result = get_name()
        self.assertEqual(result, expected_name)