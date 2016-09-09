Cookies
====

HTTP is stateless and anonymous with a very simple request-response model.  In order to build websites like Amazon or any other website that lets you login, we need a mechanism for identifying users that come back to the same server. By identifying, we mean recognizing the same "client," not actually knowing who they are.

HTTP is pretty simple but ~20 years ago, we came up with a good idea to support stateful communications between client and server. The idea is to piggyback key-value pairs called *cookies* as regular old headers already allowed within the HTTP protocol. These key-value pairs therefore do not affect the data payload (stuff after the headers).

The cookie mechanism relies on a simple agreement between client and server. The sequence goes like this when a client visits a server for the first time:

1. Server sends back one or more cookies to the browser via headers
2. Browser saves this information and then sends the same data back to the server for every future request associated with that domain/server

A *cookie* is a named piece of data (string) associated with a specific website/URL that is saved by the browser and is sent back to that same server with every page request. The server can use that as a key to retrieve data associated with that user.

Your browser keeps a dictionary of cookies for each server.  If you have 3 browsers, each would keep a separate dictionary. That's why logging in to Amazon with Chrome doesn't log you in if you switch to Firefox.

If you erase your cookies for that domain, the server will no longer recognize you. Naturally, the server will try to send you cookies again. It is up to the browser to follow the agreement to keep sending cookies and to save data.

Can I, as a server, ask for another server's cookies (such as amazon.com's)? No! Security breach! If another server can get my server's cookies, the other server/person can log in as me on my server. Heck, my cookies might even store credit card numbers (bad idea). It is up to the browser to enforce this policy. Naturally, it could send every cookie or even every document on your computer via headers to a server! In essence, we are trusting browser implementors.

A server can specify the lifetime of cookies in terms of seconds to live or that cookie should die when the browser closes. It can also tell the browser to delete a cookie immediately as part of the current request.

# Sample HTTP traffic with cookies

My first request to `cnn.com` results in a cookie coming back from cnn:

BROWSER SENDS:

```
GET / HTTP/1.1
Host: www.nytimes.com
connection=Close
accept=*/*

```

HEADERS FROM REMOTE SERVER (sets cookie with name `CG` to `US:CA:San+Francisco`):

```
HTTP/1.1 200 OK
Server: Apache
Vary: Host
X-App-Name: homepage
Cache-Control: no-cache
Content-Type: text/html; charset=utf-8
Transfer-Encoding: chunked
Date: Fri, 09 Sep 2016 18:09:32 GMT
Age: 1550
X-API-Version: 5-5
X-Cache: hit
X-PageType: homepage
nnCoection: close
X-Frame-Options: DENY
Set-Cookie: RMID=007f0102269d57d2fadd0006;Path=/; <--------------- COOKIE!Domain=.nytimes.com;Expires=Sat, 09 Sep 2017 18:09:32 UTC

```

In the second HTTP request, we see that my browser is sending the cookie back to cnn.

BROWSER SENDS (sends cookie back to the server):

```
GET www.amazon.com/robots.txt HTTP/1.1
cookie=CG=RMID=007f0102269d57d2fadd0006           <--------------- COOKIE!
host=www.cnn.com
connection=Close
accept=*/*

```

**Exercise:**  Open a fresh tab in your browser and open the developer tools. Then go to CNN.com in the URL text field. In chrome, you should see a bunch of cookies:

<img src=figures/cnn-cookies.png width=500>


# How ad companies track you

The browser will send cookies to remote servers even for images, not just webpages. Ad companies embed images in websites and therefore can send you a cookie that your browser dutifully stores. For example, here is the cookie ad traffic for realmedia.com that I got when I *opened an email* from `opentable.com`:

```
BROWSER: GET http://oascnx18015.247realmedia.com/RealMedia/ads/adstream_nx.ads/www.opentable.opt/email-reminder/m-4/4234234@x26 HTTP/1.1
...
REMOTE SERVER HEADERS:
	set-cookie=NSC_d18efmoy_qppm_iuuq=ffffffff09499e4a423660;path=/;httponly
	cache-control=no-cache,no-store,private
	pragma=no-cache
	...
```

There are a number of things to notice here:

1. The ad company, `realmedia.com`, tracks where the ad is using the URL: `www.opentable.opt/email-reminder/m-4/4234234@x26`. In other words, it knows that I opened the email from opentable. Yikes!
2. The headers turn off caching so that every time you refresh the page it gets notified.

Now, imagine that I go to a random website X that happens to have an ad from `realmedia.com`. My browser will send all cookies associated with `realmedia.com` to their server, effectively notifying them that I am looking at X. They will know about every page I visit that contains there ads.

Recently I was looking at hotels in San Diego and also purchasing some cat food on a different website. Then I went to Facebook and saw ads for the exact rooms and cat food I was looking for. This all works through the magic of cookies. There is a big ad clearinghouse where FB can ask if anybody is interested in serving ads to one of its users with a unique identifier. Hopefully they don't pass along your identity, but your browser still passes along your cookies for that ad server domain. The ad companies can then bid to send you an ad. Because your browser keeps sending the same cookies to them regardless of the website, hotel and pet food sites can show you ads for what you were just looking at on a completely unrelated site. wow.

