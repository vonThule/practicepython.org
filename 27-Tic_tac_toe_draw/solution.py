# Create a game class
class Game:
		def __init__(self):
				self.board = [[0, 0, 0],
						      [0, 0, 0],
						      [0, 0, 0]]
				self.players = ["X", "O"]
				self.empty = 9
				self.active_player = 0
		
		def place_move(self, row, column):
				if self.board[row - 1][column - 1] != 0:
						print("That position has already been played!")
				else:
						self.board[row - 1][column - 1] = self.players[self.active_player]
						self.empty -= 1
						self.change_active_player()
		
		def check_moves(self):
				if self.empty == 0:
						return False
				return True

		def print_game(self):
				for row in self.board:
						print(row)

		def change_active_player(self):
				if self.active_player == 0:
						self.active_player = 1
				else:
						self.active_player = 0

		# Get player input
		def get_input(self):
				while True:
						try:
								player_input = input("[Player {}] Enter coordinates: (row, column) ".format(self.active_player + 1)).split(",")
								if len(player_input) == 2:
										position = [int(player_input[0]), int(player_input[1])]
										break
								else:
										print("Input not recognised.\nPlease try again...")
						except ValueError:
								print("Input not recognised.\nPlease try again...")
				return position

		def run_game(self):
				self.print_game()
				player_input = self.get_input()
				self.place_move(player_input[0], player_input[1])


# Main function
def main():
		game = Game()
		while game.check_moves():
				game.run_game()
		game.print_game()
		print("Out of moves. GAME OVER!")


# Run program
if __name__ == "__main__":
		main()
