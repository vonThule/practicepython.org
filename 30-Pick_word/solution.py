#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/18/2018
    Date last modified: 8/7/2018
    Python version: 3.6.5
    Description:
        Problem #30: Pick Word from http://www.practicepython.org
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


# Main function
def main():
    word = pick_word(get_data("words.txt"))
    print("Randomly picked word:", word)


# Run program
if __name__ == "__main__":
    main()

