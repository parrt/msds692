# API home http://www.omdbapi.com/
# python lib https://github.com/dgilland/omdb.py

# no key required

# Derived from https://blog.n-der.net/?p=14
import urllib
import urllib2
import json
 
URL = "http://www.omdbapi.com/?"
 
movie_title = "Star Wars"
movie_year = "1977"
 
query = {
	'i' : '', 
	't' : movie_title,
	'y' : movie_year
}
 
query_url = URL + urllib.urlencode(query)
response = urllib2.urlopen(query_url)
jsondata = response.read()

json_data = json.loads(jsondata)
 
print json.dumps(json_data, indent=4)
