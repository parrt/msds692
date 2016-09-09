# Pulling data from (open) REST APIs

We have already seen how to use `urlib2` to fetch a webpage:

```python
webpage = urllib2.urlopen(URL).read()
```

If the URL is to a page that gives you HTML, we would say that we are fetching a webpage. On the other hand, if the URL is returning data in some form, we say that we are accessing a *REST* api.
 
*REST* is an acronym for REpresentational State Transfer and is a very handy way to make something trivial sound very complicated.  Anytime you see the word REST, just think "webpage that gives me data not HTML." There is a massive industry and giant following behind this term but I cannot see anything beyond "fetch data from webpage".

Anyway, we are going to pull data from Web servers that intentionally provide nice data spigot URLs. Information you need in order to get data is typically:

* Base URL
* The names and contents of parameters
* What data comes back and in what format (XML, CSV, ...)

## Yahoo

Let's start with something we have already seen: CSV data coming back from Yahoo finance.

* Base URL: `http://ichart.finance.yahoo.com/table.csv`
* The names and contents of parameters: `s` is the ticker name
* What data comes back and in what format: CSV

So, the full URL to fetch TSLA's stock history is:

```
http://ichart.finance.yahoo.com/table.csv?s=TSLA
```

Code: [yahoo finance stock history](notes/code/yahoo/history.py):

```python
import sys
import urllib2

HistoryURL = "http://ichart.finance.yahoo.com/table.csv?s=%s"

ticker = sys.argv[1]  # E.g., AAPL
response = urllib2.urlopen(HistoryURL % ticker)
csvdata = response.read()
print csvdata

# csv Python lib prefers reading from files, and it's easy to handle ourselves.
for row in csvdata.strip().split("\n"):
    cols = row.split(',')
    print cols
```

**Exercise:** Fetch and print a stock quote (not the history) from Yahoo finance for a specific quote. Here is the template for getting a stock quote:

```python
QuoteURL = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s"
```

The data you get back is in CSV format. For stock ticker `TSLA`, you would see data:

```
103.520,103.510
```

## JSON from openpayments.us

Now, let's look at a website that will give us JSON data: [www.openpayments.us](http://www.openpayments.us).
 
There is a data API available at URL template:

```
URL = "http://openpayments.us/data?query=%s"
```

**Exercise**: Fetch the data for a doctor's name, such as `John Chan`. If you want to get fancy, you can pull in the query from a script parameter via:

```python
query = sys.argv[1]
```

A **technical detail** related to valid strings you can include as part of a URL.  Spaces are not allowed so `John Chan` has to be encoded or "quoted" we say:

```python
query = urllib.quote(query)
```

Because `&` is the separator between parameters, it is also invalid in a parameter name or value. Here are some example conversions:

```python
>>> import urllib
>>> query = urllib.quote("name=john chan")
>>> urllib.quote("john chan")
'john%20chan'
>>> urllib.quote("john&chan")
'john%26chan'
```

The conversion uses the ASCII character code (in 2-digit hexadecimal) for space and ampersand.

This website gives you JSON, which is very easy to load and using the default `json` package:

```python
data = json.loads(jsondata)
```

Dump the JSON using `json.dumps()`.

## Pulling movie data from IMDB

[imdb lookup](notes/code/imdb/lookup.py)

[imdb search](notes/code/imdb/search.py)
