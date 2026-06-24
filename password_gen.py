import random
import pyperclip
from time import sleep



def main():
    letters = input("How many letters long do you want the password to be?")

    password = ''
    alphabet_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', '\\', '~', '`', '"', "'"]
    while len(password) < int(letters):
        if random.randint(0, 2) == 1:
            password += random.choice(alphabet_lowercase)
        else:
            password += random.choice(symbols)
    
    return password

pyperclip.copy(main())
quit()