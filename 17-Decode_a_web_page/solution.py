import requests
from bs4 import BeautifulSoup


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

for headline in data:
		print(headline)

