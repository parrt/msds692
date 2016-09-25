# Collecting data from web pages

We already know how to fetch a webpage using `urlopen()`. The question is: How do we extract useful information from the HTML. We are going to use BeautifulSoup again to parse the HTML and then search for elements of interest.

## Baby steps

**Exercise**: Go grab the latest news from Hacker News, part of the Y Combinator startup incubator: `https://news.ycombinator.com/newest`. Parse the data with BeautifulSoup and then find all of the links to news.  You can either look at the page source in your browser to see what HTML renders those links or you can use chrome browser. Right-click over one of the links and say "inspect". It will show you the HTML associated with that link:

<img src=figures/hn-element.png width=500>

Noticed that the link has a CSS class: `class="storylink"`. Wow. Now that is convenient. Figure out how to get BeautifulSoup to search for all tags that have that CSS class then print the link and link text:

```python
for link in html.find_all(...):
    print link['href'], link.text
```

## Mimicking a "human using a browser"

Many websites would prefer that you did not scrape their data using a program, so we have to mimic a human. There are two key elements:

1. varying the amount of time in between fetches to that server
2. specifying a header that indicates we are a browser. I use: `User-Agent: Resistance is futile`  (haha)

**Exercise**: Alter your script to use a new function called `fetch` that waits a random amount of time in between two integer number of seconds:

```python
def fetch(url,delay=(2,5)):
    """
    Simulate human random clicking 2..5 seconds then fetch URL.
    Returns the actual page source fetched and the HTML object.
    """
    time.sleep(random.randint(delay[0],delay[1])) # wait random seconds
    ... fetch data from URL and parse with beautiful soup ...
    return (pagedata,html)
```

Of course, you have to alter your code that does the `urlopen` to call this function now instead. This is a way to guarantee that we don't pound somebody's server and get cut off. It's also a good example of a failsafe (given example from jguru with email on/off switch at the outgoing SMTP client).

Verify that you can still get the hacker news page.

Next, we need to pretend to be a browser, which means setting a header that goes out with the HTTP protocol to the remote server. For example, if you view this URL in your browser, it's no problem but a regular `urlopen` will get a 403 permissions error from the server:

[Sample link requiring a `User-Agent` header](http://www.chronicle.com/article/When-Analogies-Fail/237716)

**Exercise**: Alter `fetch` so that it creates a `urllib2.Request` object for the `url` parameter and sets header/value pair:

```
User-Agent: Resistance is futile
```

or some other header value. Use `urlopen` on that object not the plain `url`.

Verify that you can still get the hacker news page.


**Exercise**:  Create a function that extracts all of the news links and put into a list, rather than printing them out.

```python
def parseHN():
    page,html = fetch("https://news.ycombinator.com/newest")
    links = ...
    return links
```

## Learning to crawl

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