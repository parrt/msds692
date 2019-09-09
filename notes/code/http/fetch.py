import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
html = response.content

soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

print(text)
