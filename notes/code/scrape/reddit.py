import requests

from bs4 import BeautifulSoup

response = requests.get("https://www.reddit.com/r/all", params={'User-Agent': "Resistance is futile"})
html = BeautifulSoup(response.content, "html.parser")

for h in html.find_all('a', {'class': 'title may-blank outbound '}):
    print h.string