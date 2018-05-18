import random


# Load a word list file
def get_data(filename):
		with open(filename, "r") as f:
				file_data = f.readlines()
		return [line.strip() for line in file_data]


# Pick random word
def pick_word(words):
		return words[random.randint(0, len(words) - 1)]


# Main function
def main():
		word = pick_word(get_data("words.txt"))
		print("Randomly picked word:", word)


# Run program
if __name__ == "__main__":
		main()

