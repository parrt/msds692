# HTTP

HTTP is the text-based protocol used to pass information between browser and server over the Internet. First, let's figure out how to make a simple request of a Web server and see what it gives us back.

## Connecting and requesting a page

Let's communicate with the CNN web server (port 80) the hard way. Here is the protocol for handshaking with the Web server:

```
GET / HTTP/1.1
Host: www.cnn.com

```

The first line tells the server what page we are interested in (the root `/`). The `Host:` line indicates what server we think we are talking to. Then, we have to have a blank line which indicates we are done talking/handshaking. Please try out this sample session:

```
$ telnet www.cnn.com 80
Trying 151.101.41.67...
Connected to turner-tls.map.fastly.net.
Escape character is '^]'.
GET / HTTP/1.1
Host: www.cnn.com

```

The server responds to you with:

```
HTTP/1.1 200 OK
access-control-allow-origin: *
cache-control: max-age=60
...
Set-Cookie: countryCode=US; Domain=.cnn.com; Path=/
Set-Cookie: geoData=San Jose|CA|95113|US|NA; Domain=.cnn.com; Path=/
Content-Type: text/html; charset=utf-8
Date: Sat, 08 Apr 2017 17:55:36 GMT

<!DOCTYPE html>
<html class="no-js">
<head>
...
</head>
...
</html>
```

It sends us back some headers, such as `Content-Type` and `Date`. Also, please note that *cookies* come back from the server to your web browser using these headers.

## Using python to get webpages

Now that we understand about networks, sockets, and the HTTP protocol, let's use Python to connect to a webpage and get the content. We will use [requests](http://docs.python-requests.org/en/master/), but I will sometime show you the `urllib2` version as well. Try out the following script that should print out the HTML from CNN's webpage:


```python
import requests
r = requests.get('http://www.cnn.com')
print r.text
```

Or, with `urllib2`:

```python
import urllib2
response = urllib2.urlopen("http://www.cnn.com")
html = response.read()
print html
```

In case you need it, here's how you would do that from the commandline:

```bash
$ curl http://www.cnn.com > cnn.html
```

or

```bash
$ wget -O cnn.html http://www.cnn.com
```

**Exercise**: Using what you learned from previous lectures on extracting text from HTML, extract the text from URL `http://docs.python-requests.org/en/master` and print that out.