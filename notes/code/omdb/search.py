# API home http://www.omdbapi.com/

# no key required

import requests
import json
import sys

key = sys.argv[1]

URL = "http://www.omdbapi.com/?"

args = {
	's' : 'cats',
	'r' : 'json',
        'apikey' : key
}

r = requests.get(URL, params=args)
jsondata = r.text

json_data = json.loads(jsondata)

print(json.dumps(json_data, indent=4))
