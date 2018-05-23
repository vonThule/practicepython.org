#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
		File name: solution.py
		Author: Alexander Popp
		Date created: 5/13/2018
		Date last modified: 5/23/2018
		Python version: 3.4.6
		Description:
				Problem #9: Guessing Game One from http://www.practicepython.org
				For detailed description of the problem see the accompanying
				file named 'problem.txt' or refer to the aformentioned website.
"""


from random import randint


# Generate random number function
def generate_random():
		return randint(1, 9)


# Get user input function
def get_input():
		while True:
				user_input = input("\nGuess a number from 1 to 9 or type 'exit' to quit: ")
				if user_input == "exit":
						break
				# Check if user_input is a number between 1 and 9
				try:
						if int(user_input) > 0 and int(user_input) < 10:
								break
						else:
								print("You must enter a number between 1 and 9.\nPlease try again...")
				# If user_input is not a number catch exception and inform user
				except ValueError:
						print("You did not enter a proper choice.\nPlease try again...")
		return user_input


# Ask for another game
def play_again():
		while True:
				again = input("Play again? (y/n) ")
				# Check if answer is valid
				if again.lower() != "y" and again.lower() != "n":
						print("Wrong input. You must enter either 'y' or 'n'.\nPlease try again...")
				else:
						break
		if again.lower() == "n":
				return False
		return True


# Game function
def game(random_number):
		# Keep track of number of guesses
		counter = 1
		while True:
				user_choice = get_input()
				# If user types 'exit' break game
				if user_choice == "exit":
						break
				# Check guesses and display proper information
				elif int(user_choice) == random_number:
						print("You guessed correct. The number is {} and it took you {} tries.".format(random_number, counter))
						break
				elif int(user_choice) < random_number:
						print("You guessed lower. Guess again...")
				else:
						print("You guessed higer. Guess again...")
				# If number was not guessed correctly, increase count of tries
				counter += 1


# Main function
def main():
		print("\n=========================================")
		print("||            GUESSING GAME            ||")
		print("=========================================")
		while True:
				random_number = generate_random()
				game(random_number)
				# If player does not want another game, exit
				if not play_again():
						break
		print("Goodbye.")


# Run program
if __name__ == "__main__":
		main()