This technology is not all bad. Obviously, Google analytics requires a tiny little image the embedded in your webpages so that it can track things and give you statistics.

# Accessing cookies in Python

Ok, now that we know how cookies piggyback on HTTP data packages and how they can be used for good and evil, let's work on some simple Python code that knows how to login and logout a user.

First some background. 

## Set cookies

**Exercise**: Make a server with one "route":

```python
@app.route('/setcookie')
def cookie_insertion():
    response = app.make_response("i set some cookies. haha!\n")
    response.set_cookie('ID',value='212392932')
    return response
```

Then look at the cookies and data coming back:

```bash
$ telnet 127.0.0.1 5000
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
GET /setcookie HTTP/1.1
Host: 127.0.0.1

HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 25
Set-Cookie: ID=212392932; Path=/
Server: Werkzeug/0.11.10 Python/2.7.11
Date: Fri, 09 Sep 2016 18:35:16 GMT

i set some cookies. haha!
Connection closed by foreign host.
$ 
```

Try doing the same thing in the browser using the developer tools to see the cookies.
 
## Fetch cookies

Once a server has sent cookies to a browser, the browser will send those back to the server upon each request. In order to get those cookies, the flask "view" function can simply pull them out from the dictionary. Very handy.

[Flask cookie tutorial](http://www.tutorialspoint.com/flask/flask_cookies.htm)

```python
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('ID')
   return '<h1>Welcome ID '+name+'</h1>'
```

**Exercise**: Upgrade the server from the previous section that set cookies to include this code to fetch the cookie. Now go to the browser in the following sequence to set and get cookies:

```
http://127.0.0.1:5000/setcookie
http://127.0.0.1:5000/getcookie
```

You should see `Welcome ID 212392932` in the browser. The key thing to note here is that there is no visible setting and getting of cookies in the URL or the displayed page. The displayed page magically knows the ID.

## Kill cookie

Servers need the ability to remove cookies from a browser's dictionary. To do that, we set the expiration date to "immediately":

```python
response.set_cookie(name, expires=0)
```

## Redirecting the browser

It's very common for a server to redirect the browser. The user goes to a specific page in their browser, but the server can send a response back to the browser that forces it to flip to a different page.

**Exercise**: Using the following code, create a flask server that redirects `/` to `/homepage`:
 
```python
@app.route('/')
def root():
    return redirect('/homepage')

@app.route('/homepage')
def homepage():
    return "<h1>Home page</h1>"
```

Go to the browser at http://127.0.0.1:5000/ and you will see the server get to request, one for the initial fetch and one for the fetch after redirection because of the 302 result code:
  
```
127.0.0.1 - - [09/Sep/2016 11:52:08] "GET / HTTP/1.1" 302 -
127.0.0.1 - - [09/Sep/2016 11:52:08] "GET /homepage HTTP/1.1" 200 -
```

Your browser should show "Home page" in big letters.

## A login/logout server

**Exercise**: Ok, now you have all the pieces necessary to create a server that logs people in and out.

First, create a server that looks for a cookie to determine whether someone is logged in or out:

```python
@app.route("/")
def home():
    user = request.cookies.get('ID') # get cookie called 'ID'
    if user:
        body = "logged in"
    else:
        body = "NOT logged in"
    return """
    <html>
    <h1>Home page</h1>
    %s
    </html>
    """ % body
```

When you go to `/` in the browser, you should see a page that says you're not logged in.

Also add a URL route for a bad login as we will need this later.

```python
@app.route("/badlogin")
def badlogin():
    return """
    <html>
    <h1>Bad login</h1>
    </html>
    """
```

Now we need to handle logging in with a route for URL `/login`. To simulate a database we can use a dictionary:

```python
passwords = {"parrt":"foo", "maryk":"bar"}
```

You can add whatever users you want there.

```python
@app.route("/login")
def login():
    # get user, password arguments
    user = ...
    password = ...
    if len(user)>0 and len(password)>0 and \
        user in passwords and password==passwords[user]:
        # create a redirect response that forces browser to flip pages to /
        response = ...
        # set cookie ID to a random number to simulate a real ID
        ID = str(random.randint(1000,200000))
        ...
    else:
        # bad password or unknown user.
        # redirect to /badlogin and do NOT set cookie
        response = ...
    return response
```

If you restart your server and turn on the developer tools then go to `http://127.0.0.1:5000/login?user=parrt&password=foo`, it should test for valid login and then redirect you to the homepage. If you look at the developer tools in chrome, you will see the following:

<img src=figures/fakelogin.png width=500>

Now, right-click on the cookie and tell it to delete. Refresh the browser, and it should then show you're not logged in on the homepage.

Finally, we need a way to log you out more gracefully than having to manually delete cookies.

```python
@app.route("/logout")
def logout():
    # delete 'ID' cookie and redirect to '//
    response = ...
    response.set_cookie(...)
    return response
```

Now restart your server and go to the login page `http://127.0.0.1:5000/login?user=parrt&password=foo` again. It will set your `ID` cookie and then send you to the homepage, showing that you are logged in. Now go to the `http://127.0.0.1:5000/logout` page in the browser, which will delete the `ID` cookie and go back to the homepage automatically.

Congratulations! You now fully understand how servers can log you in and out even in a stateless protocol like HTTP.