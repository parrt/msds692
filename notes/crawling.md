# Learning to crawl

To crawl a webpage means to extract links of interest and then fetch those pages. A full web crawl would then look for links in those pages recursively until some termination condition is hit. Rather than build a full web crawl, let's build something that downloads the first page linked to from hacker news.

**Exercise**: Create a function called `crawl` that fetches pages specified in a `links` list. Store the output of each page as just `page`*n* in the specified output directory:

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
        response = requests.get(url, headers={'User-Agent': "Resistance is futile"}, timeout=1)
    except Exception as e:
        print(str(e))
        return '', BeautifulSoup('', "html.parser")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return (html,soup)
```

Upon exception, this will return an empty page rather than crashing the whole program.  The timeout (1s) is useful in case a page is not responding or responding incredibly slowly; it will fail instead of cause your program to wait forever.

[Solutions](https://github.com/parrt/msds692/tree/master/notes/code/scrape)

You can test your crawl function with something like:

```python
crawl(['https://news.ycombinator.com/'], "/tmp")
```

which will fetch the home page of hacker news, get all the embedded links, fetch the data at each one of those links and store the data in file `/tmp/pagei.html` for i=0..N-1 for N links. With a suitable main program:

```python
outputdir = sys.argv[1]
if not os.path.exists(outputdir):
    os.makedirs(outputdir)

links = parseHN()
print(links)
crawl(links, outputdir)
```

we can run that function from the terminal:

```bash
$ python crawlHN.py /tmp
...
```

## Getting more out of life

So far we've grabbed just the first page of news but let's figure out how to get multiple pages of news. We'll pull just 3 pages from Hacker News just so 50 students don't each start a loop that bangs their server and pisses them off.

Using "inspect element" in Chrome or your favorite browser, find the "More" link. It should look like:

```html
<a href="news?p=2" class="morelink" rel="next">More</a>
```

and then on that page, the "More" link should look like:

```html
<a href="news?p=3" class="morelink" rel="next">More</a>
```

**Exercise**: Write a script in `pageHN.py` that prints the list of links scraped from the *main page*, *page 2*, and *page 3* of Hacker News.   Navigate the site by fetching the "More" links. My output looks like:

```python
There are 30+30+30=90 links
https://www.cnbc.com/2021/08/11/bitcoin-family-hides-bitcoin-ethereum-and-litecoin-in-secret-vaults.html
https://iep.utm.edu/thrasymachus/
https://foreignpolicy.com/2018/08/15/botched-cia-communications-system-helped-blow-cover-chinese-agents-intelligence/
https://morsewall.com/random-quote-part-5-redux-thunk-using-various-front-end-stacks/
item?id=28147846
https://investor.opendoor.com/static-files/c78989fe-7029-4ad7-9923-f56e86353783
http://www.os2museum.com/wp/the-ibm-pc-41-years-ago/
...
```

Reuse your functionality from `parseHN()` from our prior `crawlHN.py` exercise to make a similar function to pull out the list of links using a beautiful soup object:

```python
def getlinks(url):
    "get story links and More link from a url"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    # for link in soup.find_all(class_="storylink"):
    # for link in soup.find_all("a", {"class":"storylink"}):
    for link in soup.find_all("a"):
        if 'class' in link.attrs:
            if link['class'] == ["storylink"]:
                links.append(link['href'])
    morelink = ...            
    return links, morelink
```

Then you can fetch multiple pages in sequence like:
 
```
links1,more = getlinks("https://news.ycombinator.com/newest")
links2,more = getlinks(f"https://news.ycombinator.com/{more}")
links3,more = getlinks(f"https://news.ycombinator.com/{more}")
links = links1 + links2 + links3
print(f"There are {len(links1)}+{len(links2)}+{len(links3)}={len(links)} links")
...
```    