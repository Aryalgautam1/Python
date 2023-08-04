# Dice Rolling Simulator: 
""" create a program that simulates rolling a dice and generate a random 
number between 1 and 6. Allow the user to roll the dice as many times as they
want and display the result each time"""

import random

class Dice:
    def __init__(self):
        self.result = None

    def roll(self):
        self.result = random.randint(1, 6)
        return self.result

def main():
    print("Welcome to the Dice Rolling Simulator!")
    dice = Dice()

    while True:
        input("Press Enter to roll the dice...")
        result = dice.roll()
        print(f"You rolled: {result}")
        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()

