# HTTP

HTTP is the text-based protocol used to pass information between browser and server over the Internet. First, let's figure out how to make a simple request of a Web server and see what it gives us back.

## Connecting and requesting a page

Let's communicate with a server that does not require secure connections and access its web server (port 80) the hard way. Here is the protocol for handshaking with the Web server:

```
GET / HTTP/1.1
Host: www.cnn.com

```

The first line tells the server what page we are interested in (the root `/`). The `Host:` line indicates what server we think we are talking to. Then, we have to have a blank line which indicates we are done talking/handshaking. Please try out this sample session (this URL still uses http not https so we can still use `telnet`):

```
$ telnet http://checkip.dyndns.org/ 80
$ telnet checkip.dyndns.org 80
Trying 216.146.43.71...
Connected to checkip.dyndns.com.
Escape character is '^]'.
GET / HTTP/1.1
HOST: checkip.dyndns.org

```

(blank line on the end.)

The server responds to you with:

```
HTTP/1.1 200 OK
Content-Type: text/html
Server: DynDNS-CheckIP/1.0.1
Connection: close
Cache-Control: no-cache
Pragma: no-cache
Content-Length: 102

<html>
<head>
<title>Current IP Check</title>
</head>
<body>
Current IP Address: 4.78.240.2
</body>
</html>
```

It sends us back some headers, such as `Content-Type` and the content length. Also, please note that *cookies* come back from the server to your web browser using these headers.

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