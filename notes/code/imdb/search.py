# API home http://www.omdbapi.com/

# no key required

import urllib
import urllib2
import json

URL = "http://www.omdbapi.com/?"

query = {
	's' : 'cats',
}

query_url = URL + urllib.urlencode(query)
response = urllib2.urlopen(query_url)
jsondata = response.read()

json_data = json.loads(jsondata)

print json.dumps(json_data, indent=4)
