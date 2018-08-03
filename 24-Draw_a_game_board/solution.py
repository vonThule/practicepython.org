#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/16/2018
    Date last modified: 8/3/2018
    Python version: 3.6.5
    Description:
        Problem #24: Draw a Game Board from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Ask user for board-size
def get_input():
    while True:
        try:
            size = int(input("Enter the size of the board (min. 3): "))
        except ValueError:
            print("Youd did not enter a number.\nPlease try again...")
        if size < 3:
            print("Board-size must be 3 or greater.\nPlease try again...")
        else:
            break
    return size


# Draw horizontal parts of board
def draw_horizontal(size):
    print(" ---" * size)


# Draw vertical parts of the board:
def draw_vertical(size):
    print("|   " * (size + 1))


# Main function
def main():
    size = get_input()
    counter = 0
    row = 1
    while counter != size:
        if row % 2 == 0:
            draw_vertical(size)
            counter += 1
        else:
            draw_horizontal(size)
        row += 1
    draw_horizontal(size)


# Run program
if __name__ == "__main__":
    main()

