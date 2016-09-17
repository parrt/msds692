# REGISTER: https://www.zillow.com/user/Register.htm
# API REGISTER: https://www.zillow.com/webservice/Registration.htm
# API DOC: http://www.zillow.com/howto/api/APIOverview.htm

import sys
import untangle
import urllib2

KEY = sys.argv[1]  # your zillow api key/id as argument to script

# Find out how much property 64969892 is worth
zpid = '64969892'
QuoteURL = \
    "http://www.zillow.com/webservice/GetZestimate.htm?zws-id=%s&zpid=%s"
URL = QuoteURL % (KEY, zpid)
response = urllib2.urlopen(URL)
xmldata = response.read()  # read all data

print xmldata

xml = untangle.parse(xmldata)
print "URL", xml.Zestimate_zestimate.response.links.homedetails.cdata
print "Value $%s" % xml.Zestimate_zestimate.response.zestimate.amount.cdata
