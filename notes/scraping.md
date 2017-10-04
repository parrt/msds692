# Collecting data from web pages

We already know how to fetch a webpage using `requests.get(...)`. The question is: How do we extract useful information from the HTML. We are going to use BeautifulSoup again to parse the HTML and then search for elements of interest.

[Lots of useful web scraping info here](https://automatetheboringstuff.com/chapter11/)

## Baby steps

**Exercise**: Write Python code (`requests` lib) to grab the latest news from Hacker News in your browser, part of the Y Combinator startup incubator: `https://news.ycombinator.com/`. Parse the data with BeautifulSoup and then find all of the links to news.  You can either look at the page source in your browser to see what HTML renders those links or you can use chrome browser. Right-click over one of the links and say "inspect". It will show you the HTML associated with that link:

<img src=figures/hn-element.png width=500>

Notice that the link has a CSS class: `class="storylink"`. Fantastic, now that is convenient.  So you just have to figure out how to get BeautifulSoup to search for all tags that have that CSS class then print the link and link text:

```python
for link in html.find_all(...):
    print link['href'], link.text
```

*Hint:* Search for "beautifulsoup find all class."

If you want to get fancy, you can make a list of tuples, where each tumble is a (*link*,*link text*), and then print the list.


## Mimicking a "human using a browser"

Many websites would prefer that you did not scrape their data using a program, so we often have to mimic a human. There are two key elements:

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

Of course, you have to alter your code that does the `requests.get()` to call this function now instead. This is a way to guarantee that we don't pound somebody's server and get cut off. It's also a good example of a failsafe (give example from jguru with email on/off switch at the outgoing SMTP client).

Verify that you can still get the hacker news page.

Next, we need to pretend to be a browser, which means setting a header that goes out with the HTTP protocol to the remote server. For example, if you view [this URL](https://api.github.com/meta) in your browser, it's no problem but a regular `requests.get()` without a `User-Agent` will get a 403 permissions error from the server. Here is an example from the command line:

```bash
$ curl --user-agent "" https://api.github.com/meta
Request forbidden by administrative rules. Please make sure your request has a User-Agent header (http://developer.github.com/v3/#user-agent-required). Check https://developer.github.com for other possible causes.
```

**Exercise**: Alter `fetch` so that it passes a `User-Agent` header so that the protocol going to the Web server will include:

```
User-Agent: Resistance is futile
```

or some other header value. You will pass in a dictionary with that keyvalue pair as the `params` argument of `requests.get()`.

Verify that you can still get the hacker news page.

**Exercise**:  Create a function that extracts all of the news links and puts them into a list, rather than printing them out.

```python
def parseHN():
    page,html = fetch("https://news.ycombinator.com/")
    links = ...
    return links
```

## Reddit

Ok, so Hacker News might shut us down. As a back up, you can scan [reddit news](https://www.reddit.com/r/all). By inspecting a link on that page with the browser (using developer tools), it looks like links have `class="title may-blank outbound"` or just `class="title may-blank"`:

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
$ curl https://www.reddit.com/r/all/
...
<p>we're sorry, but you appear to be a bot and we've seen too many requests
from you lately. we enforce a hard speed limit on requests that appear to come
from bots to prevent abuse.</p>

<p>if you are not a bot but are spoofing one via your browser's user agent
string: please change your user agent string to avoid seeing this message
again.</p>
```

On the other hand, if you set the agent, you get real data back:
 
```bash
$ curl --user-agent "Resistance is futile" https://www.reddit.com/r/all/
...
```

(Note the / on the end of the URL. Without that you get a redirect message.)

The HTTP protocol from the client side looks then like:

```
> GET /r/all/ HTTP/1.1
> Host: www.reddit.com
> User-Agent: Resistance is futile
> Accept: */*

```