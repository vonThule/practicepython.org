# Create a game class
class Game:
		def __init__(self):
				self.board = [[0, 0, 0],
						      [0, 0, 0],
						      [0, 0, 0]]
				self.print_board = [[" ", " ", " "],
								    [" ", " ", " "],
									[" ", " ", " "]]
				self.players = [1, 2]
				self.players_marks = ["X", "O"]
				self.empty = 9
				self.active_player = 0
				self.score = [0, 0]
				self.active = True
				self.round_winner = 0
		
		def reset_game(self):
				self.board = [[0, 0, 0],
						      [0, 0, 0],
							  [0, 0 ,0]]
				self.print_board = [[" ", " ", " "],
								    [" ", " ", " "],
									[" ", " ", " "]]
				self.empty = 9
				self.active = True
				self.active_player = 0
				self.round_winner = 0

		def place_move(self, row, column):
				if self.board[row - 1][column - 1] != 0:
						print("That position has already been played!")
				else:
						self.board[row - 1][column - 1] = self.players[self.active_player]
						self.print_board[row - 1][column - 1] = self.players_marks[self.active_player]
						self.empty -= 1
						continue_play = int(self.check_result())
						if continue_play != 0 and self.empty != 0:
								self.active = False
								self.score[continue_play - 1] += 1
								self.round_winner = continue_play
						else:
								self.check_moves()
						self.change_active_player()
		
		def check_result(self):
				if self.board[1][1] != 0:
						first_diagonal = set([self.board[0][0], self.board[1][1], self.board[2][2]])
						second_diagonal = set([self.board[0][2], self.board[1][1], self.board[2][0]])
						if len(first_diagonal) == 1 or len(second_diagonal) == 1:
								return self.board[1][1]
				transposed = zip(*self.board)
				game = self.board[:]
				for row in transposed:
						game.append(row)
				for row in game:
						row_set = set(row)
						if len(row_set) == 1 and row[0] != 0:
								return row[0]
				return 0

		def check_moves(self):
				if self.empty == 0:
						self.active = False
						self.round_winner = 0
						return False
				return True

		def print_game(self):
				horizontal = " --- --- --- "
				vertical = "| {} | {} | {} |"
				j = 0
				for i in range(1, 8):
						if i % 2 == 0:
								print(vertical.format(self.print_board[j][0], self.print_board[j][1], self.print_board[j][2]))
								j += 1
						else:
								print(horizontal)

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

		def print_score(self):
				print("\n===============================")
				print("|   Player 1   |   Player 2   |")
				print("===============================")
				print("|       {}      |       {}      |".format(self.score[0], self.score[1]))
				print("===============================\n")

		def run_game(self):
				self.print_game()
				player_input = self.get_input()
				self.place_move(player_input[0], player_input[1])


# Play again function
def play_again():
		while True:
				answer = input("Do you want to play again? (y/n) ")
				if answer.lower() != "y" and answer.lower() != "n":
						print("Unrecognised input.\nPlease try again...")
				else: 
						break
		return answer


# Main function
def main():
		game = Game()
		while True:
				while game.active:
						game.run_game()
				game.print_game()
				if game.check_moves() == False:
						print("\nOut of moves. GAME OVER!")
				else:
						if game.round_winner == 1 or game.round_winner == 2:
								print("\nPlayer {} WINS!".format(game.round_winner))
						else:
								print("\nIt's a draw!")
				game.print_score()
				again = play_again()
				if again == "n":
						break
				else:
						game.reset_game()


# Run program
if __name__ == "__main__":
		main()
