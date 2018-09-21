"""
Given an IP address or machine name, pull in the list of articles
from the root / URL.  Collect the list of links and compare to the
known title/URLs.  Pull in a sample of article pages and compare
the recommended article title/URLs.
"""
import sys
from bs4 import BeautifulSoup
import requests
import pickle

artlist = [
    "business/007.txt",
    "business/025.txt",
    "business/131.txt",
    "business/223.txt",
    "entertainment/157.txt",
    "entertainment/153.txt",
    "entertainment/356.txt",
    "politics/242.txt",
    "sport/103.txt",
    "sport/364.txt",
    "tech/339.txt",
    "tech/384.txt",
    "tech/387.txt"
]

agent = {'User-agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}

def fetch_article_list():
    host = getIP()

    r = requests.get("http://"+host, headers=agent)
    links = []
    soup = BeautifulSoup(r.text, "lxml")
    for link in soup.findAll('a'):
        links.append( (link.get('href').strip(), link.text.strip()) )
    return links


def fetch_sample_articles(artlist):
    host = getIP()

    articles = []
    for url in artlist:
        r = requests.get("http://"+host+"/article/"+url, headers=agent)
        soup = BeautifulSoup(r.text, "lxml")
        links = []
        for link in soup.findAll('a'):
            links.append((link.get('href').strip(), link.text.strip()))
        articles.append( (url.strip(), links) )
    return articles


def test_links():
    host = sys.argv[len(sys.argv) - 1]  # host is last arg
    print("TESTING article list at " + host)

    f = open('articles.pkl', 'rb')
    true_links = set(pickle.load(f))
    f.close()
    links = set(fetch_article_list())
    if links!=true_links:
        if links.issubset(true_links):
            assert False, "FAIL: article links missing: "+str(true_links.difference(links))
        if links.issuperset(true_links):
            assert False, "FAIL: article links has extra: "+str(links.difference(true_links))
    print("Article links OK")


def test_sample_articles():
    host = sys.argv[len(sys.argv) - 1]  # host is last arg
    print("TESTING Recommended articles at " + host)

    f = open('recommended.pkl', 'rb')
    true_recommended = pickle.load(f)
    f.close()
    recommended = fetch_sample_articles(artlist)
    for i in range(len(recommended)):
        art = recommended[i]
        true_art = true_recommended[i]
        assert art[0]==true_art[0]
        links = set(art[1])
        true_links = set(true_art[1])
        if links != true_links:
            if links.issubset(true_links):
                assert False, "FAIL: recommended articles missing: "+str(true_links.difference(links))
            if links.issuperset(true_links):
                assert False, "FAIL: recommended articles has extra: "+str(links.difference(true_links))

    print("Recommended articles OK")


def getIP():
    with open("IP.txt") as f:
        host = f.read().strip()
        if not host.index(':'):
            host += ':5000'
    return host
