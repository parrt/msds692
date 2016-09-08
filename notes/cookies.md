Cookies
====

HTTP is stateless and anonymous with a very simple request-response model.  In order to build websites like Amazon or any other website that lets you login, we need a mechanism for identifying users that come back to the same server. By identifying, we mean recognizing the same person, not actually knowing who they are.

HTTP is pretty simple but ~20 years ago, we came up with a good idea to support stateful communications between client and server. The idea is to piggyback key-value pairs called *cookies* as regular old headers already allowed within the HTTP protocol. These key-value pairs therefore do not affect the data payload (stuff after the headers).

The cookie mechanism relies on a simple agreement between client and server. The sequence goes like this when a client visits a server for the first time:

1. Server sends back one or more cookies to the browser via headers
2. Browser saves this information and then sends the same data back to the server for every future request associated with that domain

A *cookie* is a named piece of data (string) associated with a specific website/URL that is saved by the browser and is sent back to that same server with every page request. The server can use that as a key to retrieve data associated with that user.

If you erase your cookies for that domain, the server will no longer recognize you. Naturally, it will try to send you cookies again. It is up to the browser to follow the agreement to keep sending cookies and to save data.

Can I, as a server, ask for another server's cookies (such as amazon.com's)? No! Security breach! If another server can get my server's cookies, the other server/person can log in as me on my server. Heck, my cookies might even store credit card numbers (bad idea). It is up to the browser to enforce this policy. Naturally, it could send every cookie or even every document on your computer via headers to a server! In essence, we are trusting browser implementors.

A server can specify the lifetime of cookies in terms of seconds to live or that cookie should die when the browser closes. It can also tell the browser to delete a cookie immediately as part of the current request.

# Sample HTTP traffic with cookies

My first request to `cnn.com` results in a cookie coming back from cnn:

BROWSER SENDS:

```
GET http://www.cnn.com/ HTTP/1.1
host=www.cnn.com
connection=Close
accept=*/*

```

HEADERS FROM REMOTE SERVER (sets cookie with name `CG` to `US:CA:San+Francisco`):

```
date=Fri, 26 Sep 2014 18:33:38 GMT
server=nginx
set-cookie=CG=US:CA:San+Francisco; path=/         <--------------- COOKIE!
last-modified=Fri, 26 Sep 2014 18:33:06 GMT
expires=Fri, 26 Sep 2014 18:34:37 GMT
vary=Accept-Encoding
content-type=text/html
connection=close
cache-control=max-age=60, private
```

In the second HTTP request, we see that my browser is sending the cookie back to cnn.

BROWSER SENDS (sends cookie back to the server):

```
GET http://www.cnn.com/robots.txt HTTP/1.1
cookie=CG=US:CA:San+Francisco                     <--------------- COOKIE!
host=www.cnn.com
connection=Close
accept=*/*

```

HEADERS FROM REMOTE SERVER:

```
date=Fri, 26 Sep 2014 18:33:39 GMT
server=nginx
set-cookie=CG=US:CA:San+Francisco; path=/         <--------------- COOKIE!
vary=Accept-Encoding
x-ua-profile=desktop
content-type=text/plain
connection=close
cache-control=max-age=60, private
```

<img src=figures/chrome-cookies.png width=300>

<img src=figures/chrome-cookies2.png width=350>

<img src=figures/chrome-devtools-cookies.png width=300>


# How ad companies track you

The browser will send cookies to the server even for images, not just webpages. Ad companies embed images in websites and therefore can send you a cookie that your browser dutifully stores. For example, here is the cookie ad traffic I got when I *opened an email* from `opentable.com`:

```
BROWSER: GET http://oascnx18015.247realmedia.com/RealMedia/ads/adstream_nx.ads/www.opentable.opt/email-reminder/m-4/4234234@x26 HTTP/1.1
BROWSER HEADERS:
	accept-language=en-us
	host=oascnx18015.247realmedia.com
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


## Set cookies

To [Send cookies in flask](http://flask.pocoo.org/snippets/30/):

```python
@app.route('/set_cookie')
def cookie_insertion():
    redirect_to_index = redirect('/index')
    response = current_app.make_response(redirect_to_index )  
    response.set_cookie('cookie_name',value='values')
    return response
```

## Fetch cookies

[Flask cookie tutorial](http://www.tutorialspoint.com/flask/flask_cookies.htm)

```python
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   return '<h1>welcome '+name+'</h1>'
```

## Kill cookie


```python
resp.set_cookie(name, expires=0)
```
