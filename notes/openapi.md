# Pulling data from (open) REST APIs

[Huge source of public APIs](https://www.publicapis.com/)

We have already seen how to use `requests` to fetch a webpage:

```python
r = requests.get('http://www.cnn.com')
print r.text
```

If the URL is to a page that gives you HTML, we would say that we are fetching a webpage. On the other hand, if the URL is returning data in some form, we would say that we are accessing a *REST* api.
 
**REST** is an acronym for *REpresentational State Transfer* and is a very handy way to make something trivial sound very complicated.  Anytime you see the word REST, just think "webpage that gives me data not HTML." There is a massive industry and giant following behind this term but I don't see anything beyond "fetch data from webpage".

Anyway, we are going to pull data from web servers that intentionally provide nice data spigot URLs. Information you need in order to get data is typically:

* Base URL, including machine name, port number, and "file" path
* The names and values of parameters
* What data comes back and in what format (XML, JSON, CSV, ...)

## JSON from openpayments.us

Now, let's look at a website that will give us JSON data: [www.openpayments.us](http://www.openpayments.us).
 
There is a REST data API available at URL template:

```
URL = "http://openpayments.us/data?query=%s"
```
**Exercise**: Use `curl` to fetch data about a doctor.

**Exercise**: Fetch the data for a doctor's name, such as `John Chan`. If you want to get fancy, you can pull in the query from a script parameter via:

```python
query = sys.argv[1]
```

Sample code:

```
import requests
import json
import sys

URL = "http://openpayments.us/data?query=%s"
name = sys.argv[1]

r = requests.get(URL % name)
data = json.loads(r.text)

print json.dumps(data)
```

A **technical detail** related to valid strings you can include as part of a URL.  Spaces are not allowed so `John Chan` has to be encoded or "quoted".  Fortunately, `requests` does this automatically for us. If you ever need to quote URLs, use `urllib`:

```python
from requests.utils import quote
query = quote(query)
```

Because `&` is the separator between parameters, it is also invalid in a parameter name or value. Here are some example conversions:

```python
>>> import urllib
>>> quote("john chan")
'john%20chan'
>>> quote("john&chan")
'john%26chan'
```

The conversion uses the ASCII character code (in 2-digit hexadecimal) for space and ampersand. Sometimes you will see the space converted to a `+`, which also works: `John+Chan`.

This website gives you JSON, which is very easy to load in using the default `json` package:

```python
data = json.loads(jsondata)
```

Dump the JSON using `json.dumps()`.

## Historical stock data

*Yahoo's API was taken down in 2017 so we will use Quandl instead.* 

Register for an API key at [Quandl](https://www.quandl.com/account/api) and then you can use this URL to access, for example, Apple's stock data:

```
https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv?ticker=AAPL&api_key=YOURAPIKEY
```

You have to replace the `AAPL` with whatever stock ticker you want and of course replace `YOURAPIKEY` with your specific API key that you got when you registered.
 
Code: [Quandl finance stock history](notes/code/quandl/history.py):

```python
import sys
import requests

HistoryURL = "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv?ticker=%s&api_key=%s"

ticker = sys.argv[1]  # AAPL
APIKEY = sys.argv[2]  # your key

url = HistoryURL % (ticker,APIKEY)
r = requests.get(url)
csvdata = r.text
print csvdata
```

The CSV you get back looks like:

```
ticker,date,open,high,low,close,volume,ex-dividend,split_ratio,adj_open,adj_high,adj_low,adj_close,adj_volume
AAPL,1980-12-12,28.75,28.87,28.75,28.75,2093900.0,0.0,1.0,0.42270591588018,0.42447025361603,0.42270591588018,0.42270591588018,117258400.0
AAPL,1980-12-15,27.38,27.38,27.25,27.25,785200.0,0.0,1.0,0.40256306006259,0.40256306006259,0.40065169418209,0.40065169418209,43971200.0
...
```

```
# csv is easy to handle ourselves:
for row in csvdata.strip().split("\n"):
    cols = row.split(',')
    print ', '.join(cols)
```

**Exercise:** By looking at the [quandl usage doc](https://docs.quandl.com/docs/in-depth-usage-1) and [quandl parameter doc](https://docs.quandl.com/docs/parameters-1) fetch and fetch stock history for TSLA for just 2015 and only get columns `data` and `open`.

```python
QuoteURL = "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv?ticker=%s&api_key=YOURAPIKEY&date.gte=%s&date.lt=%s&qopts.columns=%s"
```

Here's my solution from the command line:

```bash
$ curl "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv?ticker=AAPL&api_key=SECRET&date.gte=20150101&date.lt=20160101&qopts.columns=date,open"
```

The data you get back is in CSV format. For stock ticker `TSLA`, you would see two requested fields (close to these values):

```
date,open
2015-01-02,111.39
2015-01-05,108.29
2015-01-06,106.54
2015-01-07,107.2
2015-01-08,109.23
```

**Exercise**: Change `csv` into `json` in the URL and see that you get JSON back now.

## Pulling movie data from IMDB

Let's try to pull down some more interesting data using the [OMDb API](http://www.omdbapi.com/):

> The OMDb API is a free web service to obtain movie information, all content and images on the site are contributed and maintained by our users.

Let's also learn a more convenient way to specify URL parameters (with a dictionary).

```python
URL = "http://www.omdbapi.com/?"

args = {
	's' : 'cats',
	'r' : 'json'
}

r = requests.get(URL, params=args)
```

**Exercise**: Use this code as a starting point and extract data from the movie database. You can change the search string to anything you want. Print out `r.url` so you can see how it encodes the dictionary as GET arguments on the URL.

**Exercise**:  Write a small Python script using base URL `http://www.omdbapi.com` and parameters `t` (movie title) and `y` (movie year) to look up some of your favorite movies. The default output should come back in JSON.  Here is the structure of the argument dictionary:

```python
args = {
	't' : movie_title,
	'y' : movie_year,
}
```

Now, change your program so that it requests data back in XML format:

```python
args = {
	't' : movie_title,
	'y' : movie_year,
	'r' : 'xml'
}
```

Replace the json conversion code with code that [untangle](https://untangle.readthedocs.io/en/latest/)'s the XML to print out the title and the plot. All of the REST parameters are explained in the [API document](http://www.omdbapi.com/).  Recall that untangle lets you refer to children of `x` with `x.childname`. Parse with `x = untangle.parse(testxml)`. Attributes of a specific node are stored in a dictionary so `x`'s attributes are `x['attributename']`. You will have to look at the structure of the XML to figure out how to dig down into the tree.

## CURLing for it

Now that we've done it the hard way in Python, let's repeat the exercises from above using one-liners on the shell. The `curl` program is your friend and can do all sorts of amazing things. Here are the 4 GETs using curl:

```bash
curl "http://ichart.finance.yahoo.com/table.csv?s=TSLA"
curl "http://openpayments.us/data?query=John+Chan"
curl "http://www.omdbapi.com/?s=cats&r=json"
curl "http://www.omdbapi.com/?t=Star+Wars"
```

`curl` writes the output to standard out so you can redirect into a file.

Notice that we have to url encode the arguments, so ` ` becomes `+`.

Next, let's look at how we might process JSON using the command line. First, install [jq](https://stedolan.github.io/jq/), which is a very handy JSON formatting and querying tool:

```bash
$ brew install jq  # for macs
```

```bash
$ curl -s "http://www.omdbapi.com/?s=cats" | jq
{
  "Search": [
    {
      "Title": "Cats & Dogs",
      "Year": "2001",
      "imdbID": "tt0239395",
      "Type": "movie",
      "Poster": "http://ia.media-imdb.com/images/M/MV5BMjExMjIwNzE4OV5BMl5BanBnXkFtZTYwNTY0MDI5._V1_SX300.jpg"
    },
...
```

Given that output, let's use `jq` to extract the list of IDs:

```bash
$ curl -s "http://www.omdbapi.com/?s=cats" | jq '.Search[].imdbID'
"tt0239395"
"tt0117979"
"tt1287468"
"tt1426378"
"tt0118829"
"tt1223236"
"tt0465315"
"tt0217990"
"tt2345459"
"tt0285371"
```

We can get rid of those pesky quotes with `tr`:
 
```bash
curl -s "http://www.omdbapi.com/?s=cats" | jq '.Search[].imdbID' | tr -d '"'
tt0239395
tt0117979
tt1287468
tt1426378
tt0118829
tt1223236
tt0465315
tt0217990
tt2345459
tt0285371
```

Why would I want to do that? so I can use a for loop in the shell to go fetch all of those. First, let's get those into a variable:

```bash
$ ids=$(curl -s "http://www.omdbapi.com/?s=cats" | jq '.Search[].imdbID' | tr -d '"')
```

Then we can loop over these IDs to individually get their records and write them to files:

```bash
$ for id in $ids
do
	curl -s "http://www.omdbapi.com/?i=$id" > /tmp/$id.json
done
```

That writes out a bunch of files, which we can look at again with `jq` four nice formatting:

```bash
$ jq < /tmp/tt0117979.json 
{
  "Title": "The Truth About Cats & Dogs",
  "Year": "1996",
  "Rated": "PG-13",
  "Released": "26 Apr 1996",
  "Runtime": "97 min",
  "Genre": "Comedy, Romance",
  "Director": "Michael Lehmann",
  "Writer": "Audrey Wells",
  "Actors": "Uma Thurman, Janeane Garofalo, Ben Chaplin, Jamie Foxx",
  "Plot": "A successful veternarian & radio show host with low self-esteem asks her model friend to impersonate her when a handsome man wants to see her.",
  "Language": "English",
  "Country": "USA",
  "Awards": "1 nomination.",
  "Poster": "http://ia.media-imdb.com/images/M/MV5BMTYxNjIyMjkxNl5BMl5BanBnXkFtZTYwMDAzOTg4._V1_SX300.jpg",
  "Metascore": "64",
  "imdbRating": "6.3",
  "imdbVotes": "22,358",
  "imdbID": "tt0117979",
  "Type": "movie",
  "Response": "True"
}
```
