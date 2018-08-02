#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    File name: solution.py
    Author: Alexander Popp
    Date created: 5/16/2018
    Date last modified: 8/2/2018
    Python version: 3.6.5
    Description:
        Problem #21: Write To a File from http://www.practicepython.org
        For detailed description of the problem see the accompanying
        file named 'problem.txt' or refer to the aformentioned website.
"""


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
    data = get_article_titles(website_data)
    filename = get_input() + ".txt"
    write_file(data, filename)


# Run program
if __name__ == "__main__":
    main()
