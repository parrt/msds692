import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.amazon.com/gp/bestsellers/books"
r = requests.get(URL, headers={'User-Agent': "Resistance is futile"})
htmltext = r.text
print(htmltext)

""" Test with this:
with open("/tmp/t.html") as f:
    htmltext = f.read()
"""

htmltext = htmltext.strip()
soup = BeautifulSoup(htmltext, 'lxml') # 'html.parser' doesn't work here!

bestsellers = []
for item in soup.find_all('span', {'class':"aok-inline-block zg-item"}):
    # Link
    link = item.a

    # Image
    img = link.div.img

    # Author
    'Author like this: <span class ="a-size-small a-color-base" >Craig Smith</span>'
    'OR <a class="a-size-small a-link-child" ...>Bob Woodward</a>'
    authtag = item.find(class_="a-size-small a-color-base")
    if not authtag:
        authtag = item.find(class_="a-size-small a-link-child")
    if authtag:
        auth = authtag.text
    else:
        auth = "unknown"

    # Price
    pricetag = item.find(class_="a-size-base a-color-price")
    price = pricetag.text

    # Rating
    ratingtag = item.find(class_="a-icon-alt")
    rating = None
    if ratingtag:
        rating = ratingtag.text # 4.7 out of 5 stars
        words = rating.split(' ')
        rating = words[0]

    # Pack together as tuple
    info = (auth, img['alt'], price, rating, link['href'])
    bestsellers.append(info)

# ok, now write to a csv file in excel format
filename = "/tmp/bestsellers.csv"
with open(filename, "w") as f:
    fw = csv.writer(f, dialect='excel')
    fw.writerow(['author', 'title', 'price', 'rating', 'link'])
    for book in bestsellers:
        fw.writerow(book)

print(f"Wrote {filename}")
