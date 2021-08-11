import requests
from bs4 import BeautifulSoup

""" Use this while testing:
with open("/tmp/t.html") as f:
	html = f.read()
"""

response = requests.get("https://www.reddit.com/r/all", headers={'User-Agent': "Resistance is futile"})
#response = requests.get("https://www.reddit.com/r/all") # doesn't work without the user agent
html = response.text
#print(html)

soup = BeautifulSoup(html, "html.parser")

for h in soup.find_all('a'):
    #print(h.attrs)
    if 'href' in h.attrs and 'data-click-id' in h.attrs:
        if h.attrs['href'].startswith('/r/') and h.attrs['data-click-id']=='comments':
            print("href: "+h.attrs['href'])

