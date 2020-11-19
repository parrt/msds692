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
response = requests.get(URL)
print(response.text)
