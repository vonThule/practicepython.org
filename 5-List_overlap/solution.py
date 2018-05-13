# Two lists as input
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13]

# Output the two lists
print("List a: {}".format(a))
print("List b: {}\n".format(b))

# Create a set, populate it and output the result
result = set()
for number in a:
		if number in b:
				result.add(number)

print("[First solution]\nIntersection of the two lists is: {}.\n".format(result))

# Print out intersection of two lists(oneliner)
print("[Second solution(oneliner)]\nIntersection of the two lists is: {}.".format(list(set(a).intersection(b))))

