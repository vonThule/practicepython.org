# Load a file
def load_file(filename):
		with open(filename, "r") as f:
				file_content = f.readlines()
		return [line.strip() for line in file_content]


# Create name count dictionary
def count_names(data):
		name_count = {}
		for name in data:
				if name not in name_count:
						name_count[name] = 1
				else:
						name_count[name] += 1
		return name_count


# Create category count dictionary
def count_categories(data):
		category_count = {}
		for category in data:
				cat = category.split("/")[2]
				if cat not in category_count:
						category_count[cat] = 1
				else:
						category_count[cat] += 1
		return category_count

# Main function
def main():
		name_data = load_file("nameslist.txt")
		category_data = load_file("Training_01.txt")
		name_count = count_names(name_data)
		category_count = count_categories(category_data)
		print(name_count)
		print(category_count)


# Run program
if __name__ == "__main__":
		main()

