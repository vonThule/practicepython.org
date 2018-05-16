# Read file
def read_file(filename):
		with open(filename, "r") as f:
				file_content = f.readlines()
		return [int(line.strip()) for line in file_content]


# Find overlapping numbers between two files
def find_overlap(file1, file2):
		result = []
		for number in file1:
				if number in file2:
						result.append(number)
		return result


# Main function
def main():
		primes = read_file("primenumbers.txt")
		happies = read_file("happynumbers.txt")
		print("Overlapping numbers:", find_overlap(primes, happies))


# Run program
if __name__ == "__main__":
		main()

