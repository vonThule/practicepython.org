#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
		File name: solution.py
		Author: Alexander Popp
		Date created: 5/13/2018
		Date last modified: 5/21/2018
		Python version: 3.4.6
		Description:
				Problem #2: Odd or Even from http://www.practicepython.org
				For detailed description of the problem see the accompanying
				file named 'problem.txt' or refer to the aformentioned website.
"""


# Get user input and make shure input is a valid number
def get_user_input(numeration):
		while True:
				try:
						number = int(input("Enter {} number: ".format(numeration)))
				# If a number is not entered, catch exception and inform user
				except ValueError:
						print("You did not enter a number.\nPlease try again...")
				else:
						break
		return number


# Check if number is even or odd and output the information
def even_odd(number):
		if number % 2 == 0:
				print("Your number is even!")
		else:
				print("Your number is odd!")


# Check if number is a multiple of 4 and output the information if so
def multiple_of_four(number):
		if number % 4 == 0:
				print("Your number is a multiple of 4!")


# Check if one number divides into another evenly and output the information
def number_divide_into_another(num, check):
		if num % check == 0:
				print("Number {} divides evenly by {}.".format(num, check))
		else:
				print("Number {} does not divide evenly by {}.".format(num, check))


# Main function
def main():
		print("\n1. Check if number is even or odd or a multiple of 4...")
		number = get_user_input("a")
		even_odd(number)
		multiple_of_four(number)
		
		print("\n2. Check if one number divides into another...")
		num = get_user_input("first")
		check = get_user_input("second")
		number_divide_into_another(num, check)


# Run program
if __name__ == "__main__":
		main()

