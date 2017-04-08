# API home http://www.omdbapi.com/

# no key required

import requests
import json

URL = "http://www.omdbapi.com/?"

args = {
	's' : 'cats',
	'r' : 'json'
}

r = requests.get(URL, params=args)
jsondata = r.text

json_data = json.loads(jsondata)

print json.dumps(json_data, indent=4)
