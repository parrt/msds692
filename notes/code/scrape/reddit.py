import urllib2

from bs4 import BeautifulSoup

req = urllib2.Request("https://www.reddit.com/r/all", headers={'User-Agent': "Resistance is futile"})
response = urllib2.urlopen(req)
html = BeautifulSoup(response, "html.parser")

for h in html.find_all('a', {'class': 'title may-blank outbound '}):
    print h.string