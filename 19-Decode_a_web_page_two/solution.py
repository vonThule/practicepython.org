import requests
from bs4 import BeautifulSoup


# Get website data
url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
website_data = r.text

soup = BeautifulSoup(website_data, "html5lib")
data = []
data.append(soup.find("h1", {"data-reactid": "169"}).text)
data.append(soup.find("span", {"data-reactid": "171"}).text)
article_tags = soup.find_all("section", {"class": "content-section"})
for tag in article_tags:
		for element in tag.find_all("p"):
				data.append(element.text.strip())
		
data = data[:-1]

for item in data:
		print(item)

