# Importing Fernet class
from cryptography.fernet import Fernet
# Importing dump and load function
from pickle import dump,load

# To generate a strong pw
def generate_pw():
    from random import choice
    choices = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=.,/<>?;:\\|[]}{")
    pw = ""
    for i in range(25):
        pw += choice(choices)
    return pw
    del pw,choice

# To get master pw from the file
def get_masterpw():
    # Opening the file storing master pw
    with open("key.key",'rb') as file:
        # Loading data
        keys = load(file)
        # Master pw is converted from bytes to string
        key = keys[0].decode()
        del keys
    # Return keys
    return key

# To get key from the file
def get_key():
    # Opening the file storing master pw
    with open("key.key",'rb') as file:
        # Loading data
        keys = load(file)
        # Key is converted from bytes to string
        key = keys[1].decode()
        del keys
    # Return keys
    return key

# To store master pw in the file
def add_keys(masterpw,key):
    # Opening the file to store master pw
    with  open("key.key",'wb') as file:
        # Making list of value to upload
        # key is already in bytes # Converting to bytes is not necessary
        keys = [masterpw.encode(),key]
        # Dumping the master pw to file
        dump(keys,file)
        # Deleting the variable
        del masterpw,key,keys

# Checking if user is running program for first time
def is_1st_time():
    # Trying to open bytes file
    # If file is opened means program was executed once or more
    try:
        with open("key.key",'rb') as file:
            pass
        return False
    # FileNotFound means its first time
    # Or either its not in directory of this file or user deleted it :) #
    except FileNotFoundError:
        return True

# Function to copy pw to clipboard
def copy2clip(pw):
    # Importing copy function
    from pyperclip import copy
    # Copying pw to clipboard
    copy(pw)
    del pw,copy

# Encrypting the text
def encrypt(text, key):
    try:
        # Defining Fernet(class) using the key
        fernet = Fernet(key)
        # Encryption # Text is converted to bytes
        encrypted_text = fernet.encrypt(text.encode())
        del key
        # Return encrypted text
        return encrypted_text
    # Error message if any
    except Exception as e:
        print(f"Error occured:{e}\nProcess unsuccessful")

# Decrypting the text
def decrypt(text, key):
    try:
        # Defining Fernet(class) using the key
        fernet = Fernet(key)
        # Decryption # Text is converted from bytes to string
        decrypted_text = fernet.decrypt(text).decode()
        del key
        # Return decrypted text
        return decrypted_text
    # Error message if any
    except Exception as e:
        print(f"Error occured:{e}\nProcess unsuccessful")