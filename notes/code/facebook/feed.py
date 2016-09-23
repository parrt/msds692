# https://developers.facebook.com/docs/facebook-login/access-tokens/
# https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow
# create an app ID https://developers.facebook.com/docs/apps/register
# register as dev, then select "basic app" to create new app ID. i used msan692-testing name
# ugh. had to drop my mobile and add again to get phone to verify my accout to get app ID
# browser will attempt to log the user in and FB does a redirect back to
# http://localhost:8000/?code=XXX

import sys
import BaseHTTPServer
import urlparse
import urllib
import urllib2
import json
import webbrowser

APP_CODE = None
APP_ACCESS_TOKEN = None

# Do $ python -m SimpleHTTPServer or do this:
def _wait_for_user_to_enter_browser():
    class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_GET(self):
            global APP_CODE, APP_ACCESS_TOKEN
            p = self.path.split('?')
            if len(p) > 1:
                params = urlparse.parse_qs(p[1], True, True)
                print params
                if p[0]=='/login':
                    APP_CODE = params['code'][0]
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write("You logged in!\n")
                # elif p[0]=='/exchange':
                #     print "exchange!!!"
                #     APP_ACCESS_TOKEN = params['access_token'][0]
                #     self.send_response(200)
                #     self.end_headers()
                #     self.wfile.write("Access token obtained!")
            return

    server_address = ('', 8000)
    httpd = BaseHTTPServer.HTTPServer(server_address, MyHandler)
    httpd.handle_request()

APP_ID = sys.argv[1]
APP_SECRET = sys.argv[2]

LOGIN_URL = "https://www.facebook.com/dialog/oauth" \
            "?client_id=%s" \
            "&redirect_uri=http://localhost:8000/login"
webbrowser.open_new_tab(LOGIN_URL % APP_ID)

_wait_for_user_to_enter_browser()

# Go get the app code (access token)

# redirect_uri arg appears to be ignored as no redirect is done to our server (none is running!)
# but it must be present
EXCH_URL = "https://graph.facebook.com/v2.3/oauth/access_token" \
           "?client_id=%s" \
           "&redirect_uri=http://localhost:8000/login" \
           "&client_secret=%s" \
           "&code=%s"
URL = EXCH_URL % (APP_ID, urllib.quote(APP_SECRET), urllib.quote(APP_CODE))
# print URL
#webbrowser.open_new_tab(URL)

response = urllib2.urlopen(URL)
jsondata = response.read()
json_dict = json.loads(jsondata)
ACCESS_TOKEN = json_dict['access_token']
# print ACCESS_TOKEN

# Ok, now we can pull data
# https://developers.facebook.com/docs/graph-api/using-graph-api/

def getfeed(who, ACCESS_TOKEN):
    FEED_URL = "https://graph.facebook.com/%s/feed?access_token=%s"
    FEED_URL = FEED_URL % (who, ACCESS_TOKEN)

    response = urllib2.urlopen(FEED_URL)
    jsondata = response.read()
    json_dict = json.loads(jsondata)

    for story in json_dict['data']:
        if "message" in story:
            print "http://www.facebook.com/"+story['id']
            print story["message"][0:80]
            print

def get_my_photos(ACCESS_TOKEN):
    FEED_URL = "https://graph.facebook.com/me/photos?access_token=%s"
    FEED_URL = FEED_URL % ACCESS_TOKEN

    response = urllib2.urlopen(FEED_URL)
    jsondata = response.read()
    json_dict = json.loads(jsondata)

    print json_dict

get_my_photos(ACCESS_TOKEN)

getfeed("whitehouse", ACCESS_TOKEN)  # works for pages (like msnbc) but not users

