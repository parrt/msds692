import urllib2
from bs4 import BeautifulSoup

response = urllib2.urlopen("https://docs.python.org/2/howto/urllib2.html")
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

print text