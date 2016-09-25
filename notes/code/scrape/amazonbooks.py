import urllib2
from bs4 import BeautifulSoup

def parseAmazonBestSellers():
    req = urllib2.Request("https://www.amazon.com/gp/bestsellers/books/ref=sv_b_2",
                          headers={'User-Agent': "Resistance is futile"})
    response = urllib2.urlopen(req)
    html = BeautifulSoup(response, "html.parser")

    books = []
    for item in html.find_all(class_="zg_itemWrapper"):
        link = item.find(class_="zg_title").a
        price = item.find(class_="price").string.strip()
        href = link['href'].strip()
        title = link.string.strip()
        author = item.find(class_="zg_byline").string.strip()
        books.append((price, title, author, href))

    return books

books = parseAmazonBestSellers()
for b in books:
    print b
