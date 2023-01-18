import os
import pyfiglet as pyg


filename = 'secret.txt'

# Creating the banner
def theBanner():
    os.system("cls")
    result = pyg.figlet_format("Hide and Encrypt",  font = "puffy",width = 100)
    print(result)
    print(" ~ Created By jw ~")
    print("")

# functions to open & close files
def save_to_file(text, filename):
    with open(filename, "w") as f:
        f.write(text)

def get_from_file(filename):
    with open(filename, "r") as f:
        return f.read()

# functions to hide & show folders
def hidehoShow(text1):
    
    if text1 == 's':
        print('You choose the show option')
        os.system('attrib -h /s')
        
    elif text1 == 'h':
        print('You choose the hide option')
        os.system('attrib +h /s')
            
    elif text1 == 'exit':
        print('Thank you for using my program')
        run = False
        os.system('exit')
    print("")
    os.system('attrib -h hideAndEncrypt.py')
        

# function to encrypt and decrpyt
def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_char = chr((ord(char) + shift - 97) % 26 + 97)
            ciphertext += shift_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift_char = chr((ord(char) - shift - 97) % 26 + 97)
            plaintext += shift_char
        else:
            plaintext += char
    return plaintext

# main function
global run
run = True
theBanner()
while True:
    print('choose 1 or 2')
    print('1. hide or show files')
    print('2. encrpyt or decrpyt files')
    text1 = input()
    if text1 == '1':
        os.system("cls")
        text1 = input('Choose to show or hide or exit: (s/h/exit)? ').lower()
        if text1 == 'exit': 
            os.system('exit')
            #run = False
            break
        hidehoShow(text1)

    elif text1 == '2':
        os.system("cls")
        word = input('choose to encrypt or decrypt or exit: (e/d/exit) ').lower()
        if word == 'e':
            plaintext = input("Enter a text: ").lower()
            shift = int(input("Enter a number: "))
            ciphertext = encrypt(plaintext, shift)
            save_to_file(ciphertext, filename)

        elif word == 'd':
            os.system("cls")
            ciphertext = get_from_file(filename)
            shift = int(input("Enter a number between 1 to 26: "))
            decrypted_text = decrypt(ciphertext, shift)
            loaded_text = get_from_file(filename)
            print(decrypted_text)
            answer = input("would you like to add the decrypt text to the file? (y/n) ")
            if answer == 'y':
                os.system("cls")
                save_to_file(decrypted_text, filename)
            else:
                os.system("cls")
                break
        
        elif word == 'exit':
            print('Thank you for using my program')
            os.system('exit')
            break
        
        else:
            print('i didnt understand Try Again!')
            print("")
        
    else:
        print('I didnt understand can you try again?')
        os.system('cls')
    os.system("cls")
