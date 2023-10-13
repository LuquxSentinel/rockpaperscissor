import random 
# Write you code below to determine a game of rock, ppaper, scissors.

"""Prompts the user to choose rock, paper, or scissors and returns the user's choice."""
def get_user_input():
    pass
    


"""Generates a random choice (rock, paper, or scissors) for the computer and returns it."""
def generate_computer_choice():
    choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choices)  
    return computer_choice



"""Determines the winner based on the user's choice and the computer's choice. Returns one of the following values: `user_wins`, `computer_wins`, or `tie`."""
def determine_winner(user_Choice,computer_choice):
    if user_Choice == computer_choice:
        return "tie"
    elif user_Choice == "paper" and computer_choice == "scissor":
        return "computer_wins"
    elif user_Choice == "rock" and computer_choice == "paper":
        return "computer_wins"
    elif user_Choice == "scissor" and computer_choice == "rock":
        return "computer_wins"
    else:
        return "user_wins"


"""Displays the user's choice and the computer's choice, and announces the winner."""
def display_result(user_choice, computer_choice, winner):
    pass

if __name__ == "__main__":
    user_choice = get_user_input()
    computer_choice = generate_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)