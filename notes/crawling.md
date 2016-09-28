# Learning to crawl

To crawl a webpage means to extract links of interest and then fetch those pages. A full web crawl would then look for links in those pages recursively until some termination condition is hit. Rather than build a full web crawl, let's build something that downloads the first page linked to from hacker news.

**Exercise**: Create a function that fetches pages specified in a `links` list. Store the output of each page as just `page`*n* in the specified output directory:

```python
def crawl(links, outputdir):
    for link in links:
        page,html = fetch(link,delay=(0,0)) # no need to delay; pulling from random sites
        .. save page into file outputdir/pagen ...
```

As you try to crawl the links from hacker news, inevitably one of them will be bad and so we must check for this so the program doesn't crash. Python will "raise an exception" upon bad URL and so we need to catch that exception.

**Exercise**: Alter your `fetch` function so that the `urlopen` is wrapped in a `raise`...`except`:

```python
    try:
        request = urllib2.Request(...)
        response = urllib2.urlopen(req)
    except ValueError as e:
        print str(e)
        return '', BeautifulSoup('', "html.parser")
```

Upon exception, this will return an empty page rather than crashing the whole program.

## Getting more out of life

So far we've grabbed just one page of news but let's figure out how to get multiple pages. We'll pull just 3 pages from Hacker News just so 35 students don't each start a loop that bangs their server and pisses them off.

Using "inspect element" in Chrome or your favorite browser, find the "More" link. It should look like:

```html
<a href="news?p=2" class="morelink" rel="nofollow">More</a>
```

and then on that page, the "More" link should look like:

```html
<a href="news?p=3" class="morelink" rel="nofollow">More</a>
```

**Exercise**: Create a function that returns a list of links scraped from the first 3 pages (just 3 please) of Hacker News.
