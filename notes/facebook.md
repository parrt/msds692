# Pulling data from Facebook

Our data collection application requires an app ID and secret from Facebook:

1. [Register/configure an App overview](https://developers.facebook.com/docs/apps/register)
2. [Create developer account](https://developers.facebook.com/async/onboarding/dialog/)
3. [Create new Facebook App](https://developers.facebook.com/apps/async/create/platform-setup/dialog/), which looks like:<br>
  <img src=figures/fb-add-app.png width=250><br>
  Click "Basic Setup" which is what we need for our unusual application.<br>
  <img src=figures/fb-create-id.png width=350><br>
  It will ask you to verify your account using phone or credit card. *Note that I had to drop my mobile phone from the account and re-add it in order for Facebook to allow me to create the application ID.*
4. You need to make sure that you have specified where Facebook should go during OAuth:<br>
<img src=figures/fb-oauth-settings.png width=400>

**Save the application ID you get, and in a safe place.** You will need it to communicate with Facebook's API.

Once you're set up, you should see a dashboard like this:
 
<img src=figures/fb-dashboard.png width=400>

Notice that under products it says "Facebook login" but you can add lots of other products, depending on what you'd like to do. In our case we simply want to try logging in as a particular person.

Make sure you enable the app:

<img src=figures/fb-enable-desktop-app.png width=600>

and set up security on the same page:

<img src=figures/fb-security.png width=400>

Facebook does not seem to have a supported Python library so we were going to do this with raw connections to their servers. It's complicated, but it truly exposes exactly how we must communicate.

## User Login Flow

*Despite being able to login as a user, we are not able to access all of our data without having Facebook review our application*. So, what we can extract is currently limited.

Here is how the [FaceBook Login Flow](https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow) goes.

First, we open a web browser to the following URL, which will ask the user to enter their username and password:

```
https://www.facebook.com/dialog/oauth?
  client_id={app-id}
  &redirect_uri={redirect-uri}
```

The Facebook site will attempt to log the user in and then  respond by doing a redirect back to our site per the `redirect_uri` parameter (which must match the URL we specified in the configuration of our application at Facebook's dashboard):

```
http://localhost:8000/login?code=XXX
```

The code must then be exchanged for an access token, again using your app ID and secret via URL:

```
https://graph.facebook.com/v2.3/oauth/access_token?
    client_id={app-id}
   &redirect_uri={redirect-uri}
   &client_secret={app-secret}
   &code={code-parameter}
```

Note that the `app-id` and `app-secret` should be kept private. Do not embed them in any HTML, JavaScript, or anything that could become public (such as in a webpage you post). I specify them on the commandline when I start up my application so as not to embed them anywhere.

The *code-parameter* is what you got back from login above.

If you are curious, you can read more about [securing your FB requests](https://developers.facebook.com/docs/graph-api/securing-requests/)

Once you have the access token, you can make requests to the [graph API](https://developers.facebook.com/docs/graph-api/using-graph-api/).

**Permissions.** You can use `user_friends`, `public_profile`, `email` without application review by Facebook. Still, we can't access everything within the profile. I seem to be able to get email, name, user ID, and total count of friends. That's it.

### Authenticating with Python

Here is a function that  provides the core functionality.

```python
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
```

 As usual, we need a simple Web server to retrieve the authentication code that comes back from Facebook:
 
```python
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
```

 Authentication is then just a matter of:
 
```python
ACCESS_TOKEN = authenticate(scopes="user_friends,public_profile,email")
```

Once we have that access token, we can make requests to the graph API. For example, here is a function to get your userid:

```python
def get_my_id(ACCESS_TOKEN):
    FEED_URL = "https://graph.facebook.com/me?access_token=%s"
    FEED_URL = FEED_URL % ACCESS_TOKEN

    response = urllib2.urlopen(FEED_URL)
    jsondata = response.read()
    json_dict = json.loads(jsondata)

    print "me:", json_dict
    return json_dict['id']
```

**Exercise**: Get all that Python code into a script and see if you can get it to print out your user ID.

**Exercise**: Create a new function that prints out how many friends you have. The URL you need is `https://graph.facebook.com/%s?access_token=%s&fields=%s` where the field you want is `friends`. Print out the json object you get back to find the structure and then dig in to get the total count of users.

**Exercise**: Create a function that accesses public feeds such as the White House or MSNBC:

```python
def getfeed(ACCESS_TOKEN, who):
    ...
```

The URL you need is `https://graph.facebook.com/%s/feed?access_token=%s`. Print the URL and first 80 characters or so of the feed post. For example, at the time I write this the first two entries look like:

```
http://www.facebook.com/63811549237_10154762657259238
"We are large, containing multitudes, full of contradictions. That's America. Th

http://www.facebook.com/63811549237_10154762686644238
"This weekend, we’ll dedicate the newest American icon on our National Mall—the 
```