# Get number from user input
while True:
		try:
				number = int(input("Input a number: "))
		except ValueError:
				print("You didn't enter a number.\nPlease try again...")
		else:
				break

# Create a list of possible divisors
possible_divisor_list = list(range(1, number + 1))

# Get resulting list of divisors
result = []
for divisor in possible_divisor_list:
		if number % divisor == 0:
				result.append(divisor)

# Output the result
print("Number {} has following divisors: {}".format(number, result))

