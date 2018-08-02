#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/16/2018
    Date last modified: 8/2/2018
    Python version: 3.6.5
    Description:
        Problem #23: File Overlap from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


# Read file
def read_file(filename):
    with open(filename, "r") as f:
        file_content = f.readlines()
    return [int(line.strip()) for line in file_content]


# Find overlapping numbers between two files
def find_overlap(file1, file2):
    result = []
    for number in file1:
        if number in file2:
            result.append(number)
    return result


# Main function
def main():
    primes = read_file("primenumbers.txt")
    happies = read_file("happynumbers.txt")
    print("Overlapping numbers:", find_overlap(primes, happies))


# Run program
if __name__ == "__main__":
    main()

