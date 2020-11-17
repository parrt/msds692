# Pulling data from REST APIs requiring keys

Sites that use to be freely available without any kind of a dedication have become rare.  Companies have started to require keys because they can throttle usage and it prevents, or at least gives a way to shut down, denial of service attacks.

So, after completely open APIs, the next easiest kind of data to get is one that has an API but requires you to register and get a key, which is what we will do in this lab/lecture.

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
print(csvdata)
```

You can run this via:

```
$ python history.py TSLA $(cat ~/Dropbox/licenses/quandl.txt)
ticker,date,open,high,low,close,volume,ex-dividend,split_ratio,adj_open,adj_high,adj_low,adj_close,adj_volume
AAPL,1980-12-12,28.75,28.87,28.75,28.75,2093900.0,0.0,1.0,0.42270591588018,0.42447025361603,0.42270591588018,0.42270591588018,117258400.0
AAPL,1980-12-15,27.38,27.38,27.25,27.25,785200.0,0.0,1.0,0.40256306006259,0.40256306006259,0.40065169418209,0.40065169418209,43971200.0
...
```

where `$(cat ~/Dropbox/licenses/quandl.txt)` just gets my secret api key.

CSV data is easy to handle ourselves:

```
for row in csvdata.strip().split("\n"):
    cols = row.split(',')
    print(', '.join(cols))
```

**Exercise:** By looking at the [quandl usage doc](https://docs.quandl.com/docs/in-depth-usage-1) and [quandl parameter doc](https://docs.quandl.com/docs/parameters-1) fetch and fetch stock history for TSLA for just 2015 and only get columns `data` and `open`.

```python
QuoteURL = "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv?ticker=%s&api_key=YOURAPIKEY&date.gte=%s&date.lt=%s&qopts.columns=%s"
```

Here's my solution from the command line:

```bash
$ curl "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv?ticker=AAPL&api_key=SECRET&date.gte=20150101&date.lt=20160101&qopts.columns=date,open"
```

But, you can also use a Python script.

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

As of 2018, you have to [get an API key](http://www.omdbapi.com/apikey.aspx). They will send you a key by email that you must activate. [Never store your API key in your code](https://www.zdnet.com/article/over-100000-github-repos-have-leaked-api-or-cryptographic-keys/).

Let's also learn a more convenient way to specify URL parameters (with a dictionary).

```python
URL = "http://www.omdbapi.com/?"

args = {
   's' : 'cats',
   'r' : 'json',
   'apikey' : YOUR_OMDB_API_KEY
}

r = requests.get(URL, params=args)
```

**Exercise**: Use this code as a starting point and extract data from the movie database. You can change the search string to anything you want.  My output looks like:

```bash
$ python omdb.py YOUR_OMDB_API_KEY | jq
{
  "Search": [
    {
      "Title": "Cats & Dogs",
      "Year": "2001",
      "imdbID": "tt0239395",
      "Type": "movie",
      "Poster": "https://m.media-amazon.com/images/M/MV5BY2JmMDJlMmEtYTk4OS00YWQ5LTk2NzMtM2M3NzhkMjI4MGJkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_SX300.jpg"
    },
    {
      "Title": "The Truth About Cats & Dogs",
      "Year": "1996",
      "imdbID": "tt0117979",
      "Type": "movie",
      "Poster": "https://ia.media-imdb.com/images/M/MV5BOWM0MTA4NjItMzM3ZS00NDJmLTg3NWItNGE5ODIyOGJhNzQ0L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg"
    },
    ...
```

Look at `r.url` so you can see how it encodes the dictionary as GET arguments on the URL. [Solutions](https://github.com/parrt/msds692/tree/master/notes/code/omdb)

**Exercise**:  Write a small Python script using base URL `http://www.omdbapi.com` and parameters `t` (movie title) and `y` (movie year) to look up some of your favorite movies. The default output should come back in JSON.  Here is the structure of the argument dictionary:

```python
args = {
    't' : movie_title,
    'y' : movie_year,
    'apikey' : YOUR_OMDB_API_KEY
}
```

Now, change your program so that it requests data back in XML format:

```python
args = {
    't' : movie_title,
    'y' : movie_year,
    'r' : 'xml',
    'apikey' : YOUR_OMDB_API_KEY
}
```

Replace the json conversion code with code that [untangle](https://untangle.readthedocs.io/en/latest/)'s the XML to print out the title and the plot. All of the REST parameters are explained in the [API document](http://www.omdbapi.com/).  Recall that untangle lets you refer to children of `x` with `x.childname`. Parse with `x = untangle.parse(testxml)`. Attributes of a specific node are stored in a dictionary so `x`'s attributes are `x['attributename']`. You will have to look at the structure of the XML to figure out how to dig down into the tree.

[Solutions](https://github.com/parrt/msds692/tree/master/notes/code/omdb)

## CURLing for it

Now that we've done it the hard way in Python, let's repeat the exercises from above using one-liners on the shell. The `curl` program is your friend and can do all sorts of amazing things. Here are the 4 GETs using curl:

```bash
curl "http://www.omdbapi.com/?s=cats&r=json&apikey=SECRET"
curl "http://www.omdbapi.com/?t=Star+Wars&apikey=SECRET"
```

`curl` writes the output to standard out so you can redirect into a file.

Notice that we have to url encode the arguments, so ` ` becomes `+`.

Next, let's look at how we might process JSON using the command line. First, install [jq](https://stedolan.github.io/jq/), which is a very handy JSON formatting and querying tool:

```bash
$ brew install jq  # for macs
```

```bash
$ curl -s "http://www.omdbapi.com/?s=cats&apikey=SECRET" | jq
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
$ curl -s "http://www.omdbapi.com/?s=cats&apikey=SECRET" | jq '.Search[].imdbID'
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
curl -s "http://www.omdbapi.com/?s=cats&apikey=SECRET" | jq '.Search[].imdbID' | tr -d '"'
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
$ ids=$(curl -s "http://www.omdbapi.com/?s=cats&apikey=SECRET" | jq '.Search[].imdbID' | tr -d '"')
```

Then we can loop over these IDs to individually get their records and write them to files:

```bash
$ for id in $ids
do
	curl -s "http://www.omdbapi.com/?i=$id&apikey=SECRET" > /tmp/$id.json
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
