# Do "pip install python-linkedin"

import sys
from linkedin import linkedin
import BaseHTTPServer
import urlparse
import webbrowser

KEY = sys.argv[1]
SECRET = sys.argv[2]

token = None

def _wait_for_user_to_enter_browser(app):
    class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
        def do_GET(self):
            global token
            p = self.path.split('?')
            if len(p) > 1:
                params = urlparse.parse_qs(p[1], True, True)
                app.authentication.authorization_code = params['code'][0]
                app.authentication.state = params['state'][0]
                token = app.authentication.get_access_token()

    server_address = ('localhost', 8000)
    httpd = BaseHTTPServer.HTTPServer(server_address, MyHandler)
    httpd.handle_request()
    return token

# KEY = "wFNJekVpDCJtRPFX812pQsJee-gt0zO4X5XmG6wcfSOSlLocxodAXNMbl0_hw3Vl"
# SECRET = "daJDa6_8UcnGMw1yuq9TjoO_PMKukXMo8vEMo7Qv5J-G3SPgrAV0FqFCd0TNjQyG"
RETURN_URL = "http://localhost:8000/"
authentication = linkedin.LinkedInAuthentication(KEY, SECRET, RETURN_URL,
                                                 ['r_basicprofile'])
print authentication.authorization_url
webbrowser.open_new_tab(authentication.authorization_url)
application = linkedin.LinkedInApplication(authentication)

_wait_for_user_to_enter_browser(application)
print token # set in do_GET

# print application.get_companies(universal_names=['apple'],
#                                 selectors=['name'])

# print application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'})
print application.get_profile(member_url='https://www.linkedin.com/in/terence-parr-33530')
