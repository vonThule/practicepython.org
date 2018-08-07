#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/20/2018
    Date last modified: 8/7/2018
    Python version: 3.6.5
    Description:
        Problem #35: Birthday Months from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


import json


# Read file
def read_data_file(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


# Write to json
def write_data_file(filename, dictionary):
    with open(filename, "w") as f:
        json.dump(dictionary, f)


# Extract months from dictionary into a list
def get_months(dictionary):
    mnt_lst = []
    for key, value in dictionary.items():
        mnt_lst.append(int(value[:2]))
    return mnt_lst


# Get month stats
def get_stats(mnt_lst):
    stats = {}
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"
             ]
    for mnt in mnt_lst:
        if months[mnt - 1] not in stats:
            stats[months[mnt - 1]] = 1
        else:
            stats[months[mnt - 1]] += 1
    return stats


# Main function
def main():
    dictionary = read_data_file("birthdays.json")
    months = get_months(dictionary)
    stats = get_stats(months)
    print("\nBirthday month statistics:\n")
    for key, value in stats.items():
        print(key + " : " + str(value))
    write_data_file("stats.json", stats)


# Run program
if __name__ == "__main__":
    main()

