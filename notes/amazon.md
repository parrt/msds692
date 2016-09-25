# Capturing the bestseller list from Amazon

Let's capture the [bestseller list from Amazon](https://www.amazon.com/gp/bestsellers/books/ref=sv_b_2). The HTML coming out is extremely complicated and contains lots of JavaScript, but the HTML is very organized using `div` tags. Using Firefox, I can also inspect elements. Notice that `div` tag with `class=zg_itemWrapper` nicely groups each element in the bestseller list:

<img src="figures/amz-book-item.png" width=300>

To collect information about each book, we just have to look at the child nodes of that `div`.

**Exercise**:  Create a function that returns a list of tuples, one per book. The couple should contain `(price, title, author, href)`.

```python
def parseAmazonBestSellers():
    req = urllib2.Request("https://www.amazon.com/gp/bestsellers/books/ref=sv_b_2",
                          headers={'User-Agent': "Resistance is futile"})
    response = urllib2.urlopen(req)
    html = BeautifulSoup(response, "html.parser")
    ...
```

Notice that I have included the user agent, otherwise I noticed that Amazon gave me a permission error. (It's funny that it is so easy to defeat.)