# https://docs.python.org/2/howto/urllib2.html
import requests
import sys
import json

URL = "http://openpayments.us/data?query=%s"

query = sys.argv[1]

r = requests.get(URL % query)
jsondata = r.text

#print jsondata                          # raw json

data = json.loads(jsondata)             # dictionary version

print(json.dumps(data, indent=4))
