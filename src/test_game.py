import unittest
from unittest.mock import patch
from  game import *

class TestGame(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['pper', 'ppew', '223r', 'paper'])
    def test_get_user_input(self, input):
        """Allows user to input a an option from a given list(rock,paper.scissor).
        If option not in list it prints 'Invalid choice. Please choose 'rock,' 'paper,' or 'scissors.'"""
        user_choice = get_user_input()
        self.assertIn (user_choice, ["rock", "paper", "scissor"])
    
    
    def test_generate_computer_choice(self):
        '''Determines computer choice by generating a list(rock,paper,scissor) and choosing a random choice'''
        computer_choice = generate_computer_choice()
        self.assertTrue(computer_choice.isalpha())

    def test_user_win(self):
        """Determines the winner based on the user's choice and the computer's choice. 
        Returns one of the following values: `user_wins`, `computer_wins`, or `tie`."""
        self.assertEqual(determine_winner("rock","scissor"),"user_wins")
        self.assertEqual(determine_winner("paper","rock"),"user_wins")
        self.assertEqual(determine_winner("scissor","paper"),"user_wins")
        
    def test_computer_wins(self):
        """Determines the winner based on the user's choice and the computer's choice. 
        Returns one of the following values: `user_wins`, `computer_wins`, or `tie`."""
        self.assertNotEqual(determine_winner("rock","scissor"),"computer_wins")
        self.assertNotEqual(determine_winner("paper","rock"),"computer_wins")
        self.assertNotEqual(determine_winner("scissor","paper"),"computer_wins")
    
    def test_draw(self):
        """Determines the winner based on the user's choice and the computer's choice. 
        Returns one of the following values: `user_wins`, `computer_wins`, or `tie`."""
        self.assertTrue(determine_winner("rock","rock")== "tie")
        self.assertTrue(determine_winner("paper","paper")== "tie")
        self.assertTrue(determine_winner("scissor","scissor")=="tie")
       
    
    # Write tests to detrimine the winners i.e. rock beats scissor, scissor beats paper, paper beats rock
    # Write tests to determine a tie between rock and rock, paper and paper, scissor and scissor.
    # Write your code below
        
        
if __name__ == '__main__':
    unittest.main()