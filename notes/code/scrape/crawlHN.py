import requests
import time
import random
from bs4 import BeautifulSoup
import sys, os

def fetch(url,delay=(1,3)):
    """
    Simulate human random clicking x..y seconds then fetch URL.
    Returns the actual page source fetched and the HTML object.
    """
    time.sleep(random.randint(delay[0],delay[1])) # wait random seconds
    try:
        response = requests.get(url, headers={'User-Agent': "Resistance is futile"})
    except ValueError as e:
        print(str(e))
        return '', BeautifulSoup('', "html.parser")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return (html,soup)

def crawl(links, outputdir):
    i = 0
    for link in links:
        page,html = fetch(link,delay=(0,0)) # no need to delay; pulling from random sites
        filename = f"page{i}.html"
        i += 1
        print("Writing {filename}")
        with open(os.path.join(outputdir,filename), "w") as f:
            f.write(page)

def parseHN():
    page,html = fetch("https://news.ycombinator.com/newest")
    links = []
    for link in html.find_all(class_="storylink"):
        links.append(link['href'])

    return links

outputdir = sys.argv[1]
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

links = parseHN()
print(links)
crawl(links, outputdir)
