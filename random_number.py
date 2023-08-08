"""Guess the Number: Write a program where the computer generates a random number, 
and the user has to guess it. Provide hints like "too high" or "too low"
 until the user correctly guesses the number."""

import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < secret_number:
            print("Too low! Try a higher number.")
        elif user_guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
