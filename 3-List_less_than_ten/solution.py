#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/13/2018
    Date last modified: 8/8/2018
    Python version: 3.6.5
    Description:
        Problem #3: List Less Than Ten from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Print out all elements less than 5
def print_less_than_five(a):
    print("Elements that are less than 5:")
    for element in a:
        if element < 5:
            print(element)


# Make a new list of elements less than 5
def create_list(a):
    new_list = []
    for element in a:
        if element < 5:
            new_list.append(element)
    return new_list


# Get user input
def get_input():
    while True:
        try:
            number = int(input("Enter a number: "))
        # If input is not a number catch exception and inform user
        except ValueError:
            print("You did not enter a number.\nPlease try again...")
        else:
            break
    return number


# Main function
def main():
    # Define a list and print it
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print("Original list:", a)
		
    # Print out elements of the list that are less than 5
    print_less_than_five(a)
		
    # Make a new list of elements less than 5 and print it
    new_list = create_list(a)
    print("List of elements less than 5:", new_list)

    # Make a new list of elements less than 5 and print it(one liner)
    print("List of elements less than 5(oneliner):", [element for element in a if element < 5])

    # Ask user for input and print a list that contains elements smaller
    # than the users number
    user_input = get_input()
    print("List of elements less than number {}: {}".format(user_input, [element for element in a if element < user_input]))


# Run program
if __name__ == "__main__":
    main()

