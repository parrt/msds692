# REGISTER: https://www.zillow.com/user/Register.htm
# API REGISTER: https://www.zillow.com/webservice/Registration.htm
# API DOC: http://www.zillow.com/howto/api/APIOverview.htm

# Run with args: yourzipid "190 7th St APT 4" "San Francisco, CA"
import sys
import untangle
import urllib2
import urllib

KEY = sys.argv[1]                       # your zillow api key/id as argument to script

# Find a house
SearchURL = "http://www.zillow.com/webservice/GetChart.htm?zws-id=%s&zpid=%s&unit-type=percent&width=500&height=250&chartDuration=10years"

URL = SearchURL % (KEY, '64969892')
response = urllib2.urlopen(URL)
xmldata = response.read()
print xmldata

xml = untangle.parse(xmldata)
code = xml.SearchResults_searchresults.message.code.cdata
if code=='0':
    zpid = xml.SearchResults_searchresults.response.results.result.zpid.cdata
    print zpid
else:
    msg = xml.SearchResults_searchresults.message.text.cdata
    print msg
