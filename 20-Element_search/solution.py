#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/15/2018
    Date last modified: 8/2/2018
    Python version: 3.6.5
    Description:
        Problem #20: Element Search from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


import random


# Binary search
def binary_search(lst, num):
    left = 0
    right = len(lst) - 1
    found = False
    while left <= right and not found:
        middle = (left + right) // 2
        if lst[middle] == num:
            found = True
        else:
            if num < lst[middle]:
                right = middle - 1
            else:
                left = middle + 1
    return found


# Main function
def main():
    # Create a list and a random number
    a = [1, 3, 5, 30, 33, 35, 42, 43, 54, 58, 67, 87, 98]
    num = random.randint(0, 100)
    if binary_search(a, num):
        print("Number {} is in the list {}.".format(num, a))
    else:
        print("Number {} is not in the list {}.".format(num, a))


# Run program
if __name__ == "__main__":
    main()

