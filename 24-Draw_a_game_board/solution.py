# Draw horizontal parts of board
def draw_horizontal():
		print(" ---" * 3)


# Draw vertical parts of the board:
def draw_vertical():
		print("|   " * 4)


# Main function
def main():
		for i in range(1, 8):
				if i % 2 == 0:
						draw_vertical()
				else:
						draw_horizontal()


# Run program
if __name__ == "__main__":
		main()

