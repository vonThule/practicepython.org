#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
		File name: solution.py
		Author: Alexander Popp
		Date created: 5/13/2018
		Date last modified: 5/20/2018
		Python version: 3.4.6
		Description:
				Problem #1: Character Input from http://www.practicepython.org
				For detailed description of the problem see the accompanying
				file named 'problem.txt' or refer to the aformentioned website.
"""

import datetime


# Get user name and check for valid input
def get_user_name():
		while True:
				name = input("Enter your name: ")
				# Name may not be of length 0
				if len(name) == 0:
						print("You did not enter a name.\nPlease try again...")
				# Name must contain only letters and spaces
				elif not all(char.isalpha() or char.isspace() for char in name):
						print("You may only use letters and spaces.\nPlease try again...")
				else:
						break
		return name.title()


# Get user age and check for valid input
def get_user_age(name):
		while True:
				try:
						age = int(input("Hello {}, how old are you? ".format(name)))
				# If entered age is not a number, catch exception and inform user
				except ValueError:
						print("You did not enter a number.\nPlease try again...")
				else:
						break
		return age


# Get number of repeats for message, if out of scope, ask for input again
def get_number_repeats(name):
		while True:
				try:
						print("How many times would you like the message displayed {}?".format(name))
						repeats = int(input("Enter a number from 1 to 20: "))
						# If entered value is not within set range, notify user
						if repeats <= 0 or repeats > 20:
								print("Your number is out of scope.\nPlease try again...")
						else:
								break
				# If entered value is not a number, catch exception and inform user
				except ValueError:
						print("You did not enter a number.\nPlease try again...")
		return repeats


# Calculate year to turn 100
def get_hundredth_year(age):
		current_year = datetime.datetime.now().year
		return current_year + 100 - age


# Main function
def main():
		user_name = get_user_name()
		user_age = get_user_age(user_name)
		message_repeats = get_number_repeats(user_name)
		hundredth_year = get_hundredth_year(user_age)

		# Display result n number of times
		for n in range(0, message_repeats):
				print("{}, you will turn 100 in the year {}.".format(user_name, hundredth_year))


# Run program
if __name__ == "__main__":
		main()

