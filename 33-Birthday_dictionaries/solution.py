#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/20/2018
    Date last modified: 8/7/2018
    Python version: 3.6.5
    Description:
        Problem #33: Birthday Dictionaries from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Get user input
def get_input(dictionary):
    while True:
        name = input("Who's birthday do you want to look up? ")
        if name.title() in dictionary:
            break
        else:
            print("Unrecognised input.\nPlease try again...")
    return name.title()


# Main function
def main():
    dictionary = {
        "Ernest Rutherford": [8, 30, 1871],
        "Werner Heisenberg": [12, 5, 1901],
        "Erwin Schroedinger": [8, 12, 1887],
        "Max Planck": [4, 23, 1858]
    }
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for item in dictionary:
        print(item)
    name = get_input(dictionary)
    print("{}'s birthday is {}/{}/{}.".format(name, dictionary[name][0], dictionary[name][1], dictionary[name][2]))


# Run program
if __name__ == "__main__":
    main()

