import urllib2
from collections import defaultdict

from bs4 import BeautifulSoup

response = urllib2.urlopen("http://data1.cde.ca.gov/dataquest/Acnt2013/2013GrthStAPI.aspx")
html = BeautifulSoup(response, "html.parser")

def get_table_headers():
    headers = []
    for h in html.find_all('th', {'class': 'medium_center'}):
        s = ''
        for c in h.contents:
            if c.string:
                s += c.string.strip()
        if len(s)>0:
            headers.append(s)
    return headers

def get_table_rows():
    # this finds all "lbl_*" tags
    data = defaultdict(list)
    for h in html.find_all(lambda tag : tag.name=='span' and tag.has_attr('id') and tag['id'][0:4]=='lbl_'):
        print h

print get_table_headers()

print get_table_rows()