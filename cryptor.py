#!/data/data/com.termux/files/usr/bin/python3
#!/usr/bin/python3

from time import sleep
import subprocess
import readline
import sys

 
def cls():
    idle_or_terminal = "idlelib" in sys.modules

    if idle_or_terminal == True:
        print("\n" * 100)
    else:
        readline.parse_and_bind("set editing-mode vim")
        subprocess.call("clear")


def encrypt(filename): 
    encrypted = ""

    with open(filename) as file:
        for line in file:
            for letter in line:
                encrypted += chr(ord(letter) + 5)

    final_encryption = encrypted * 3

    file = open(filename,"w")
    file.write(final_encryption)
    file.close()


def decrypt(filename): 
    decrypted = ""

    with open(filename) as file:
        for line in file:
            for letter in line:
                decrypted += chr(ord(letter) - 5)

    final_decryption = decrypted[0:int(len(decrypted) / 3)]

    file = open(filename,"w")
    file.write(final_decryption)
    file.close()

def options():
    print("""Cryptor - An easy-to-use tool for encrypting and decrypting a file.
        
Note: A file that has been encrypted by this tool can only be decrypted by this tool and files that haven't been encrypted by this tool can't be decrypted by it.\n""")

    print("e - to encrypt")
    print("d - to decrypt\n")

    choice = input()


    if choice == "e" or choice == "E" or choice == "encrypt" or choice == "Encrypt":
        filename = input("Which file do you want to encrypt? ")
        encrypt(filename)

    elif choice == "d" or choice == "D" or choice == "decrypt" or choice == "Decrypt":
        filename = input("Which file do you want to decrypt? ") 
        decrypt(filename)

    else:
        print("Sorry, but that is not an option.")
        sleep(1)
        cls()
        options()

try:
    options()

except:
    exit()
