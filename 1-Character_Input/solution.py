"""
Problem #1, from: http://www.practicepython.org
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that
they will turn 100 years old.
Extras:
		- Add on to the previous program by asking the user
		for another number and printing out that many copies
		of the previous message.
		- Print out that many copies of the previous message
		on separte lines.
"""

import datetime


# Get user name
name = input("Enter your name: ")
while len(name) == 0:
		print("You did not enter a name.\nPlease try again...")
		name = input("Enter your name: ")

# Get user age
while True:
		try:
				age = int(input("Enter your age: "))
		except ValueError:
				print("Fail! You did not enter correct age value.")
				print("Please try again...")
		else:
				break

# Get number of repeats for message
# If out of scope, ask for input again
while True:
		try:
				repeats = int(input("Enter a number from 1 to 20: "))
				while repeats <= 0 or repeats > 20:
						print("Your number is out of scope.\nPlease try again...")
						repeats = int(input("Enter a number from 1 to 20: "))
		except ValueError:
				print("Fail! You did not enter a number.")
				print("Please try again...")
		else:
				break

# Calculate difference between users age and 100
years_to_hundred = 100 - age
# Get current year
current_year = datetime.datetime.now().year
# Calculate result
result = current_year + years_to_hundred

# Display result n number of times
for n in range(0, repeats):
		print("Hello, {}! You will turn 100 in the year {}.".format(name, result))

