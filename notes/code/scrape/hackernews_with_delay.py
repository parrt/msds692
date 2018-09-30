import requests
import time
import random
from bs4 import BeautifulSoup

def fetch(url,delay=(1,3)):
    """
    Simulate human random clicking x..y seconds then fetch URL.
    Returns the actual page source fetched and the HTML object.
    """
    time.sleep(random.randint(delay[0],delay[1])) # wait random seconds
    try:
        response = requests.get(url)
    except ValueError as e:
        print(str(e))
        return '', BeautifulSoup('', "html.parser")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return (html,soup)

html,soup = fetch("https://news.ycombinator.com/newest")
html = BeautifulSoup(html, "html.parser")

for link in html.find_all("a", {"class":"storylink"}):
        print(link['href'], link.text)
