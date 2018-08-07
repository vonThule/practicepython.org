#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/20/2018
    Date last modified: 8/7/2018
    Python version: 3.6.5
    Description:
        Problem #34: Birthday JSON from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


import json


# Get user choice
def get_choice():
    text = "\nMain menu\n==============================\n"
    text += "1. View persons birthday\n"
    text += "2. Add an entry\n"
    text += "3. Quit\n"
    text += "Choose an option (1-3) >> "
    while True:
        try:
            choice = int(input(text))
            if choice >= 1 and choice <= 3:
                break
            else:
                print("You must choose a number between 1 and 3.\nPlease try again...")
        except ValueError:
            print("Unrecognised input.\nPlease try again...")
    return choice


# Get user input
def get_input(dictionary):
    while True:
        name = input("Who's birthday do you want to look up? ")
        if name.title() in dictionary:
            break
        else:
            print("Unrecognised input.\nPlease try again...")
    return name.title()


# Enter new name
def input_new_name():
    while True:
        name = input("Enter name: ")
        if all(char.isalpha() or char.isspace() for char in name) and len(name.split(" ")) >= 2:
            break
        else:
            print("Invalid input.\nPlease try again...")
    return name


# Enter new birthdate
def input_new_birthdate():
    while True:
        try:
            birthday = input("Enter birthday (mm/dd/yyyy): ")
            check = int(birthday.replace("/", ""))
            if len(birthday) == 10 and int(birthday[:2]) <= 12 and int(birthday[3:5]) <= 31:
                break
            else:
                print("Invalid entry.\nPlease try again...")
        except ValueError:
            print("Unrecognised input.\nPlease try again...")
    return birthday


# Read file
def read_data_file(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


# Write to json
def write_data_file(filename, dictionary):
    with open(filename, "w") as f:
        json.dump(dictionary, f)


# Main function
def main():
    while True:
        dictionary = read_data_file("birthdays.json")
        print("\nWelcome to the birthday dictionary. We know the birthdays of:")
        for item in dictionary:
            print(item)
        choice = get_choice()
        if choice == 1:
            name = get_input(dictionary)
            print("{}'s birthday is {}.".format(name, dictionary[name]))
        elif choice == 2:
            name = input_new_name()
            birthday = input_new_birthdate()
            dictionary[name] = birthday
            write_data_file("birthdays.json", dictionary)
        else:
            break


# Run program
if __name__ == "__main__":
    main()

