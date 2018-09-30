import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/newest")
soup = BeautifulSoup(response.text, "html.parser")

# for link in soup.find_all(class_="storylink"):
for link in soup.find_all("a", {"class":"storylink"}):
        print(link['href'], link.text)
