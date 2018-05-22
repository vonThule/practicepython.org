#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
		File name: solution.py
		Author: Alexander Popp
		Date created: 5/13/2018
		Date last modified: 5/22/2018
		Python version: 3.4.6
		Description:
				Problem #5: List Overlap from http://www.practicepython.org
				For detailed description of the problem see the accompanying
				file named 'problem.txt' or refer to the aformentioned website.
"""


import random


# Create a set, populate it and output the result
def get_list_intersection(a, b):
		result = set()
		for number in a:
				if number in b:
						result.add(number)
		return list(result)


# Generate a list
def generate_list():
		# Get a random number from 0 to 50 to be used as list length
		list_length = random.randint(0, 50)
		# Generate a list from random numbers 0 to 100
		random_list = []
		for i in range(0, list_length):
				random_list.append(random.randint(0, 100))
		return random_list


# Output list
def print_lists(list1, list2):
		print("List a: {}\nList b: {}\n".format(list1, list2))


# Output result
def print_result(result):
		print("Intersection of the two lists is: {}.\n".format(result))

		
# Main function
def main():
		# Two lists as input
		a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
		b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13]

		# Output the two lists
		print_lists(a, b)

		# Get the intersection of the two lists and print out the resulting list
		intersection = get_list_intersection(a, b)
		print_result(intersection)

		# Get the intersection of the two lists and print out the resulting list(oneliner)
		print("[Oneline solution]\nIntersection of the two lists is: {}.\n\n".format(list(set(a).intersection(b))))

		# Generate two random lists
		r1 = generate_list()
		r2 = generate_list()

		# Output the two random lists
		print_lists(r1, r2)

		# Get the intersection of the two random lists and print of the resulting list
		intersection = get_list_intersection(r1, r2)
		print_result(intersection)


# Run program
if __name__ == "__main__":
		main()

