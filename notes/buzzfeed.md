# Pulling news from buzzfeed

[Buzzfeed](https://www.buzzfeed.com/news) is an interesting news site that also still provides webpages as HTML we can parse easily. The difference between this and hacker news is that we are going to group links by category from the website.

Using Chrome's "inspect" again, we see that news link `a` tags have a number of interesting attributes:

```html
<a href="/katherinemiller/obama-jokes-i-am-so-relieved-that-the-birther-thing-is-over"
	data-bfa="@a:Title;@d:politics;"
	rel:gt_act="post/title"
	rel:gt_label="politics"
	class="xs-block link-gray">
Obama Jokes: "I Am So Relieved That The Birther Thing Is Over"
</a>
```

You can see that there are two handy attributes: `rel:gt_act` and `rel:gt_label`. Unfortunately, not all links have the second. For example the top stories look like:

```html
<a href="/davidmack/miami-marlins-pitcher-jose-fernandez-dies-in-boating-acciden"
	class="xs-block link-gray"
	rel:gt_act="post/title"
	data-bfa="@a:Title;@d:Top-Stories;">
Miami Marlins Pitcher José Fernández Dies In Boating Accident
</a>
```

To get all `a` tags that have this `rel:gt_act="post/title"` attribute, we can use:

```python
for link in html.find_all('a', {'rel:gt_act':'post/title'}):
    ...
```

If you look at the `link.attrs` dictionary, you will see `rel:gt_label` unless it is a top story. By assuming links missing that attribute are in the `topstories` topic, I get the following topic list:

```python
['topstories', u'business', u'science', u'LGBT', u'bigstories', u'tech', u'politics', u'world']
```

**Exercise**: Write a `parseBF` function that extracts all `post/title` links and returns a dictionary mapping topic to a list of links associated with that topic.  Using the following code

```python
topics = parseBF()
for t in topics:
    print t
    print '\t'+'\n\t'.join(topics[t])
```

you will get output that looks like:

```
topstories
	/talalansari/heres-what-we-know-about-the-suspected-washington-mall-shoot
	/davidmack/miami-marlins-pitcher-jose-fernandez-dies-in-boating-acciden
	/dinograndoni/climate-change-clinton-trump
   ...
science
	/kellyoakes/would-you-like-some-dry-ice-for-that-burn
	/peteraldhous/where-are-the-shy-trumpers
	/danvergano/does-congress-need-a-jail
	/azeenghorayshi/hackers-invade-science-journalism-site
LGBT
	/hazelnewlevant/badass-bisexual-women
	/skarlan/beaches-binders-and-baptism-a-first-summer-after-top-surgery
	/tasneemnashrulla/texas-judge-temporarily-blocks-federal-protections-for-trans
	/shannonkeating/stranger-things-and-compulsory-femininity
bigstories
	/mattstroud/latitude-360
	/zainaa/meet-the-muslim-blogger-whos-proving-modesty-can-be-fashiona
	/albertsamaha/threesheldons
tech
	/charliewarzel/after-reporting-abuse-many-twitter-users-hear-silence-or-wor
	/charliewarzel/i-let-facebooks-algorithms-run-my-life-for-weeks
	/stephaniemlee/game-on
	/johnpaczkowski/inside-iphone-7-why-apple-killed-the-headphone-jack
politics
	/kyleblaine/trump-says-police-know-who-terrorists-are-dont-do-anything-o
	/katherinemiller/obama-jokes-i-am-so-relieved-that-the-birther-thing-is-over
	/rubycramer/clinton-people-have-thrown-hateful-nonsense-at-the-obamas
	/chrisgeidner/the-supreme-court-almost-became-an-issue
world
	/mikegiglio/the-syrian-regime-had-full-details-about-the-aid-convoy-that
	/miriamelder/estonias-president-wants-some-of-his-fellow-leaders-to-end-n
	/hayesbrown/latvian-president-buzzfeed-interview
	/alimwatkins/washington-really-doesnt-want-to-deal-with-a-cyber-war-with
```