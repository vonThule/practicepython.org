#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
		File name: solution.py
		Author: Alexander Popp
		Date created: 5/13/2018
		Date last modified: 5/22/2018
		Python version: 3.4.6
		Description:
				Problem #7: List Comprehensions from http://www.practicepython.org
				For detailed description of the problem see the accompanying
				file named 'problem.txt' or refer to the aformentioned website.
"""


# Declare a list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Output the list
print("List a: {}".format(a))

# Output a list with only the even elements from input list
print("[Result]\nResulting list of even elements from list a: {}".format([n for n in a if n % 2 == 0]))

