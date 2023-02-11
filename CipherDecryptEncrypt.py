"""Textfile Decryptor/Encryptor

This script allows the user to decrypt or encrypt textfiles. It is assumed 
that if the user wants to decrypt a file, the file is plaintext. 

This tool wants 1 (one) textfile (.txt) from the current directory to 
decrypt/encrypt.

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

Returns:
    _type_: _description_
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


def decrypt(encrypted_file):
    """ Decodes an encrypted plaintext .txt file 

    Calls get_key() to retrieve cipher key

    Creates .txt file that starts with 'decoded_' and reads from 
    filename given by parameter. Replaces ciphertext with letters from 
    key and writes to 'decoded_' .txt file

    Args:
        encrypted_file (str): Name of encrypted .txt file
    """

    key = get_key()

    file2 = open(f"decoded_{encrypted_file}", "w")
    with open(encrypted_file) as file:
        for line in file:
            line = line.translate(str.maketrans(key, alphabet))
            file2.write(line)
    file2.close()
    print(f"\nDecrypted file created as 'decoded_{encrypted_file}'")


def encrypt(plain_file):
    """ Encrypts a plaintext .txt file

    Calls make_plainttext(filename) to create a plaintext .txt file

    Creates .txt file that starts with 'ciphertext_'. Generates a random
    26-character key. Replaces plaintext with letters from the key and 
    writes to 'ciphertext_' .txt file

    Args:
        plain_file (str): Name of plaintext .txt file
    """

    plaintext_file = make_plaintext(plain_file)
    list = random.sample(alphabet, len(alphabet))
    key = ''.join(list)

    key_file = open(f"key_{plain_file}", "w")
    key_file.write(key)
    print(f"Key stored in 'key_{plain_file}'")

    encrypted_file = open(f"ciphertext_{plain_file}", "w")
    with open(plaintext_file) as file:
        for line in file:
            line = line.translate(str.maketrans(alphabet, key))
        encrypted_file.write(line)
    print(f"\nEncrypted file created as 'ciphertext_{plaintext_file}'")

    encrypted_file.close()
    key_file.close()


def make_plaintext(rich_text):
    """ Turns a .txt file to a plaintext file

    Creates a plaintext version of the user's .txt file by replacing 
    uppercase letters with lowercase letters and removing all punctuation.

    Args:
        rich_text (str): User's filename input

    Returns:
        str: Name of newly created .txt file
    """

    plain_file_name = f"plaintext_{rich_text}"
    plain = open(plain_file_name, "w")
    with open(rich_text) as file:
        for line in file:
            line = line.lower()
            line = line.translate(str.maketrans('', '', string.punctuation))
            plain.write(line)
    plain.close()

    print(f"Plaintext version of .txt file created as 'plaintext_{rich_text}'")
    return plain_file_name


def get_key():
    """ Gets encryption key from user

    Prompts user to input a 26-character key that acts as the substitution alphabet

    Raises:
        ValueError: If input is not 26-characters long

    Returns:
        str: Key for decoding ciphertext
    """

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


def decrypt_or_encrypt(choice, file):
    """ 'D' to decrypt, 'E' to encrypt, '!QUIT' to exit program

    Args:
        choice (str): command
        file (str): file name

    Raises:
        ValueError: If input isn't 'D', 'E', or '!QUIT'
    """

    match choice:
        case 'D':
            decrypt(file)
        case'E':
            encrypt(file)
        case'!QUIT':
            quit()
        case _:
            raise ValueError(
                f"ERROR: Command '{choice}' not recognized. Format is capital D or E or !QUIT\n")


def get_text_file_name():
    """ Makes sure filename is a .txt file and in current directory

    Raises:
        ValueError: If not a .txt file
        FileNotFoundError: If file isn't in current directory

    Returns:
        str: valid filename
    """

    print("To Exit, type !QUIT")
    file = input("Enter a .txt file to encrypt/decrypt: \n")

    if file == "!QUIT":
        quit()

    if not file.endswith(".txt"):
        raise ValueError("ERROR: .txt file extension not found\n")

    if not os.path.isfile(file):
        raise FileNotFoundError(
            f"ERROR: {file} is not found in {os.getcwd()}\n")

    return file


"""
START OF MAIN METHOD
"""
if __name__ == "__main__":
    more = True
    file = ""
    while (more):
        try:
            file = get_text_file_name()
            more = False
        except (ValueError, FileNotFoundError) as e:
            print(e)
            continue
    print()
    more = True
    while (more):
        try:
            print("To Exit, type !QUIT")
            choice = input(
                "Do you want to [D]ecrypt or [E]ncrypt this file?: ")
            decrypt_or_encrypt(choice, file)
            more = False
        except ValueError as e:
            print(e)
            continue
