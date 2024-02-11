import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        with patch('sys.stdin', return_value='create User') as mock_stdin:
            self.hbnb_cmd.onecmd("create User")
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        with patch('sys.stdin', return_value='show User') as mock_stdin:
            self.hbnb_cmd.onecmd("show User")
        self.assertEqual(mock_stdout.getvalue().strip(), "Error: instance id missing")

    # Add similar tests for destroy, all, update, and count

if __name__ == '__main__':
    unittest.main()
