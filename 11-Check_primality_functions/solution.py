#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/14/2018
    Date last modified: 8/8/2018
    Python version: 3.6.5
    Description:
        Problem #11: Check Primality Functions from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Get input from user and check if it's valid
def get_user_input():
    while True:
        try:
            number = int(input("Enter a number: "))
        # If input is not an integer, catch exception and inform user
        except ValueError:
            print("You did not enter a number.\nPlease try again...")
        else:
            break
    return number


# Check primality
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


# Main function
def main():
    num = get_user_input()
    if is_prime(num):
        print("Number {} is a prime number.".format(num))
    else:
        print("Number {} is not a prime number.".format(num))


# Run program
if __name__ == "__main__":
    main()

