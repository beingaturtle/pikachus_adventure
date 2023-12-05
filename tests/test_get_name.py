from unittest import TestCase
from unittest.mock import patch
from utils.get_name import get_name

class TestGetName(TestCase):
    @patch('builtins.input', return_value='Ash_Ketchum')
    def test_get_name_valid(self, _):
        expected_name = 'Ash_Ketchum'
        result = get_name()
        self.assertEqual(result, expected_name)