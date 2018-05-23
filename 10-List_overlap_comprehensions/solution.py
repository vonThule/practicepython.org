#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
		File name: solution.py
		Author: Alexander Popp
		Date created: 5/13/2018
		Date last modified: 5/23/2018
		Python version: 3.4.6
		Description:
				Problem #10: List Overlap Comprehensions from http://www.practicepython.org
				For detailed description of the problem see the accompanying
				file named 'problem.txt' or refer to the aformentioned website.
"""


from random import randint, sample


# Generate a random list
def generate_list():
		length = randint(5, 100)
		element_range = range(1, randint(1, 100))
		return sample(element_range, length if len(element_range) > length else len(element_range))


# Main function
def main():
		# Hardcoded lists
		a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
		b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
		print("List a: {}\nList b: {}".format(a, b))

		# Output resulting intersection list
		print("\n[Solution with generic lists]")
		print([n for n in set(a) if n in b])

		# Randomly generated lists
		c = generate_list()
		d = generate_list()
		print("\n\nList c: {}\nList d: {}".format(c, d))

		# Second solution
		print("\n[Solution with random lists]")
		print([n for n in set(c) if n in d])


# Run program
if __name__ == "__main__":
		main()

