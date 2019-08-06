import sys
from bs4 import BeautifulSoup

def html2text(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text()
    return text

with open("/tmp/TeslaIPO.html", "r") as f:
    html_text = f.read()
tsla = html2text(html_text)

import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp(tsla[0:5000])

print([w for w in doc if w.like_num])
