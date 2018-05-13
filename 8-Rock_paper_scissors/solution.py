# Get user choice function
def player_choice(player):
		print("[{}]:".format(player))
		print("1. Rock\n2. Paper\n3. Scissors\n4. Quit")
		while True:
				try:
						player_input = int(input("Your choice >>> "))
				except ValueError:
						print("You didn't input the proper choice.\nPlease try again...")
				else:
						break
		return player_input


# Check result function
def check_result(pl1choice, pl2choice):
		if pl1choice == 1 and pl2choice == 2:
				return 2
		elif pl1choice == 1 and pl2choice == 3:
				return 1
		elif pl1choice == 2 and pl2choice == 1:
				return 1
		elif pl1choice == 2 and pl2choice == 3:
				return 2
		elif pl1choice == 3 and pl2choice == 1:
				return 2
		elif pl1choice ==3 and pl2choice == 2:
				return 1
		else:
				return 0


# Display result function
def display_result(result):
		if result == 1:
				print("Player 1 wins!")
		elif result == 2:
				print("Player 2 wins!")
		else:
				print("It's a draw!")
		while True:
				new = input("New game? (y/n) >> ")
				if new != "y" and new != "n":
						print("You didn't input the right choice.\nPlease try again...")
				else:
						break
		return new


# Main function
def main():
		while True:
				pl1 = player_choice("Player 1")
				if pl1 == 4:
						break
				pl2 = player_choice("Player 2")
				if pl2 == 4:
						break
				result = check_result(pl1, pl2)
				end = display_result(result)
				if end == "n":
						break


# Run program
if __name__ == "__main__":
		main()

