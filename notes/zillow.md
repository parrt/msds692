# Zillow

Most sites nowadays require you to register in order to access their data spigot, but some of them don't require authentication. You just need to have your secret ID in order to communicate with them. Zillow is such a site and is straightforward to pull data from, so it is how we will start with the more complicated APIs.

In order to pull data from the real estate website [Zillow](http://www.zillow.com), you must:

1. [Create an account](https://www.zillow.com/user/Register.htm)
2. [Get a ZWSID (Zillow web services ID)](https://www.zillow.com/webservice/Registration.htm)

(*Warning, I'm having trouble with their website redirecting me back to the homepage instead of navigating around or even letting me login. ugh*)

You are limited to 1000 queries per day per API; be careful not to put a request in a loop and then let it run like crazy.

Familiarize yourself with the [API](http://www.zillow.com/howto/api/APIOverview.htm). We are going to use a number of different base URLs to pull some data.

## First contact

To verify that we can communicate with the Zillow server, let's look up a specific property by ID (in file `zestimate.py`) using the [GetZestimate](http://www.zillow.com/howto/api/GetZestimate.htm) API. The URL is of the form

```python
QuoteURL = "http://www.zillow.com/webservice/GetZestimate.htm?zws-id=%s&zpid=%s"
```

You have to pass your ID and the property ID.

**Exercise**: Enter the following code into `zxml.py` to verify that you can access their API. [Solutions](https://github.com/parrt/msds692/tree/master/notes/code/zillow)

```python
import sys
import requests

KEY = sys.argv[1]  # your zillow api key/id as argument to script

# Find out how much property 64969892 is worth
zpid = '64969892'
URL = "http://www.zillow.com/webservice/GetZestimate.htm?zws-id=%s&zpid=%s" % (KEY,zpid)
#print(URL)
r = requests.get(URL)
print(r.text)
```

That will give us XML data back that looks like:

```xml
<?xml version="1.0" encoding="utf-8"?>
<Zestimate:zestimate ...>
  ...
  <message>
    <text>Request successfully processed</text>
    <code>0</code>
  </message>
  <response>
    <zpid>64969892</zpid>
    <links>
      ...
    </links>
    <address>
      <street>140 S Van Ness Ave UNIT 1015</street>
      <zipcode>94103</zipcode>
      <city>San Francisco</city>
      <state>CA</state>
      <latitude>37.771585</latitude>
      <longitude>-122.418825</longitude>
    </address>
    <zestimate>
      <amount currency="USD">725896</amount>
...      
```

BTW, the XML comes back with no new lines, but we can use `xmllint` (`brew install xmlstarlet`) to format the output nicely like that:

```bash
$ python zxml.py | xmllint --format -
...
```

In order to get the estimate, we have to navigate the XML tree using `untangle` and grab the `zestimate` node:

```python
zestimate = xml.Zestimate_zestimate.response.zestimate.amount.cdata
```

**Exercise**: Use untangle to also print out the URL of the property. The link is under the `links` tag. You should get a price and link something like this: [Solutions](https://github.com/parrt/msds692/tree/master/notes/code/zillow)

```
725896
http://www.zillow.com/homedetails/140-S-Van-Ness-Ave-UNIT-1015-San-Francisco-CA-94103/64969892_zpid/
```

## Searching for a property

What do we do if we don't know the property ID? We have to use the [GetSearchResults](http://www.zillow.com/howto/api/GetSearchResults.htm) API.  Picking an address at random, 190 7th St APT 4 SF CA, let's see if we can find it using their API.  The URL we need is:

```python
SearchURL = "http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=%s&address=%s&citystatezip=%s"
```

Where those arguments are passed into your script like this:

```bash
$ python search.py yourzipid "190 7th St APT 4" "San Francisco, CA"
80734051
```

**Exercise**: Using the code from your previous exercise as a base, create a new `search.py` file that searches for a property by address and prints out the `zpid` node (80734051, in this case). [Solutions](https://github.com/parrt/msds692/tree/master/notes/code/zillow)

**Exercise**: Alter your script so that it handles the situation where you have entered an invalid address. The XML you get back looks like: [Solutions](https://github.com/parrt/msds692/tree/master/notes/code/zillow)

```xml
<?xml version="1.0" encoding="utf-8"?>
<SearchResults:searchresults ...>
  <request>
    <address>190 7th St APT 47732498232</address>
    <citystatezip>San Francisco, CA</citystatezip>
  </request>
  <message>
    <text>Error: no exact match found for input address</text>
    <code>508</code>
  </message>
...
```

If there is no error you get `<code>0</code>` in the message, whereas here you can see we get nonzero 508.  First look for the error code. If it is zero then proceed as before. It is nonzero, simply print the text of the error message. If you try to access results, you will get a Python error when you try to untangle the XML.

## Historical price chart

**Exercise**: Using the [GetChart](http://www.zillow.com/howto/api/GetChart.htm) API, print out a link to a chart containing data for a specific property, such as property ID 64969892. The XML you get back looks like: [Solutions](https://github.com/parrt/msds692/tree/master/notes/code/zillow)

```xml
<?xml version="1.0" encoding="utf-8"?>
<Chart:chart ...>
  <request>
  ...
  </request>
  <message>
    <text>Request successfully processed</text>
    <code>0</code>
  </message>
  <response>
    <url>http://www.zillow.com/app?chartDuration=10years&amp;chartType=partner&amp;height=250&amp;page=webservice%2FGetChart&amp;service=chart&amp;showPercent=true&amp;width=500&amp;zpid=64969892</url>
    <graphsanddata>http://www.zillow.com/homedetails/140-S-Van-Ness-Ave-UNIT-1015-San-Francisco-CA-94103/64969892_zpid/#charts-and-data</graphsanddata>
  </response>
  ...
```

Get the URL with the historical chart from the `url` field of the `response` object.  Then use

```
webbrowser.open_new(xml.Chart_chart.response.url.cdata)
```

to open a web browser showing the image, such as:

<img src="figures/zillow-history.png" width="60%">
