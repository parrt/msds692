# Pulling data from (open) REST APIs

[Big source of public APIs](https://rapidapi.com/collection/list-of-free-apis)

We have already seen how to use `requests` to fetch a webpage:

```python
r = requests.get('http://www.cnn.com')
print(r.text)
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
URL = f"http://openpayments.us/data?query={q}" # for some q
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

name = sys.argv[1]
URL = f"http://openpayments.us/data?query={name}"

r = requests.get(URL)
data = json.loads(r.text)

print(json.dumps(data))
```

A **technical detail** related to valid strings you can include as part of a URL.  Spaces are not allowed so `John Chan` has to be encoded or "quoted".  Fortunately, `requests` does this automatically for us. If you ever need to quote parameter values in URLs, you can do this:

```python
from urllib.parse import quote
value = quote(value)
```

Because `&` is the separator between parameters, it is also invalid in a parameter name or value. Here are some example conversions:

```python
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
