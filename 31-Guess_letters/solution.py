#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/18/2018
    Date last modified: 8/7/2018
    Python version: 3.6.5
    Description:
        Problem #31: Guess Letters from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Get user input
def get_input(guessed):
    while True:
        letter = input("Guess a letter: (A-Z) ")
        if letter.isalpha() and len(letter) == 1:
            if letter in guessed:
                print("You already guessed that letter.\nTry another one...")
            else:
                break
        else:
            print("Unrecognised input.\nPlease try again...")
    return letter


# Check if letter in string
def check_letter(letter, word):
    if letter in word:
        return True
    return False


# Add letter to empty field
def add_letter(word, letter, result):
    for i in range(0, len(word)):
        if word[i] == letter:
            result[i] = letter
    return result


# Check if game complete
def check_complete(result):
    for letter in result:
        if letter == "_":
            return False
    return True


# Main function
def main():
    word = "EVAPORATE"
    guessed = []
    result = ["_" for x in range(0, len(word))]
    print("\nWelcome to hangman!\n")
    print(result)
    while True:
        letter = get_input(guessed)
        guessed.append(letter)
        if check_letter(letter, word):
            result = add_letter(word, letter, result)
            if check_complete(result):
                print(result)
                break
        else:
            print("No such letter.")
        print(result)
        print("Guessed letters:", guessed)


# Run program
if __name__ == "__main__":
    main()

