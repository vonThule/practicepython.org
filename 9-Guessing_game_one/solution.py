from random import randint


# Generate random number function
def generate_random():
		return randint(1, 9)


# Get user input function
def get_input():
		while True:
				user_input = input("Guess a number from 1 to 9 or type 'exit' to quit: ")
				if user_input == "exit":
						break
				try:
						if int(user_input) > 0 and int(user_input) < 10:
								break
				except ValueError:
						print("You did not enter a proper choice.\nPlease try again...")
		return user_input


# Main function
def main():
		counter = 0
		while True:
				random_number = generate_random()
				print("Debug:", random_number)
				user_choice = get_input()
				if user_choice == "exit":
						break
				if int(user_choice) == random_number:
						print("You guessed correct. The number is: {}.".format(random_number))
						counter += 1
				else:
						print("You did not guess correct. The number is: {}.".format(random_number))
				again = input("Play again? (y/n) >> ")
				while True:
						if again.lower() != "y" and again.lower() != "n":
								print("Wrong choice.\nPlease try again...")
						else:
								break
				if again.lower() == "n":
						break
		print("Goodbye. Your had {} correct guesses!".format(counter))


# Run program
if __name__ == "__main__":
		main()

