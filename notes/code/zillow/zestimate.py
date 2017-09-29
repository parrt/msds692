# REGISTER: https://www.zillow.com/user/Register.htm
# API REGISTER: https://www.zillow.com/webservice/Registration.htm
# API DOC: http://www.zillow.com/howto/api/APIOverview.htm

# This one does not get captcha Sept 2017

import sys
import untangle
import requests

KEY = sys.argv[1]  # your zillow api key/id as argument to script

# Find out how much property 64969892 is worth
zpid = '64969892'
URL = "http://www.zillow.com/webservice/GetZestimate.htm?zws-id=%s&zpid=%s" % (KEY,zpid)
print URL
# response = requests.get(URL, params={"zws-id":KEY, "zpid":zpid})
response = requests.get(URL)
xmldata = unicode.encode(response.text, encoding='ascii', errors='ignore')

xml = untangle.parse(xmldata)
print "URL", xml.Zestimate_zestimate.response.links.homedetails.cdata
print "Value $%s" % xml.Zestimate_zestimate.response.zestimate.amount.cdata
