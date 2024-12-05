import unittest
from unittest.mock import patch
from io import StringIO
from main import main
from fixtures import set_case_tests_as_str


class TestMain(unittest.TestCase):
    
    @patch("sys.stdin", new_callable=StringIO)
    @patch("sys.stdout", new_callable=StringIO)
    def test_main(self, mock_output, mock_input):
        case_tests = set_case_tests_as_str()
        for input_parameter, expected_value in case_tests:
            with self.subTest(input_data=input_parameter, expected_output=expected_value):
                mock_input.write(input_parameter)
                mock_input.seek(0)
                
                main()
                output = mock_output.getvalue()
                self.assertEqual(output, expected_value)
                
                mock_input.truncate(0)
                mock_input.seek(0)
                mock_output.truncate(0)
                mock_output.seek(0)
