import urllib2
import time
import random
from bs4 import BeautifulSoup
import sys, os, urlparse

def fetch(url,delay=(2,5)):
    """Simulate human random clicking 2..5 seconds then fetch URL"""
    time.sleep(random.randint(delay[0],delay[1])) # wait random seconds
    try:
        req = urllib2.Request(url, headers={'User-Agent': "Resistance is futile"})
        response = urllib2.urlopen(req)
    except ValueError as e:
        print str(e)
        return '', BeautifulSoup('', "html.parser")
    page = response.read()
    html = BeautifulSoup(page, "html.parser")
    return (page,html)

def crawl(links, outputdir):
    i = 0
    for link in links:
        page,html = fetch(link,delay=(0,0)) # no need to delay; pulling from random sites
        filename = "page%s" % i
        i += 1
        f = open(os.path.join(outputdir,filename), "w")
        f.write(page)
        f.close()

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
print links
crawl(links, outputdir)


