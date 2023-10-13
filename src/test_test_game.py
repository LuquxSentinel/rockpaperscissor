import unittest
from unittest.mock import patch
from test_game import *

class TestTestGame(unittest.TestCase):
    testGame = TestGame()
    @patch('builtins.input', side_effect=['aper', 'dynamite', 'pape', 'scissor'])
    def test_get_user_input(self, input):
        self.testGame.test_get_user_input()

    def test_test_generate_computer_choice(self):
        try:
            self.testGame.test_generate_computer_choice()
        except:
            raise AssertionError
    
    def test_test_determine_winner(self):
        try:
            self.testGame.test_determine_winner()
        except:
            raise AssertionError

# if __name__ == '__main__':
#     unittest.main()