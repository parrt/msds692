# REGISTER: https://www.zillow.com/user/Register.htm
# API REGISTER: https://www.zillow.com/webservice/Registration.htm
# API DOC: http://www.zillow.com/howto/api/APIOverview.htm

# Seems not to hit captcha Sept 2017

# Run with args: yourzipid
import sys
import untangle
import requests
import webbrowser


KEY = sys.argv[1]                       # your zillow api key/id as argument to script

# Find a house
SearchURL = "http://www.zillow.com/webservice/GetChart.htm?zws-id=%s&zpid=%s&unit-type=percent&width=500&height=250&chartDuration=10years"

URL = SearchURL % (KEY, '64969892')
r = requests.get(URL)
xmldata = r.text

xml = untangle.parse(xmldata)
code = xml.Chart_chart.message.code.cdata
if code=='0':
    zpid = xml.Chart_chart.response.url.cdata
    print(zpid)
else:
    msg = xml.Chart_chart.message.text.cdata
    print(msg)

webbrowser.open_new(zpid)
