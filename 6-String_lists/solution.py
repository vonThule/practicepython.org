#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/13/2018
    Date last modified: 8/8/2018
    Python version: 3.6.5
    Description:
        Problem #6: String Lists from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Take user input
def get_input():
    while True:
        string = input("Enter a string of characters: ")
        # Check if string inputed and if string is only letters and spaces
        if len(string) > 0 and all(char.isalpha() or char.isspace() for char in string):
            break
        else:
            print("Incorrect input.\nPlease try again...")
    return string


# Check if string is palindrome
def is_palindrome(string):
    string = "".join(string.split())
    if string == string[::-1]:
        return True
    return False


# Check if string is palindrome - iterative solution
def is_palindrome_it(string):
    for i in range(0, len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


# Main function
def main():
    user_string = get_input()
    if is_palindrome(user_string):
        print("String {} is a palindrome.".format(user_string))
    else:
        print("String {} is not a palindrome.".format(user_string))

    # if is_palindrome_it(user_string):
        # print("String {} is a palindrome.".format(user_string))
    # else:
        # print("String {} is not a palindrome.".format(user_string))


# Run program
if __name__ == "__main__":
    main()

