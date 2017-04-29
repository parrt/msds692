import urllib2
from collections import defaultdict

from bs4 import BeautifulSoup

response = urllib2.urlopen("http://data1.cde.ca.gov/dataquest/Acnt2013/2013GrthStAPI.aspx")
soup = BeautifulSoup(response, "html.parser")

def get_table_headers(soup):
    headers = set()
    for h in soup.find_all('th', {'class': 'medium_center'}):
        s = ''
        for c in h.contents:
            if c.string:
                s += c.string.strip()
        if len(s)>0:
            headers.add(s)
    return headers

def get_table_rows_as_tuple_lists(soup):
    data = []
    for tbl in soup.find_all("table"):
        for row in tbl.find_all("tr"):
            datarow = []
            cols = row.find_all("td")
            rowname = cols[0].text.strip()
            # bug in soup gobbles too much so just grab first line of text
            rowname = rowname.split("\n")[0].strip()
            datarow.append(("rowname", rowname))
            for col in cols[1:]:
                if col.span:
                    colname = col.span['id'][len("lbl_"):].strip()
                    value = col.span.text.strip()
                    if len(value)>0:
                        datarow.append((colname, value))
            if len(datarow)==5:
                data.append(datarow)
    return data

def get_table_rows(soup):
    data = []
    for tbl in soup.find_all("table"):
        for row in tbl.find_all("tr"):
            datarow = []
            cols = row.find_all("td")
            rowname = cols[0].text.strip()
            # bug in soup gobbles too much so just grab first line of text
            rowname = rowname.split("\n")[0].strip()
            datarow.append(rowname)
            for col in cols[1:]:
                if col.span:
                    colname = col.span['id'][len("lbl_"):].strip()
                    value = col.span.text.strip()
                    if len(value)>0:
                        datarow.append(value)
            if len(datarow)==5:
                data.append(datarow)
    return data

print get_table_headers(soup)

allrows = get_table_rows(soup)
for row in allrows:
    print row
