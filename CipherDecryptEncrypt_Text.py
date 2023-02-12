"""Textfile Decryptor/Encryptor

This script allows the user to decrypt or encrypt a message from stdin. It is assumed
that the message is in the English language or uses the English alphabet.

This script requires Python 3.10 or later.

This file contains the following functions:
    * decrypt - creates 1 (one) new (.txt) file containing 
                               decrypted ciphertext
    * encrypt - creates 2 (two) (.txt) files. 1 (one) 
                            containing the new ciphertext and 1 (one)
                            containing the randomly generated key
    * make_plaintext - creates 1 (one) new plaintext (.txt) file
    * get_key - asks user for the substitution alphabet
    * decrypt_or_encrypt - asks user if they want to decrypt/encrypt a 
                           (.txt) file
    * get_text_file_name - checks if filename is (.txt) file and in
                           current directory
    * main - main function of script
"""

__author__ = "Channon Zuo"
__email__ = "01channonzuo@gmail.com"
__published__ = "02/10/19"
__updated__ = "02/10/19"
__version__ = "1.0.0"

import string
import os
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def decrypt(encrypted_text, key):
    decrypted_str = encrypted_text.translate(str.maketrans(key, alphabet))
    return decrypted_str


def encrypt(plaintext, key):
    encrypted_str = plaintext.translate(str.maketrans(alphabet, key))
    return encrypted_str


def make_plaintext(rich_text):
    plaintext = rich_text.lower()
    plaintext = plaintext.translate(str.maketrans('', '', string.punctuation))
    return plaintext


def get_key():
    more = True
    while (more):
        try:
            key = input("Type in your 26 letter key: \n")
            if len(key) != 26:
                raise ValueError(
                    f"ERROR: Length of '{key}' is {len(key)}. It should be 26 characters long.\n")
            more = False
        except ValueError as e:
            print(e)
            continue
    return key


def generate_key():
    list = random.sample(alphabet, len(alphabet))
    key = ''.join(list)
    return key


def decrypt_or_encrypt(choice, text):
    match choice:
        case 'D' | 'd':
            message = decrypt(text, get_key())
            print(f"\nDecoded message: {message}")
        case'E' | 'e':
            key = generate_key()
            plaintext = make_plaintext(text)
            message = encrypt(plaintext, key)
            print(f"\nEncrypted message: {message}")
            print(f"Key: {key}")
        case'!QUIT':
            quit()
        case _:
            raise ValueError(
                f"ERROR: Command '{choice}' not recognized. Format is 'D', 'E', or !QUIT\n")


def get_message():
    message = input("What is your message you want to decrypt or encrypt?\n")
    if message == '!QUIT':
        quit()
    return message

def continue_choice():
    continue_loop = input("Do you want to continue? Y/N: ")
    match continue_loop:
        case 'Y' | 'y':
            pass
        case 'N' | 'n':
            quit()
        case _:
            raise ValueError(
                f"ERROR: Command '{continue_loop}' not recognized. Format is Y or N\n")    
"""
START OF MAIN METHOD
"""
if __name__ == "__main__":
    # TODO: Write methods for asking input to be able to repeat certain questions if input is not right
    more = True
    print("To Exit, type !QUIT")
    message = get_message()
    while (more):
        print("To Exit, type !QUIT")
        try:
            choice = input("Do you want to [D]ecrypt or [E]ncrypt this file?: ")
            decrypt_or_encrypt(choice, message)
            continue_choice()
        except ValueError as e:
            print(e)
            continue
