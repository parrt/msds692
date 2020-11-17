# API home http://www.omdbapi.com/

import requests
import json
import sys

key = sys.argv[1]
term = sys.argv[2]

URL = "http://www.omdbapi.com/?"

args = {
    's' : term,
    'r' : 'json',
    'apikey' : key
}

r = requests.get(URL, params=args)
jsondata = r.text

json_data = json.loads(jsondata)

print(json.dumps(json_data, indent=4))
