# Collecting data from web pages

We already know how to fetch a webpage using `urlopen()`. The question is: How do we extract useful information from the HTML. We are going to use BeautifulSoup again to parse the HTML and then search for elements of interest.

[Lots of useful web scraping info here](https://automatetheboringstuff.com/chapter11/)

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


## Reddit

Ok, so Hacker News might shut us down. As a back up, you can scan [reddit news](https://www.reddit.com/r/all). To me it looks like links have `class="title may-blank outbound "`:

```html
<a class="title may-blank outbound "
 href="http://imgur.com/wJqUthV" 
 tabindex="1" 
 data-href-url="http://imgur.com/wJqUthV" 
 data-outbound-url="https://out.reddit.com/t3_54ts81?url=http%3A%2F%2Fimgur.com
%2FwJqUthV&amp;token=AQAAoh7rVw1w9L81tgHr_XrmvIA01bcGQyOcWWbvU9jNqgetktoX" 
data-outbound-expiration="1475026594000" 
rel="nofollow">My former teacher posted this today.
 Said that "they always hug like this"</a>
```

If you don't set the "user agent" (browser), you'll see this in response:

```bash
$ curl https://www.reddit.com/r/all
...
<p>we're sorry, but you appear to be a bot and we've seen too many requests
from you lately. we enforce a hard speed limit on requests that appear to come
from bots to prevent abuse.</p>

<p>if you are not a bot but are spoofing one via your browser's user agent
string: please change your user agent string to avoid seeing this message
again.</p>
```

## Extracting a table of data

Let's see if we can pull academic performance data from [2012-13 Accountability Progress Reporting (APR)](http://data1.cde.ca.gov/dataquest/Acnt2013/2013GrthStAPI.aspx).

**Exercise**: Create a list of lists representation for the `2013 Growth API` table and another for the `Number of Students Included in the 2013 Growth API` table. Or try list of dictionary representation.  Consider hardcoding the headers into your script or you can pull the headers too. *This one is challenging*!