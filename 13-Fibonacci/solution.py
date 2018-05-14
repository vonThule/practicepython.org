# Get user input
def get_input():
		while True:
				try:
						number = int(input("How many Fibonacci numbers do you want to generate: "))
				except ValueError:
						print("You did not enter a number.\nPlease try again...")
				else:
						break
		return number


# Generate fibonacci number
def fibonacci(n):
		if n == 0 or n == 1:
				return n
		return fibonacci(n - 1) + fibonacci(n - 2)


# Create a sequnce of numbers
def get_fibonacci_sequence(n):
		result = []
		for i in range(1, n + 1):
				result.append(fibonacci(i))
		return result


# Main function
def main():
		number = get_input()
		result = get_fibonacci_sequence(number)
		print("The resulting sequence of numbers is:", result)


# Run program
if __name__ == "__main__":
		main()

