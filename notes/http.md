# HTTP

HTTP is the text-based protocol used to pass information between browser and server over the Internet. First, let's figure out how to make a simple request of a Web server and see what it gives us back.

## Connecting and requesting a page

Let's communicate with the "White House" Web server (port 80) the hard way.  What I have to type once I connect:

```
GET / HTTP/1.1
Host: whitehouse.com

```

The `Host:` line is followed by newline then another newline to get a blank line, indicating end of stuff I'm sending to the server.  Please try out this sample session:

```
$ telnet whitehouse.com 80
Trying 54.208.227.56...
Connected to whitehouse.com.
Escape character is '^]'.
GET / HTTP/1.1
Host: whitehouse.com

HTTP/1.1 200 OK
Content-Type: text/html
Last-Modified: Tue, 31 May 2016 15:51:11 GMT
Accept-Ranges: bytes
ETag: "0482a4154bbd11:0"
Server: Microsoft-IIS/7.5
X-Powered-By: ASP.NET
Date: Mon, 22 Aug 2016 20:10:05 GMT
Content-Length: 290

<html>
<head>
<title>WhiteHouse.com Official Site</title>
</head>
<body>
<center>
<h2>WhiteHouse.com Official Site</h2><h3><br><br><red>
Celebrating our 19th Anniversary (1997-2016)<br><br>
World's Most Famous Adult Site coming back Summer 2016
</red></h2></center>
</body>

</html>
```

Whoops.  I guess we meant `whitehouse.gov`. Anyway, it does send us back some headers, such as `Content-Type` and `Date`. Also, please note that *cookies* come back from the server to your web browser using these headers.

## Using python to get webpages

Now that we understand about networks, sockets, and the HTTP protocol, let's use Python to connect to a webpage and get the content. Try out the following script that should print out the HTML from CNN's webpage:

```python
import urllib2
response = urllib2.urlopen("http://www.cnn.com")
html = response.read()
print html
```

In case you need it, here's how you would do that from the commandline:

```bash
$ curl http://www.cnn.com
```

**Exercise**: Using what you learned from previous lectures on extracting text from HTML, extract the text from URL `https://docs.python.org/2/howto/urllib2.html` and print that out.