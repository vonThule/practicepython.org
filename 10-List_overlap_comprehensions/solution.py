from random import randint, sample

# Two lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("List a: {}\nList b: {}".format(a, b))

# Output resulting intersection list
print("\n[Solution with generic lists]")
print([n for n in set(a) if n in b])

# Randomise two lists
num_elements = randint(10, 25)
num_range = range(1, randint(1, 100))
a = sample(num_range, num_elements if len(num_range) > num_elements else len(num_range))
num_elements = randint(10, 25)
num_range = range(1, randint(1, 100))
b = sample(num_range, num_elements if len(num_range) > num_elements else len(num_range))
print("\n\nList a: {}\nList b: {}".format(a, b))

# Second solution
print("\n[Solution with random lists]")
print([n for n in set(a) if n in b])


