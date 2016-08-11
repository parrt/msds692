# REGISTER: https://www.zillow.com/user/Register.htm
# API REGISTER: https://www.zillow.com/webservice/Registration.htm
# API DOC: http://www.zillow.com/howto/api/APIOverview.htm

# Run with args: yourzipid "2130 Fulton St" "San Francisco, CA"
import sys
import untangle
import urllib2
import urllib

KEY=sys.argv[1]
addr=urllib.quote(sys.argv[2])
citystatezip=urllib.quote(sys.argv[3])

# Find a house
SearchURL=\
    "http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=%s&address=%s&citystatezip=%s"

URL = SearchURL % (KEY, addr, citystatezip)
response = urllib2.urlopen(URL)
xmldata = response.read()
#print xmldata

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

zpid = xml.SearchResults_searchresults.response.results.result.zpid.cdata

# Find out how much it's worth

QuoteURL =\
    "http://www.zillow.com/webservice/GetZestimate.htm?zws-id=%s&zpid=%s"
URL = QuoteURL % (KEY, zpid)
response = urllib2.urlopen(URL)
xmldata = response.read()              # read all data
#print xmldata

testxml = """<?xml version="1.0" encoding="utf-8"?>
<Zestimate:zestimate xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:Zestimate="http://www.zillow.com/static/xsd/Zestimate.xsd" xsi:schemaLocation="http://www.zillow.com/static/xsd/Zestimate.xsd http://www.zillowstatic.com/vstatic/7b56836/static/xsd/Zestimate.xsd">
<response>
    <zpid>48749425</zpid>
    <links>
        <homedetails>
        http://www.zillow.com/homedetails/2114-Bigelow-Ave-N-Seattle-WA-98109/48749425_zpid/
        </homedetails>
        <graphsanddata>
        http://www.zillow.com/homedetails/2114-Bigelow-Ave-N-Seattle-WA-98109/48749425_zpid/#charts-and-data
        </graphsanddata>
        <mapthishome>http://www.zillow.com/homes/48749425_zpid/</mapthishome>
        <comparables>http://www.zillow.com/homes/comps/48749425_zpid/</comparables>
    </links>
    <address>
        <street>2114 Bigelow Ave N</street>
        <zipcode>98109</zipcode>
        <city>Seattle</city>
        <state>WA</state>
        <latitude>47.637933</latitude>
        <longitude>-122.347938</longitude>
    </address>
    <zestimate>
        <amount currency="USD">1621376</amount>
        <last-updated>08/10/2016</last-updated>
        <oneWeekChange deprecated="true"/>
        <valueChange duration="30" currency="USD">-8021</valueChange>
        <valuationRange>
        <low currency="USD">1540307</low>
        <high currency="USD">1702445</high>
        </valuationRange>
        <percentile>97</percentile>
    </zestimate>
    <localRealEstate>
    <region name="East Queen Anne" id="271856" type="neighborhood">
    <zindexValue>742,400</zindexValue>
    <links>
    <overview>
    http://www.zillow.com/local-info/WA-Seattle/East-Queen-Anne/r_271856/
    </overview>
    <forSaleByOwner>
    http://www.zillow.com/east-queen-anne-seattle-wa/fsbo/
    </forSaleByOwner>
    <forSale>http://www.zillow.com/east-queen-anne-seattle-wa/</forSale>
    </links>
    </region>
    </localRealEstate>
    <regions>
    <zipcode-id>99569</zipcode-id>
    <city-id>16037</city-id>
    <county-id>207</county-id>
    <state-id>59</state-id>
    </regions>
</response>
</Zestimate:zestimate>
"""

xml = untangle.parse(xmldata)
print "URL", xml.Zestimate_zestimate.response.links.homedetails.cdata
print "Value $%s" % xml.Zestimate_zestimate.response.zestimate.amount.cdata
