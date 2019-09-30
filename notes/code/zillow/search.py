# REGISTER: https://www.zillow.com/user/Register.htm
# API REGISTER: https://www.zillow.com/webservice/Registration.htm
# API DOC: http://www.zillow.com/howto/api/APIOverview.htm

# This seems to not get captcha Sept 2017

# Run with args: yourzipid "190 7th St APT 4" "San Francisco, CA"
import sys
import untangle
import requests

KEY = sys.argv[1]          # your zillow api key/id as argument to script
addr= sys.argv[2]          # "190 7th St APT 4"
citystatezip= sys.argv[3]  # "San Francisco, CA"

URL = f"http://www.zillow.com/webservice/GetSearchResults.htm?zws-id={KEY}&address={addr}&citystatezip={citystatezip}"

r = requests.get(URL)
xmldata = r.text
#print(xmldata)

xml = untangle.parse(xmldata)
code = xml.SearchResults_searchresults.message.code.cdata
if code=='0':
    zpid = xml.SearchResults_searchresults.response.results.result.zpid.cdata
    print(zpid)
else:
    msg = xml.SearchResults_searchresults.message.text.cdata
    print(msg)
