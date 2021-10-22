from cryptography.fernet import Fernet
from crypt import *
from Create_DB import create_database_and_password


print('''Welcome to Your Personal Vault
       /#/#/#\#\#\\
     /#/#/     \#\#\\
    |#|#|       |#|#|
    |#|#|       |#|#|
    |#|#|       |#|#|
 -----------------------
 |\#/\#/\#/\#/\#/\#/\#/|
 |\#/\#/\#/   \#/\#/\#/|
 |\#/\#/\#/   \#/\#/\#/|
 |\#/\#/\#/   \#/\#/\#/|
 |\#/\#/\#/\#/\#/\#/\#/|
 -----------------------''')


def save_masterpw(masterpw):
    key = Fernet.generate_key()
    add_keys(masterpw,key)

if is_1st_time():
    masterpw = input("Guess this is your first time\nEnter your Master Password:")
    print("Remember it as you will need to provide it everytime you run this program.\n")
    save_masterpw(masterpw)
    create_database_and_password()
else:
    while True:
        masterpw = input("Enter your Master Password:")
        stored_masterpw = get_masterpw()
        if masterpw == stored_masterpw:
            del masterpw,stored_masterpw
            break
        print("Incorrect!")

#Dont change position of this import statemnt . It wont work without it being exactly here
from vaultdb import *

while True:
    print("\nAvaiable Tasks:\n(1)View stored Passwords\n(2)Generate a Strong Password\n(3)Add Password\n(4)Update Password\n(5)Remove one of the stored Password\n(6)Update master password\n(7)Exit Program\n")

    task = input("What would you like to do:")

    if task == '1':
        subtask = input("Would you like to view (a)ll the stored passwords or of a (s)pecific site (a/s):")
        if subtask == 'a':
            display('a')
        elif subtask == 's':
            display_sites()
            # Input to display details of a specific site
            app = input("Which site's password you want:")
            details = display('s',app=app)
            print(details)
            copy = input("Would you like to copy password to clipboard(y/n):")
            if copy == 'y':
                copy2clip(decrypt(details[3].encode(), get_key()))
                print("Copied!.\nRemember to clear clipboard after using!")
        else:
            print("Invalid Input!")

    elif task == '2':
        print(f"This is a program generated strong password: {generate_pw()}")

    elif task == '3':
        n = int(input("How many details would you like to add: "))
        for i in range(n):
            app = input("Enter Site/App name: ")
            uname = input("Enter your username: ")
            pw = input("Enter your password for the site: ")
            pw = encrypt(pw, get_key()).decode()
            add(app,uname,pw)

    elif task == '4':
        display_sites()
        app = input("Which site's password would you like to update:")
        pw = input("Enter new password:")
        pw = encrypt(pw, get_key()).decode()
        update(app,pw)

    elif task == '5':
        display_sites()
        app = input("Which site's password would you like to remove:")
        remove(app)

    elif task == '6':
        if is_1st_time():
            print("You can't reset your master password if you haven't set it yet!")
        else:
            masterpw = input("Please enter your new master password: ")
            save_masterpw(masterpw)

    elif task == '7':
        break

    else:
        print("\nInvalid Input!\n")

connection.close()
quit()