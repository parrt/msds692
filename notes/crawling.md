# Learning to crawl

To crawl a webpage means to extract links of interest and then fetch those pages. A full web crawl would then look for links in those pages recursively until some termination condition is hit. Rather than build a full web crawl, let's build something that downloads the first page linked to from hacker news.

**Exercise**: Create a function that fetches pages specified in a `links` list. Store the output of each page as just `page`*n* in the specified output directory:

```python
def crawl(links, outputdir):
    N = 0
    for link in links:
        # no need to delay; pulling from random sites
        page,html = fetch(link,delay=(0,0)) 
        ... save page into file outputdir/pageN.html ...
        N += 1
```

As you try to crawl the links from hacker news, inevitably one of them will be bad and so we must check for this so the program doesn't crash. Python will "raise an exception" upon bad URL and so we need to catch that exception. Make sure your `fetch` function wraps the `get()` in a `raise`...`except`:

```python
    try:
        response = requests.get(url, headers={'User-Agent': "Resistance is futile"})
    except ValueError as e:
        print(str(e))
        return '', BeautifulSoup('', "html.parser")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return (html,soup)
```

Upon exception, this will return an empty page rather than crashing the whole program. [Solutions](https://github.com/parrt/msds692/tree/master/notes/code/scrape)

You can test your program with something like:

```python
crawl(['https://news.ycombinator.com/'], "/tmp")
```

which will fetch the home page of hacker news, get all the embedded links, fetch the data at each one of those links and store the data in file `/tmp/pagei.html` for i=0..N-1 for N links.

## Getting more out of life

So far we've grabbed just the first page of news but let's figure out how to get multiple pages. We'll pull just 3 pages from Hacker News just so 50 students don't each start a loop that bangs their server and pisses them off.

Using "inspect element" in Chrome or your favorite browser, find the "More" link. It should look like:

```html
<a href="news?p=2" class="morelink" rel="nofollow">More</a>
```

and then on that page, the "More" link should look like:

```html
<a href="news?p=3" class="morelink" rel="nofollow">More</a>
```

**Exercise**: Write a script in `pageHN.py` that prints the list of links scraped from *page 2* and *page 3* of Hacker News.  Reuse your functionality from `parseHN` from our prior exercise to make a similar function to pull out the list of links from a beautiful soup object:

```python
# get links from html (soup) tree
def getlinks(soup):
    links = []
    for link in soup.find_all(class_="storylink"):
        links.append(link['href'])
    return links

def getmorelink(soup):
    find tag with "morelink" class in tree
    get "href" attribute from that tag
    combine with "https://news.ycombinator.com/" and return

# Get main page
response = requests.get("https://news.ycombinator.com",
                        params={'User-Agent': "Resistance is futile"})
soup = BeautifulSoup(response.text, "html.parser")
morelink = getmorelink(soup) # what is URL of the next page?

# Get page 2
response = requests.get(morelink, params={'User-Agent': "Resistance is futile"})
soup = ...
links = getlinks(soup)
print "PAGE 2"
print links
morelink = ...

# Get page 2
...
print "PAGE 3"
print links
```
