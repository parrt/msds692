# HTTP

HTTP is the text-based protocol used to pass information between browser and server over the Internet. First, let's figure out how to make a simple request of a Web server and see what it gives us back.

## Connecting and requesting a page

Let's communicate with a server that does not require secure connections and access its web server (port 80) the hard way. Here is the protocol for handshaking with the Web server:

```
GET / HTTP/1.1
Host: www.cnn.com

```

The first line tells the server what page we are interested in (the root `/`). The `Host:` line indicates what server we think we are talking to. Then, we have to have a blank line which indicates we are done talking/handshaking. Please try out this sample session:

```
$ telnet www.openpayments.us 80
Trying 138.202.168.24...
Connected to sunshine.cs.usfca.edu.
Escape character is '^]'.
GET / HTTP/1.1
Host: www.openpayments.us

```

(blank line on the end.)

The server responds to you with:

```
HTTP/1.1 200 OK
Date: Mon, 09 Sep 2019 18:49:36 GMT
Last-Modified: Thu, 15 Jun 2017 17:55:26 GMT
Content-Type: text/html
Accept-Ranges: bytes
Content-Length: 9129
Server: Jetty(9.4.z-SNAPSHOT)


<!DOCTYPE html>
<html lang="en">
  <head>
...
</html>
```

It sends us back some headers, such as `Content-Type` and `Date`. Also, please note that *cookies* come back from the server to your web browser using these headers.

## Using python to get webpages

Now that we understand about networks, sockets, and the HTTP protocol, let's use Python to connect to a webpage and get the content. We will use [requests](http://docs.python-requests.org/en/master/). Try out the following script that should print out the HTML from CNN's webpage:


```python
import requests
r = requests.get('http://www.cnn.com')
print(r.text)
```

Here's how you do that from the commandline:

```bash
$ curl https://www.cnn.com > cnn.html
```

or

```bash
$ wget -O cnn.html https://www.cnn.com
```

**Exercise**: Using what you learned from previous lectures on extracting text from HTML, extract the text from URL `https://news.ycombinator.com` and print that out.