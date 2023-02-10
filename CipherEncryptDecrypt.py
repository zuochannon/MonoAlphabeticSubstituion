__author__      = "Channon Zuo"
__email__       = "01channonzuo@gmail.com"
__published__   = "02/10/19"
__updated__     = "02/10/19"
__version__     = "1.0.0"

import string
import os

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(fileName):    
    # TODO: add body of decrypt(file)
    key = get_key()
    file2 = get_new_file_name()
    with open(fileName) as file:
        for line in file:
            line = line.translate(str.maketrans(alphabet, key))
            file2.write(line)
    file2.close()
    print("decrypted file")     # stub code
    
def encrypt(file):
    # TODO: add body of encrypt(file)
    print("encrypted file")     # stub code

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

def get_new_file_name():
    # TODO: add body of get_new_file_name()
    print("new file name")      # stub code

def decrypt_or_encrypt(choice, file):
    print(choice)
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
    # TODO: split this method into 2. One to check .txt file ending and another to see if it is in file
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