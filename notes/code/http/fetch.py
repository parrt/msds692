import requests
from bs4 import BeautifulSoup

response = requests.get("https://docs.python.org/2/howto/urllib2.html")
html = response.content

soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

print text