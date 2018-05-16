import requests
from bs4 import BeautifulSoup


# Get user input
def get_input():
		while True:
				name = input("Type in the filename you would like to save to: ")
				if name.isalnum():
						break
				else:
						continue
		return name

# Write to file
def write_file(data, filename):
		counter = 0
		with open(filename, "w") as f:
				for item in data:
						f.write(item + "\n")
						counter += 1
		print("{} lines writen to {}".format(counter, filename))


# Get website data
url = "http://www.nytimes.com"
r = requests.get(url)
website_data = r.text

soup = BeautifulSoup(website_data, "html5lib")
article_tag = soup.find_all("article", {"class": "story"})
data = []
for tag in article_tag:
		for element in tag.find_all("h2", {"class": "story-heading"}):
				data.append(element.text.strip())

filename = get_input() + ".txt"
write_file(data, filename)

