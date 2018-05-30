#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/15/2018
    Date last modified: 5/30/2018
    Python version: 3.6.5
    Description:
        Problem #18: Cows and Bulls from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


import random


# Get user input
def get_input():
    while True:
        try:
            number = int(input("Guess a four digit number: "))
            if len(str(number)) == 4:
                break
            else:
                print("The number must have four digits.\nPlease try again...")
                continue
        except ValueError:
            print("You did not enter a number.\nPlease try again...")
    return number


# Generate random number
def generate_number():
    return random.randint(1000, 9999)


# Ask user for another game
def play_again():
    while True:
        again = input("Another game? (y/n) ")
        if again.lower() == "y" or again.lower() == "n":
            break
        else:
            print("Invalid input.\nPlease try again...")
    return again


# Game function
def game():
    guess = generate_number()
    counter = 0
    while True:
        user = get_input()
        counter += 1
        hits = [0, 0]
        if user == guess:
            print("You guessed correct! Number of tries: {}.".format(counter))
            break
        else:
            for i in range(0, 4):
                if str(user)[i] == str(guess)[i]:
                    hits[0] += 1
                elif str(user)[i] != str(guess)[i] and str(user)[i] in str(guess):
                    hits[1] += 1
            print("{} cows, {} bulls".format(hits[0], hits[1]))
    return play_again()


# Main function
def main():
    while True:
        play = game()
        if play == "n":
            break
        else:
            continue


# Run program
if __name__ == "__main__":
    main()

