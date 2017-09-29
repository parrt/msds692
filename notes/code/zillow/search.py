# REGISTER: https://www.zillow.com/user/Register.htm
# API REGISTER: https://www.zillow.com/webservice/Registration.htm
# API DOC: http://www.zillow.com/howto/api/APIOverview.htm

# This seems to not get captcha Sept 2017

# Run with args: yourzipid "190 7th St APT 4" "San Francisco, CA"
import sys
import untangle
import urllib
import requests

KEY = sys.argv[1]                       # your zillow api key/id as argument to script
addr=urllib.quote(sys.argv[2])          # "190 7th St APT 4"
citystatezip=urllib.quote(sys.argv[3])  # "San Francisco, CA"

SearchURL = "http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=%s&address=%s&citystatezip=%s"

URL = SearchURL % (KEY, addr, citystatezip)
print URL
r = requests.get(URL)
xmldata = r.text
# print xmldata

testxml = """<?xml version="1.0" encoding="utf-8"?>
<SearchResults:searchresults xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SearchResults="http://www.zillow.com/static/xsd/SearchResults.xsd" xsi:schemaLocation="http://www.zillow.com/static/xsd/SearchResults.xsd http://www.zillowstatic.com/vstatic/7b56836/static/xsd/SearchResults.xsd">
    <request>
    <address>690 S Van Ness Ave</address>
    <citystatezip>San Francisco, CA</citystatezip>
    </request>
    <message>
    <text>Request successfully processed</text>
    <code>0</code>
    </message>
    <response>
        <results>
            <result>
                <zpid>96040316</zpid>
"""

xml = untangle.parse(xmldata)
code = xml.SearchResults_searchresults.message.code.cdata
if code=='0':
    zpid = xml.SearchResults_searchresults.response.results.result.zpid.cdata
    print zpid
else:
    msg = xml.SearchResults_searchresults.message.text.cdata
    print msg
