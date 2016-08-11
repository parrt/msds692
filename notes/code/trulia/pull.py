# register via mashery: http://developer.trulia.com/member/register
# get API key http://developer.trulia.com/apps/register

import urllib
import urllib2
import sys
import json
import xml.etree.ElementTree as ET

KEY=sys.argv[1]

LocationInfoURL =\
    "http://api.trulia.com/webservices.php?library=LocationInfo&function=getCitiesInState&state=%s&apikey=%s"

state = "CA"

URL = LocationInfoURL % (state, KEY)
print URL
response = urllib2.urlopen(URL)
jsondata = response.read()              # read all data

data = json.loads(jsondata)             # dictionary version

print json.dumps(data, indent=4)