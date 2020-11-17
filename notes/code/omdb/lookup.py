# API home http://www.omdbapi.com/
# python lib https://github.com/dgilland/omdb.py

# Derived from https://blog.n-der.net/?p=14
import requests
import json
import untangle
import sys

key = sys.argv[1]

URL = "http://www.omdbapi.com/?"
 
movie_title = "Star Wars"
movie_year = "1977"
 
args = {
	't' : movie_title,
	'y' : movie_year,
	'r' : 'xml',
        'apikey' : key
}

r = requests.get(URL, params=args)
data = r.text

if 'r' in args and args['r']=='xml':
    print(data)
    xml = untangle.parse(data)
    print(xml.root.movie['title'])
    print(xml.root.movie['plot'])
else:
    json_data = json.loads(data)
    print(json.dumps(json_data, indent=4))
