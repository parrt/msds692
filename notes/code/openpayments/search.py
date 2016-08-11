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

# def spaces(n): return " " * n
#
# def nestedjson(data):
#     indent = 0
#     if isinstance(data, list):
#         print spaces(indent)+"["
#         indent += 4
#         for it in items[1]:
#             nestedjson
#         print spaces(indent)+"]"
#         nestedjson(items[1])
#     if isinstance(data, dict):
#         for items in data.items():
#         else:
#             print str(items[0]) + ":" + str(items[1])
#
# nestedjson(data)
