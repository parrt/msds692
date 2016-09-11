# API home http://www.omdbapi.com/
# python lib https://github.com/dgilland/omdb.py

# no key required

# Derived from https://blog.n-der.net/?p=14
import urllib
import urllib2
import json
import untangle
 
URL = "http://www.omdbapi.com/?"
 
movie_title = "Star Wars"
movie_year = "1977"
 
query = {
	't' : movie_title,
	'y' : movie_year,
	'r' : 'xml'
}
 
query_url = URL + urllib.urlencode(query)
response = urllib2.urlopen(query_url)
data = response.read()

if 'r' in query and query['r']=='xml':
    print data
    xml = untangle.parse(data)
    print xml.root.movie['title']
    print xml.root.movie['plot']
else:
    json_data = json.loads(data)
    print json.dumps(json_data, indent=4)
