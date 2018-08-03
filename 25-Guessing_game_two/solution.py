#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/16/2018
    Date last modified: 8/3/2018
    Python version: 3.6.5
    Description:
        Problem #25: Guessing Game Two from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Get number from user
def get_number():
    while True:
        try:
            number = int(input("Choose a number from 0 to 100 for computer to guess: "))
            if number >= 0 and number <= 100:
                break
            else:
                print("Your number is out of bounds.\nPlease try again...")
                continue
        except ValueError:
            print("You did not enter a number.\nPlease try again...")
    return number


# Get input from user
def get_input(guess):
    while True:
        response = input("Computer: I guessed {}. Is your number 'higher' or 'lower'? ".format(guess))
        if response == "higher" or response == "lower":
            break
        else:
            print("I don't understand your input.\nPlease try again...")
    return response


# Binary search
def computer_guess(number):
    left = 0
    right = 100
    middle = 50
    counter = 1
    while middle != number:
        counter += 1
        user_input = get_input(middle)
        if user_input == "lower":
            right = middle - 1
        elif user_input == "higher":
            left = middle + 1
        middle = (left + right) // 2
    return counter


# Main function
def main():
    number = get_number()
    result = computer_guess(number)
    print("I guessed the correct number({}) in {} tries!".format(number, result))


# Run program
if __name__ == "__main__":
    main()

