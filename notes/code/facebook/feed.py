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

def wait_for_user_to_login_via_browser():
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
            return

    httpd = BaseHTTPServer.HTTPServer(('', 8000), MyHandler)
    httpd.handle_request()

APP_ID = sys.argv[1]
APP_SECRET = sys.argv[2]

def authenticate(scopes="public_profile"):
    """
    Open browser to allow user to login, get authentication code,
    exchange to get (and return) access token.
    """
    scopes = urllib.quote(scopes)
    LOGIN_URL = "https://www.facebook.com/dialog/oauth" \
                "?client_id=%s" \
                "&redirect_uri=http://localhost:8000/login" \
                "&scope=%s"
    webbrowser.open_new_tab(LOGIN_URL % (APP_ID,scopes))

    wait_for_user_to_login_via_browser() # sets global APP_CODE (yuck)

    # Go get the app code (access token)

    # redirect_uri arg appears to be ignored as no redirect is done to our server (none is running!)
    # but it must be present
    EXCH_URL = "https://graph.facebook.com/v2.3/oauth/access_token" \
               "?client_id=%s" \
               "&redirect_uri=http://localhost:8000/login" \
               "&client_secret=%s" \
               "&code=%s"
    URL = EXCH_URL % (APP_ID, urllib.quote(APP_SECRET), urllib.quote(APP_CODE))

    response = urllib2.urlopen(URL)
    jsondata = response.read()
    json_dict = json.loads(jsondata)
    return json_dict['access_token']

def getfeed(ACCESS_TOKEN, who):
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

def get_my_id(ACCESS_TOKEN):
    FEED_URL = "https://graph.facebook.com/me?access_token=%s"
    FEED_URL = FEED_URL % ACCESS_TOKEN

    response = urllib2.urlopen(FEED_URL)
    jsondata = response.read()
    json_dict = json.loads(jsondata)

    print "me:", json_dict
    return json_dict['id']

def get_profile(ACCESS_TOKEN, uid, fields="email,name"):
    fields = urllib.quote(fields)
    FEED_URL = "https://graph.facebook.com/%s?access_token=%s&fields=%s"
    FEED_URL = FEED_URL % (uid,ACCESS_TOKEN,fields)

    response = urllib2.urlopen(FEED_URL)
    jsondata = response.read()
    # {u'friends': {u'data': [], u'summary': {u'total_count': 165}}, u'id': u'xxxx'}
    return json.loads(jsondata)

ACCESS_TOKEN = authenticate(scopes="user_friends,public_profile,email")

myid = get_my_id(ACCESS_TOKEN)
get_profile(ACCESS_TOKEN, myid, fields="friends")

getfeed(ACCESS_TOKEN, "whitehouse")  # works for public pages (like msnbc) but not users