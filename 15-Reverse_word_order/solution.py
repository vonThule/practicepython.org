#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/14/2018
    Date last modified: 5/30/2018
    Python version: 3.6.5
    Description:
        Problem #15: Reverse Word Order from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Get user input
def get_input():
    while True:
        string = input("Enter a string with more than one word: ")
        if len(string.split()) > 1 and all(ch.isalpha() or ch.isspace() for ch in string):
            break
        else:
            print("Invalid input!\nPlease enter a valid string containing only letters and spaces...")
    return string


# Reverse word order
def reverse_string(string):
    word_list = string.split()
    result = []
    for i in range(len(word_list)-1, -1, -1):
        result.append(word_list[i])
    return " ".join(result)


# Main function
def main():
    string = get_input()
    reverse = reverse_string(string)
    print("Original string: {}\nReverse ordered string: {}".format(string, reverse))


# Run program
if __name__ == "__main__":
    main()

