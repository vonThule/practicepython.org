#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/14/2018
    Date last modified: 5/30/2018
    Python version: 3.6.5
    Description:
        Problem #14: List Remove Duplicates from http://www.practicepython.org
        For detailed description of the problem see the accompanying
	file named 'problem.txt' or refer to the aformentioned website.
"""


# Generate a list without duplicates using a loop
def generate_new_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


# Generate new list using a set
def generate_set(lst):
    return list(set(lst))


# Main function
def main():
    # Declare a list
    a = [1, 2, 3, 6, 2, 4, 4, 8, 10, 11, 10, 12, 3, 5, 7, 9, 5, 5, 13, 11, 7, 7, 8, 30]
    
    print("Original list:", a)
    print("[Using loops]List without duplicates:", generate_new_list(a))
    print("[Using sets]List without duplicates:", generate_set(a))


# Run program
if __name__ == "__main__":
    main()

