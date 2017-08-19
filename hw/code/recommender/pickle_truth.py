"""
Create the set of ground truth for the list of articles and a sample set
of articles. Pickle the (url,title) and (url,[recommended (url,title)]).
"""
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


def fetch_article_list(host):
    r = requests.get("http://"+host)
    links = []
    soup = BeautifulSoup(r.text, "lxml")
    for link in soup.findAll('a'):
        links.append( (link.get('href').strip(), link.text.strip()) )
    return links


def fetch_sample_articles(host, artlist):
    articles = []
    for url in artlist:
        r = requests.get("http://"+host+"/article/"+url)
        soup = BeautifulSoup(r.text, "lxml")
        links = []
        for link in soup.findAll('a'):
            links.append((link.get('href').strip(), link.text.strip()))
        articles.append( (url.strip(), links) )
    return articles


# get list of links
links = fetch_article_list("localhost")
output = open('articles.pkl', 'wb')
pickle.dump(links, output)
output.close()
print "Pickled list of %d article links" % len(links)

# get a sampling of articles
articles = fetch_sample_articles("localhost", artlist)
output = open('recommended.pkl', 'wb')
pickle.dump(articles, output)
output.close()
print "Pickled list of %d article pages each with 5 recommended links" % len(articles)
