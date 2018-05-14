# Get input from user and check if it's valid
def get_user_input():
		while True:
				try:
						number = int(input("Enter a number: "))
				except ValueError:
						print("You did not enter a number.\nPlease try again...")
				else:
						break
		return number


# Check primality
def is_prime(number):
		if number <= 1:
				return False
		elif number <= 3:
				return True
		elif number % 2 == 0 or number % 3 == 0:
				return False
		i = 5
		while i * i <= number:
				if number % i == 0 or number % (i + 2) == 0:
						return False
				i += 6
		return True


# Main function
def main():
		num = get_user_input()
		if is_prime(num):
				print("Number {} is a prime number.".format(num))
		else:
				print("Number {} is not a prime number.".format(num))


# Run program
if __name__ == "__main__":
		main()
