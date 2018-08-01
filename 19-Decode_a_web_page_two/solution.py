#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/15/2018
    Date last modified: 8/1/2018
    Python version: 3.6.5
    Description:
        Problem #19: Decode a Web Page Two from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""

import requests
from bs4 import BeautifulSoup


# Get website data
def get_website_data(url):
    r = requests.get(url)
    return r.text


# Process website data with beautiful soup
def get_article(website_data):
    soup = BeautifulSoup(website_data, "html.parser")
    data = []
    data.append(soup.find("h1", {"data-reactid": "168"}).text)
    data.append(soup.find("span", {"data-reactid": "170"}).text)
    article_tags = soup.find_all("section", {"class": "content-section"})
    for tag in article_tags:
        for element in tag.find_all("p"):
            data.append(element.text.strip())
    return data[:-1]


# Main function
def main():
    url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    website_data = get_website_data(url)
    article_data = get_article(website_data)
    for item in article_data:
        print(item)


# Run program
if __name__ == "__main__":
    main()
