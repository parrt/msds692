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

# Using images for page analytics

Imagine a simple HTML file on some server xyz.com:

<img src=figures/pageimg.png width=400>

that displays a simple image in your browser:

<img src=http://www.antlr.org/images/icons/antlr.png>

Your browser makes **two** web requests, one to xyz.com and **another** to www.antlr.org for the image.

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

To send cookie back to the browser from a Java servlet:

1. set type of response to `text/html`
1. create `Cookie` object
1. `setMaxAge(interval-in-sec)` on cookie:
  * positive=num secs to live
  * negative = kill with browser
  * 0 = kill now
1. add cookie to `response`

```java
/** Set a cookie by name */
public static void setCookieValue(HttpServletResponse response,
								  String name,
								  String value)
{
	// Set-Cookie:user=parrt;Path=/;Expires=Thu, 25-Dec-2014 20:13:16 GMT
	Cookie c = new Cookie(name,value);
	c.setMaxAge( 3 * 30 * 24 * 60 * 60 ); // 3 months
	c.setPath( "/" );
	response.addCookie( c );
}
```

## Fetch cookies

The API provides only a method to get all cookies.  Have to search for
correct one:

```java
/** Find a cookie by name; return first found */
public static Cookie getCookie(HttpServletRequest request, String name) {
    Cookie[] allCookies;

    if ( name==null ) {
        throw new IllegalArgumentException("cookie name is null");
    }

    allCookies = request.getCookies();
    if (allCookies != null) {
        for (int i=0; i < allCookies.length; i++) {
            Cookie candidate = allCookies[i];
            if (name.equals(candidate.getName()) ) {
                return candidate;
            }
        }
    }
    return null;
}
```


```java
response.setContentType("text/html");
String user = request.getParameter("user");
setCookieValue(response, "user", ...);
```

See [CookieServlet.java](https://raw.githubusercontent.com/parrt/cs601/master/lectures/code/cookies/CookieServlet.java).

http://localhost:8080/cookies
http://localhost:8080/cookies?user=tombu

## Kill cookie

```java
private void killCookie(HttpServletResponse response, String name) {
    Cookie c = new Cookie(name,"false");
    c.setMaxAge( 0 ); // An age of 0 is defined to mean "delete cookie"
    c.setPath( "/" ); // for all subdirs
    response.addCookie( c );
}
```

# Who does CNN page contact?

Using my proxy, I see the following hosts contacted by a visit to the cnn.com home page.

```
	host=download.cdn.mozilla.net
	host=facebook.com
	host=download.cdn.mozilla.net
	host=download.cdn.mozilla.net
	host=download.cdn.mozilla.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-43.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-166-77.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-36.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-43.nodes.56m.dmtio.net
	host=fast.fonts.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-42.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-165-19.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-170-44.nodes.56m.dmtio.net
	host=z.cdn.turner.com
	host=cdn.clicktale.net
	host=cdn.optimizely.com
	host=www.cnn.com
	x-servedbyhost=prd-10-60-162-176.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-37.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-165-23.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-47.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-36.nodes.56m.dmtio.net
	host=z.cdn.turner.com
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-45.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-38.nodes.56m.dmtio.net
	host=cdn.krxd.net
	host=www.googletagservices.com
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-43.nodes.56m.dmtio.net
	host=i.cdn.turner.com
	host=131788053.log.optimizely.com
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-41.nodes.56m.dmtio.net
	host=hpr.outbrain.com
	host=i.cdn.turner.com
	host=i.cdn.turner.com
	host=i.cdn.turner.com
	host=131788053.log.optimizely.com
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-37.nodes.56m.dmtio.net
	host=i2.cdn.turner.com
	host=a.visualrevenue.com
	host=i.cdn.turner.com
	host=i.cdn.turner.com
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-49.nodes.56m.dmtio.net
	host=hpr.outbrain.com
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-49.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-170-44.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-162-176.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-166-101.nodes.56m.dmtio.net
	host=www.cnn.com
	x-servedbyhost=prd-10-60-170-40.nodes.56m.dmtio.net
	host=widgets.outbrain.com
	host=vrt.outbrain.com
	host=download.cdn.mozilla.net
	host=widgets.outbrain.com
	host=log.outbrain.com
	host=consent.truste.com
	host=z.cdn.turner.com
	host=cdn.livefyre.com
	host=data.cnn.com
	host=z.cdn.turner.com
	host=www.cnn.com
	x-servedbyhost=prd-10-60-168-49.nodes.56m.dmtio.net
	host=connect.facebook.net
	host=metrics.cnn.com
	host=www.cnn.com
	x-servedbyhost=prd-10-60-170-40.nodes.56m.dmtio.net
	host=b.scorecardresearch.com
	host=secure-us.imrworldwide.com
	host=cdn.gigya.com
```