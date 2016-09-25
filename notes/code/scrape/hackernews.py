import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen("https://news.ycombinator.com/newest")
html = BeautifulSoup(response, "html.parser")

for link in html.find_all(class_="storylink"):
    print link['href'], link.text
