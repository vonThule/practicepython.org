# Get user input
def get_input():
		while True:
				try:
						user_input = input("Enter three numbers separated by comas: ").split(",")
						numbers = list(map(int, user_input))
						if len(numbers) == 3:
								break
						else:
								print("You did not enter three numbers.\nPlease try again...")
				except ValueError:
						print("Unrecognised input.\nPlease try again...")
		return numbers


# Get max value
def get_max(numbers):
		maximum = 0
		for number in numbers:
				if number > maximum:
						maximum = number
		return maximum


# Main function
def main():
		numbers = get_input()
		result = get_max(numbers)
		print("The largest number of {} is {}".format(numbers, result))


# Run program
if __name__ == "__main__":
		main()

