import requests
import time
import random
from bs4 import BeautifulSoup
import sys, os

def getlinks(url):
    "get story links and More link from a url"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    # for link in soup.find_all(class_="storylink"):
    # for link in soup.find_all("a", {"class":"storylink"}):
    for link in soup.find_all("a"):
        if 'class' in link.attrs:
            if link['class'] == ["storylink"]:
                links.append(link['href'])

    more = soup.find("a", {"class": "morelink"})
    return links, more['href']

links1,more = getlinks("https://news.ycombinator.com/newest")
links2,more = getlinks(f"https://news.ycombinator.com/{more}")
links3,more = getlinks(f"https://news.ycombinator.com/{more}")

links = links1 + links2 + links3
print(f"There are {len(links1)}+{len(links2)}+{len(links3)}={len(links)} links")
for link in links:
    print(link)

