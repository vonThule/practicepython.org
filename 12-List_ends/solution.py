# Define a list
a = [5, 10, 15, 20, 25]

# Make new list from first and last elements of original
def list_ends(lst):
		return [lst[0], lst[-1]]


# Main function
def main():
		print("Original list:", a)
		print("List made from first and last elements of the original:", list_ends(a))


# Run program
if __name__ == "__main__":
		main()
