"""
Problem no 3, from htttp://www.practicepython.org
Take a list, for example: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that
are less than 5.
Extras:
		- Instead of printing the elements one by one, make a new
		list that has all the elements less than 5 from this list
		in it and print out this new list.
		- Write this in one line of Python.
		- Ask the user for a number and return a list that contains
		only elements from the original list, a, that are smaller
		than that number given by the user.
"""


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("Original list:", a)

# 1. Print out all elements less than 5
print("Elements that are less than 5:")
for element in a:
		if element < 5:
				print(element)


# 2. Make a new list of elements less than 5 and print it
new_list = []
for element in a:
		if element < 5:
				new_list.append(element)

print("List of elements less than 5:", new_list)

# 3. Make a new list of elements less than 5 and print it(one liner)
print("List of elements less than 5(oneliner):", [element for element in a if element < 5])

print("\n")
# 4. Ask user for input and print a list that contains elements smaller
# than the users number

# Get user input
while True:
		try:
				number = int(input("Enter a number: "))
		except ValueError:
				print("You did not enter a number.\nPlease try again...")
		else:
				break

# Check condition and print
print("List of elements less than number {}: {}".format(number, [element for element in a if element < number]))

