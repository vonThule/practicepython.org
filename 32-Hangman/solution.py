#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 8/21/2018
    Date last modified: 8/21/2018
    Python version: 3.6.5
    Description:
        Problem #32: Hangman from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


import random


# Load a word list file
def get_data(filename):
    with open(filename, "r") as f:
        file_data = f.readlines()
    return [line.strip() for line in file_data]


# Pick random word
def pick_word(words):
    return words[random.randint(0, len(words) - 1)]


# Get user input
def get_input(guessed_letters, guessed_words):
    while True:
        letter = input("Guess a letter: (A-Z) ")
        if letter.isalpha() and len(letter) == 1:
            if letter.upper() in guessed_letters:
                print("You already guessed that letter.\nTry another one...")
            else:
                break
        elif letter.isalpha() and len(letter) > 1:
            if letter.upper() in guessed_words:
                print("You already guessed that word.\nTry another one...")
            else:
                break
        else:
            print("Unrecognised input.\nPlease try again...")
    return letter.upper()


# Ask user for another game
def play_again():
    while True:
        again = input("Do you want to play again? (y/n) >> ")
        if again.lower() == "y":
            return True
        elif again.lower() == "n":
            return False
        else:
            print("Unrecognised input.\nPlease try again...")
    
    
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


# Game function
def game():
    word = pick_word(get_data("words.txt"))
    print("Word: ", word) #debug
    counter = 0
    guessed_letters = []
    guessed_words = []
    result = ["_" for x in range(0, len(word))]
    print("\nWelcome to hangman!\n")
    print(result)
    while True:
        letter = get_input(guessed_letters, guessed_words)
        if len(letter) > 1:
            if letter == word:
                print("YOU WIN! The word was:")
                print(word)
                break
            else:
                print("Not the word!")
                counter += 1
                guessed_words.append(letter)
        else:
            guessed_letters.append(letter)
            if check_letter(letter, word):
                result = add_letter(word, letter, result)
                counter += 1
                if check_complete(result):
                    print("YOU WIN! The word was:")
                    print(result)
                    break
            else:
                print("No such letter.")
                counter += 1
        print(result)
        print("Guessed letters:", guessed_letters)
        print("Guessed words:", guessed_words)
        print("Moves left: ", 6 - counter)
        if counter == 6:
            print("Out of moves!")
            print("The word was: ", word)
            break


# Main function
def main():
    game()
    while True:
        if play_again():
            game()
        else:
            print("Goodbye...")
            break


# Run program
if __name__ == "__main__":
    main()

