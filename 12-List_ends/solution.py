#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/14/2018
    Date last modified: 5/30/2018
    Python version: 3.6.5
    Description:
        Problem #12: List Ends from http://www.practicepython.org
	For detailed description of the problem see the accompanying
	file named 'problem.txt' or refer to the aformentioned website.
"""



# Make new list from first and last elements of original
def list_ends(lst):
    return [lst[0], lst[-1]]


# Main function
def main():
    # Define a list
    a = [5, 10, 15, 20, 25]
    
    print("Original list:", a)
    print("List made from first and last elements of the original:", list_ends(a))


# Run program
if __name__ == "__main__":
    main()

