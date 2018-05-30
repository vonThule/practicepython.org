#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/14/2018
    Date last modified: 5/30/2018
    Python version: 3.6.5
    Description:
        Problem #13: Fibonacci from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Get user input
def get_input():
    while True:
        try:
	    number = int(input("How many Fibonacci numbers do you want to generate: "))
	except ValueError:
	    print("You did not enter a number.\nPlease try again...")
	else:
	    break
    return number


# Generate fibonacci number
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Create a sequnce of numbers
def get_fibonacci_sequence(n):
    result = []
    for i in range(1, n + 1):
        result.append(fibonacci(i))
    return result


# Main function
def main():
    number = get_input()
    result = get_fibonacci_sequence(number)
    print("The resulting sequence of numbers is:", result)


# Run program
if __name__ == "__main__":
    main()

