import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.amazon.com/gp/bestsellers/books/ref=sv_b_2"

r = requests.get(URL)
htmltext = r.text

soup = BeautifulSoup(htmltext, 'html.parser')

bestsellers = []
for item in soup.find_all(class_="zg_itemWrapper"):
    link = item.div.a
    img = link.div.img
    authtag = item.find(class_="a-size-small a-link-child")
    pricetag = item.find(class_="a-size-base a-color-price")
    price = pricetag.text
    ratingtag = item.find(class_="a-icon-alt")
    rating = ratingtag.text # 4.7 out of 5 stars
    words = rating.split(' ')
    rating = words[0]
    if authtag:
        auth = authtag.text
    else:
        auth = "unknown"
    info = [auth, img['alt'], price, rating, link['href']]
    bestsellers.append(info)

# ok, now write to a csv file in excel format
f = open("/tmp/bestsellers.csv", "w")
fw = csv.writer(f, dialect='excel')

fw.writerow(['author', 'title', 'price', 'rating', 'link'])
for book in bestsellers:
    fw.writerow(book)

f.close()
