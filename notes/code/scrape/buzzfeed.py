import requests
from bs4 import BeautifulSoup
from collections import defaultdict

def parseBF():
    response = requests.get("https://www.buzzfeed.com/")
    soup = BeautifulSoup(response.text, "html.parser")

    def f(tag): return tag.name=='a' and 'data-bfa' in tag.attrs

    topics = defaultdict(set)
    #for link in soup.findAll(lambda tag: tag.name=='a' and 'data-bfa' in tag.attrs):
    for link in soup.findAll(f):
        attr = link['data-bfa']
        if not 'post_category' in attr: continue
        values = attr.split(',')
        topic = [v.split(':')[1] for v in values if v.startswith('post_category')]
        topic = topic[0]
        # print topic, link['href']
        topics[topic].add(link['href'])
    return topics

topics = parseBF()
for t in topics:
    print(t)
    print('\t'+'\n\t'.join(topics[t]))
