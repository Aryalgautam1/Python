"""Text Encryption/Decryption: Create a program that can encrypt and
 decrypt text using a simple substitution cipher or a Caesar cipher."""


def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    return caesar_encrypt(encrypted_text, -shift)

# Input the text and encryption shift
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the encryption shift (1-25): "))

# Encrypt the text
encrypted_text = caesar_encrypt(text, shift)
print("Encrypted Text:", encrypted_text)

# Decrypt the text
decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted Text:", decrypted_text)
