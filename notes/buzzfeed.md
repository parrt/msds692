# Pulling news from buzzfeed

[Buzzfeed](https://www.buzzfeed.com/) is an interesting news site that also still provides webpages as HTML we can parse easily. The difference between this and hacker news is that we are going to group links by category from the website.

Using Chrome's "inspect" again, we see that news link `a` tags have a number of interesting attributes:

<img src=figures/buzzfeed.png width=550>

Note the `post_category` thing inside of the weird `data-bfa` attribute of the `a` tag. We need to grab both the `href` and the topic/category from this `a` tag. Unfortunately it's a lot trickier than looking for a simple `class` attribute as we did with HackerNews.

To get all `a` tags that has an attribute with `post_category`, we have to do something fancy. We're going to pass in a function to `findAll`:

```python
for link in soup.findAll(lambda tag: tag.name=='a' and 'data-bfa' in tag.attrs):
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
for link in soup.findAll(f):
    ...
```

If you don't like that approach, you can use the more explicit:

```
for link in soup.find_all("a"):
    if 'data-bfa' not in link.attrs: continue
    attr = link['data-bfa']
```

**Exercise**: Write a `parseBF` function that fetches `https://www.buzzfeed.com/`, parses with beautiful soup, and then uses the `for` loop above to find all of the appropriate tags. While debugging, you can print out `link['href']` to show the link, or of course you can print the whole `link`. Next, extract to the `post_category` from the `data-bfa` attribute.  Fill and return a dictionary that maps category/topic two a set of `href` links.  Using the following main script to print out the dictionary

```python
topics = parseBF()
for t in topics:
    print(t)
    print('\t'+'\n\t'.join(topics[t]))
```

you will get output that looks like:

```
World
	https://www.buzzfeednews.com/article/karlazabludovsky/venezuela-women-fleeing-colombia-give-birth-refugee
	https://www.buzzfeednews.com/article/emilytamkin/kosovo-land-swap-serbia-warns-against-prime-minister
...
USNews
	https://www.buzzfeednews.com/article/tasneemnashrulla/juanita-broaddrick-who-accused-bill-clinton-of-rape-says
	https://www.buzzfeednews.com/article/gabrielsanchez/this-is-what-americas-first-shopping-mall-looked-like-when
	https://www.buzzfeednews.com/article/davidmack/cristiano-ronaldo-says-a-rape-accusation-against-him-is
	https://www.buzzfeednews.com/article/paulmcleod/kavanaugh-vote-jeff-flake-fbi-investigation-delay
...
```

[Solutions](https://github.com/parrt/msds692/tree/master/notes/code/scrape)
