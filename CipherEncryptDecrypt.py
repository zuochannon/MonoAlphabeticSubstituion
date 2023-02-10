__author__      = "Channon Zuo"
__email__       = "01channonzuo@gmail.com"
__published__   = "02/10/19"
__updated__     = "02/10/19"
__version__     = "1.0.0"

import string
import os
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(encryptedFile):    
    # TODO: add body of decrypt(file)
    key = get_key()
    
    file2 = open(f"decoded_{encryptedFile}", "w")
    with open(encryptedFile) as file:
        for line in file:
            line = line.translate(str.maketrans(key, alphabet))
            file2.write(line)
    file2.close()
    print(f"\nDecrypted file created as 'decoded_{encryptedFile}'")     
    
def encrypt(plain_file):
    plaintextFile = make_plaintext(plain_file)
    list = random.sample(alphabet, len(alphabet))
    key = ''.join(list)
    
    keyFile = open(f"key_{plain_file}", "w")
    keyFile.write(key)
    print(f"Key stored in 'key_{plain_file}'")
    
    encryptedFile = open(f"ciphertext_{plain_file}", "w")
    with open(plaintextFile) as file:
        for line in file:
            line = line.translate(str.maketrans(alphabet, key))
        encryptedFile.write(line)
    print(f"\nEncrypted file created as 'ciphertext_{plaintextFile}'")
    
    encryptedFile.close()
    keyFile.close()

def make_plaintext(raw_file):
    plain_file_name = f"plaintext_{raw_file}"
    plain = open(plain_file_name, "w")
    with open(raw_file) as file:
        for line in file:
            line = line.lower()
            line = line.translate(str.maketrans('','', string.punctuation))
            plain.write(line)
    plain.close()
    
    print(f"Plaintext version of .txt file created as 'plaintext_{raw_file}'")
    return plain_file_name

def get_key():
    more = True
    while(more):
        try:
            key = input("Paste/Type in your 26 letter key: \n")
            if len(key) != 26:
                raise ValueError(f"ERROR: Length of '{key}' is {len(key)}. It should be 26 characters long.\n")
            more = False
        except ValueError as e:
            print(e)
            continue
    return key

def decrypt_or_encrypt(choice, file):
    match choice:
        case 'D': 
            decrypt(file)
        case'E':
            encrypt(file)
        case'!QUIT':
            quit()    
        case _:
            raise ValueError(f"ERROR: Command '{choice}' not recognized. Format is capital D or E or !QUIT\n")
            
def get_text_file_name():
    print("To Exit, type !QUIT")
    file = input("Enter a .txt file to encrypt/decrypt: \n")
    
    if file == "!QUIT":
        quit()
        
    if not file.endswith(".txt"):
        raise ValueError("ERROR: .txt file extension not found\n")
    
    if not os.path.isfile(file):
        raise FileNotFoundError(f"ERROR: {file} is not found in {os.getcwd()}\n")
    
    return file

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
            choice = input("Do you want to [D]ecrypt or [E]ncrypt this file?: ")    
            decrypt_or_encrypt(choice, file)
            more = False
        except ValueError as e:
            print(e)
            continue