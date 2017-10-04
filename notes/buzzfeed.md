# Pulling news from buzzfeed

[Buzzfeed](https://www.buzzfeed.com/news) is an interesting news site that also still provides webpages as HTML we can parse easily. The difference between this and hacker news is that we are going to group links by category from the website.

Using Chrome's "inspect" again, we see that news link `a` tags have a number of interesting attributes:

<img src=figures/buzzfeed.png width=550>

Note the `post_category` thing inside of the weird `data-bfa` attribute of the `a` tag. We need to grab both the `href` and the topic/category from this `a` tag. Unfortunately it's a lot trickier than looking for a simple `class` attribute as we did with HackerNews.

To get all `a` tags that has an attribute with `post_category`, we have to do something fancy. Were going to pass in a function to `findAll`:

```python
for link in html.findAll(lambda tag: tag.name=='a' and 'data-bfa' in tag.attrs):
    attr = link['data-bfa']
    if not 'post_category' in attr: continue
    ...
```

That lambda is just a function that would normally look like:

```python
def f(tag):
    return tag.name=='a' and 'data-bfa' in tag.attrs
```

Then we would use this loop instead:

```python
for link in html.findAll(f):
    ...
```

**Exercise**: Write a `parseBF` function that fetches `https://www.buzzfeed.com/news`, purses with beautiful soup, and then uses the `for` loop above to find all of the appropriate tags. While debugging, you can print out `link['href']` to show the link, or of course you can print the whole `link`. Next, extract to the `post_category` from the `data-bfa` attribute.  Fill and return a dictionary that maps category/topic two a list of `href` likes.  Using the following main script to print out the dictionary

```python
topics = parseBF()
for t in topics:
    print t
    print '\t'+'\n\t'.join(topics[t])
```

you will get output that looks like:

```
Business
	/venessawong/americas-biggest-egg-company-is-rethinking-its-cage-free
	/venessawong/americas-biggest-egg-company-is-rethinking-its-cage-free
USNews
	/amberjamieson/everything-we-know-about-marilou-danley
	/buzzfeednews/live-updates-two-people-are-dead-as-police-investigate
	/rosebuchanan/las-vegas-shooter
	/coralewis/these-are-the-victims-of-the-las-vegas-shooting
	/jimdalrympleii/eerie-silence-inside-the-las-vegas-hotel-turned-into-a
...
```
