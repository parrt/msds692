import requests
from bs4 import BeautifulSoup
from collections import defaultdict

def parseBF():
    response = requests.get("https://www.buzzfeed.com/news")
    html = BeautifulSoup(response.text, "html.parser")

    topics = defaultdict(list)
    for link in html.find_all('a', {'rel:gt_act':'post/title'}):
        if 'rel:gt_label' in link.attrs:
            topic = link.attrs['rel:gt_label']
            topics[topic].append(link['href'])
            # print link['href'], link.attrs['rel:gt_label'], link.text
        else:
            topics['topstories'].append(link['href'])
            # print '###', link['href'], link.text
    return topics

"""
<a href="/katherinemiller/obama-jokes-i-am-so-relieved-that-the-birther-thing-is-over"
data-bfa="@a:Title;@d:politics;" rel:gt_act="post/title" rel:gt_label="politics" class="xs-block link-gray">Obama Jokes: "I Am So Relieved That The Birther Thing Is Over"</a>
"""

topics = parseBF()
for t in topics:
    print t
    print '\t'+'\n\t'.join(topics[t])
