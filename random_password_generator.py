"""Random Password Generator: Design a program that generates a random password with a 
specified length and includes a mix of letters, numbers, and special characters."""

import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Input the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate and display the random password
random_password = generate_random_password(password_length)
print("Random Password:", random_password)
