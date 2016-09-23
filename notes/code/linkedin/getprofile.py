# Do "pip install python-linkedin"

import sys
from linkedin import linkedin
import BaseHTTPServer
import urlparse
import webbrowser

KEY = sys.argv[1]
SECRET = sys.argv[2]

def wait_for_user_to_login_via_browser(app):
    class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_GET(self):
            p = self.path.split('?')
            if len(p) > 1:
                params = urlparse.parse_qs(p[1], True, True)
                app.authentication.authorization_code = params['code'][0]
                app.authentication.state = params['state'][0]
                # POSTs to https://www.linkedin.com/uas/oauth2/accessToken
                app.authentication.get_access_token() # creates and sets app.token (access token)
            self.send_response(200)
            self.end_headers()
            return

    server_address = ('localhost', 8000)
    httpd = BaseHTTPServer.HTTPServer(server_address, MyHandler)
    httpd.handle_request()
    return

RETURN_URL = "http://localhost:8000/"
authentication = linkedin.LinkedInAuthentication(KEY, SECRET, RETURN_URL,
                                                 ['r_basicprofile'])
application = linkedin.LinkedInApplication(authentication)

# Now we need to trigger authentication

# GET to https://www.linkedin.com/uas/oauth2/authorization either asking user to click
# or directly with webbrowser open
# print authentication.authorization_url
webbrowser.open_new_tab(authentication.authorization_url)

wait_for_user_to_login_via_browser(application)

print authentication.token

# The authentication.token has been set so now we can make requests

print application.get_profile(member_url='https://www.linkedin.com/in/terence-parr-33530')

profile = application.get_profile(member_url='https://www.linkedin.com/in/terence-parr-33530')
print "%s %s, %s" % (profile['firstName'], profile['lastName'], profile['headline'])

profile = application.get_profile(member_url='https://www.linkedin.com/in/david-uminsky-5153b1a8')
print "%s %s, %s" % (profile['firstName'], profile['lastName'], profile['headline'])
