import random

# List of words for the game
word_list = ["python", "hangman", "programming", "computer", "science", "keyboard"]

def choose_random_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman_game():
    print("Welcome to Hangman Game!")
    word_to_guess = choose_random_word()
    guessed_letters = set()
    attempts_left = 6

    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word:", word_to_guess)
            break

        if attempts_left == 0:
            print("You ran out of attempts! The word was:", word_to_guess)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            attempts_left -= 1
            print(f"Wrong guess! You have {attempts_left} attempts left.")

if __name__ == "__main__":
    hangman_game()
