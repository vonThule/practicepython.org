#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/15/2018
    Date last modified: 5/30/2018
    Python version: 3.6.5
    Description:
        Problem #17: Decode a Web Page from http://www.practicepython.org
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
def get_article_titles(website_data):
    soup = BeautifulSoup(website_data, "html.parser")
    article_tag = soup.find_all("article", {"class": "story"})
    headlines = []
    for tag in article_tag:
        for element in tag.find_all("h2", {"class": "story-heading"}):
            headlines.append(element.text.strip())
    return headlines


# Main function
def main():
    url = "http://www.nytimes.com"
    website_data = get_website_data(url)
    headlines = get_article_titles(website_data)
    for headline in headlines:
        print(headline)


# Run program
if __name__ == "__main__":
    main()

