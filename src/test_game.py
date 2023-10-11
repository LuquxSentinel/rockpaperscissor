import unittest
from  game import get_user_input, generate_computer_choice, determine_winner, display_result

class TestGame(unittest.TestCase):
    
    def test_get_user_input(self):
        user_choice = get_user_input()
        self.assertIn (user_choice, ["rock", "paper", "scissor"])
    
    def test_generate_computer_choice(self):
        computer_choice = generate_computer_choice()
        self.assertIn (computer_choice,["rock", "paper", "scissor"])

    def test_determine_winner(self):
        """Determines the winner based on the user's choice and the computer's choice. Returns one of the following values: `user_wins`, `computer_wins`, or `tie`."""
    
    # Write tests to detrimine the winners i.e. rock beats scissor, scissor beats paper, paper beats rock
    # Write tests to determine a tie between rock and rock, paper and paper, scissor and scissor.
    # Write your code below
        
        
if __name__ == '__main__':
    unittest.main()