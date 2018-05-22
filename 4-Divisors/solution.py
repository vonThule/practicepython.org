#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
		File name: solution.py
		Author: Alexander Popp
		Date created: 5/13/2018
		Date last modified: 5/22/2018
		Python version: 3.4.6
		Description:
				Problem #4: Divisors from http://www.practicepython.org
				For detailed description of the problem see the accompanying
				file named 'problem.txt' or refer to the aformentioned website.
"""


# Get user input
def get_input():
		while True:
				try:
						number = int(input("Input a number: "))
				# If number not entered catch exception and inform user
				except ValueError:
						print("You didn't enter a number.\nPlease try again...")
				else:
						break
		return number


# Get resulting list of divisors
def get_divisors(number):
		# Create a list of possible divisors
		possible_divisor_list = list(range(1, number + 1))

		# Find divisors of number and add them to list
		divisors = []
		for possible_divisor in possible_divisor_list:
				if number % possible_divisor == 0:
						divisors.append(possible_divisor)

		return divisors


# Main function
def main():
		# Ask for input and find divisors
		number = get_input()
		divisors = get_divisors(number)
		
		# Output the result
		print("Number {} has following divisors: {}".format(number, divisors))


# Run program
if __name__ == "__main__":
		main()

