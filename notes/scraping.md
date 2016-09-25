# Collecting data from web pages

We already know how to fetch a webpage using `urlopen()`. The question is: How do we extract useful information from the HTML. We are going to use BeautifulSoup again to parse the HTML and then search for elements of interest.

## Training wheels

**Exercise**: Go grab the latest news from Hacker News, part of the Y Combinator startup incubator: `https://news.ycombinator.com/newest`. Parse the data with BeautifulSoup and then find all of the links to news.  You can either look at the page source in your browser to see what HTML renders those links or you can use chrome browser. Right-click over one of the links and say "inspect". It will show you the HTML associated with that link:

<img src=figures/hn-element.png width=500>

Noticed that the link has a CSS class: `class="storylink"`. Wow. Now that is convenient. Figure out how to get BeautifulSoup to search for all tags that have that CSS class then print the link and link text:

```python
for link in html.find_all(...):
    print link['href'], link.text
```
