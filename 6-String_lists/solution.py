# Take user input
string = input("Enter a string of characters: ")
while len(string) == 0:
		print("You did not provide an input.\nPlease try again...")
		string = input("Enter a string of characters: ")

# Check if string is palindrome and output result
# First solution
print("[Solution no 1]")
if string == string[::-1]:
		print("String {} is a palindrome.".format(string))
else:
		print("String {} is not a palindrome.".format(string))

# Second (iterative) solution using functions
print("\n[Solution no 2(iterative)]")

def is_palindrome(string):
		for i in range(0, len(string) // 2):
				if string[i] != string[len(string) - i - 1]:
						return False
		return True

if(is_palindrome(string)):
		print("String {} is a palindrome.".format(string))
else:
		print("String {} is not a palindrome.".format(string))

