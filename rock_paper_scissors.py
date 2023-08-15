"""Rock-Paper-Scissors Game: Create a simple text-based game of Rock-Paper-Scissors, where the user plays against the computer."""
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose: rock, paper, or scissors")

    choices = ["rock", "paper", "scissors"]
    player_choice = input("Your choice: ").lower()
    
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices)

    print(f"Computer chooses: {computer_choice}")
    print(determine_winner(player_choice, computer_choice))

if __name__ == "__main__":
    rock_paper_scissors()
