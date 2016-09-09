# https://docs.python.org/2/howto/urllib2.html
import urllib
import urllib2
import sys
import json

URL = "http://openpayments.us/data?query=%s"

query = sys.argv[1]

query = urllib.quote(query)             # https://docs.python.org/2/library/urllib.html#urllib.quote
response = urllib2.urlopen(URL % query) # https://docs.python.org/2/library/urllib.html#urllib.urlencode
jsondata = response.read()              # read all data

#print jsondata                          # raw json

data = json.loads(jsondata)             # dictionary version

print json.dumps(data, indent=4)
