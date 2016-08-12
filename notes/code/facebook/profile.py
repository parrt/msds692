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
import urllib2
import webbrowser

APP_CODE = None

# Do $ python -m SimpleHTTPServer or do this:
def _wait_for_user_to_enter_browser():
    class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_GET(self):
            global APP_CODE
            p = self.path.split('?')
            if len(p) > 1:
                params = urlparse.parse_qs(p[1], True, True)
                APP_CODE = params['code'][0]
                self.send_response(200)
                self.end_headers()
                self.wfile.write("Heh, you logged into Facebook!")

    server_address = ('', 8000)
    httpd = BaseHTTPServer.HTTPServer(server_address, MyHandler)
    httpd.handle_request()

KEY = sys.argv[1]

RETURN_URL = "http://localhost:8000/"

URL = "https://www.facebook.com/dialog/oauth?%%20client_id=%s&redirect_uri=http://localhost:8000/"
webbrowser.open_new_tab(URL % KEY)

_wait_for_user_to_enter_browser()

print "App code is", APP_CODE