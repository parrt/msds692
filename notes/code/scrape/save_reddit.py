import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.reddit.com/r/all", headers={'User-Agent': "Resistance is futile"})
with open("/tmp/t.html", "w") as f:
	f.write(response.text)
