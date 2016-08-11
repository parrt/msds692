# register via mashery: http://developer.trulia.com/member/register
# get API key http://developer.trulia.com/apps/register

import urllib
import urllib2
import sys
import json

# https://untangle.readthedocs.io/en/latest/
# https://github.com/stchris/untangle
import untangle

KEY=sys.argv[1]

LocationInfoURL =\
    "http://api.trulia.com/webservices.php?library=LocationInfo&function=getCitiesInState&state=%s&apikey=%s"

state = "CA"

URL = LocationInfoURL % (state, KEY)
print URL
response = urllib2.urlopen(URL)
xmldata = response.read()              # read all data
# print xmldata

testxml = """<?xml version="1.0"?>
<TruliaWebServices>
    <response>
        <LocationInfo>
            <city>
                <cityId>86930</cityId>
                <name>Yountville</name>
                <longitude>-122.367593491246</longitude>
                <latitude>38.3938834972556</latitude>
            </city>
        </LocationInfo>
    </response>
</TruliaWebServices>
"""

xml = untangle.parse(xmldata)
for city in xml.TruliaWebServices.response.LocationInfo.city:
    print city.cityId.cdata, city.name.cdata, city.longitude.cdata, city.latitude.cdata
