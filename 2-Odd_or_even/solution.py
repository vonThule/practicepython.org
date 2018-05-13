"""
Problem #2, from http://www.practicepython.org

Ask the user for a number. Depending on whether the number is even
or odd, print out an appropriate message to the user.
Extras:
		- If the number is a multiple of 4, print out
		a different message.
		- Ask the user for two numbers: one number to
		check (call it num) and one number to divide
		by (check). If check divides evenly into num,
		tell that to the user. If not, print a different
		appropriate message.
"""

# Get user input and make shure input is a valid number
while True:
		try:
				number = int(input("Enter a number: "))
		except ValueError:
				print("You did not enter a number.\nPlease try again...")
		else:
				break

# Check if number is even or odd
if number % 2 == 0:
		print("Your number is even!")
else:
		print("Your number is odd!")

# Check if number is a multiple of 4
if number % 4 == 0:
		print("Your number is a multiple of 4!")

print("\n\n")
# Get two user inputs and make shure they are valid numbers
while True:
		try:
				num = int(input("Enter first number: "))
		except ValueError:
				print("You did not enter a number.\nPlease try again...")
		else:
				break

while True:
		try:
				check = int(input("Enter second number: "))
		except ValueError:
				print("You did not enter a number.\nPlease try again...")
		else:
				break

# Check first mod second and display message
if num % check == 0:
		print("Number {} divides evenly by {}.".format(num, check))
else:
		print("Number {} does not divide evenly by {}.".format(num, check))


