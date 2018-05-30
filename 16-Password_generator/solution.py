#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/15/2018
    Date last modified: 5/30/2018
    Python version: 3.6.5
    Description:
        Problem #16: Password Generator from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


import random
import string


# Get user input
def get_number_of_chars():
    while True:
        try:
            number = int(input("How many characters in your password: "))
        except ValueError:
            print("You did not enter a number.\nPlease try again...")
        else:
            break
    return number


# Ask for passwrod sterngth
def get_password_strength():
    while True:
        print("Choose password strength.")
        print("1. Weak\n2. Medium\n3. Strong")
        try:
            strength = int(input("Your choice (1,2,3) >> "))
            if strength in (1, 2, 3):
                break
            else:
                print("Wrong entry.\nPlease enter a number from 1 to 3 only...")
        except ValueError:
            print("You did not enter a number.\nPlease try again...")
    return strength


# Read word list file
def read_word_file():
    with open("words.txt", "r") as f:
        data = f.readlines()
    word_list = [n.strip() for n in data]
    return word_list


# Weak password generation
def get_weak(num):
    word_list = read_word_file()
    current_length = 0
    password = ""
    while current_length < num:
        rand = random.randint(0, len(word_list) - 1)
        random_word = word_list[rand]
        password += random_word
        current_length += len(random_word)
        if len(password) > num:
            diff = len(password) - num
            password = password[:-diff]
    return password


# Generate password
def generate_password(numchars, strength):
    password = ""
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    characters = string.punctuation
    if strength == 1:
        password = get_weak(numchars)
    elif strength == 2:
        chars = lowercase + numbers
        for i in range(0, numchars):
            rand = random.randint(0, len(chars) - 1)
            password += chars[rand]
    elif strength == 3:
        chars = lowercase + uppercase + numbers + characters
        for i in range(0, numchars):
            rand = random.randint(0, len(chars) - 1)
            password += chars[rand]
    return password


# Main function
def main():
    number = get_number_of_chars()
    strength = get_password_strength()
    password = generate_password(number, strength)
    print("Your password is:", password)


# Run program
if __name__ == "__main__":
    main()

