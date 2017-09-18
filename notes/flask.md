# Python-based websites with flask

Making a web server in Python is fairly easy if we use, yet another library, [Flask](http://flask.pocoo.org/).  Flask provides *annotations* that **map URL paths to Python functions**. Every URL for which you want the server to respond, requires an annotation/function combination.
 
### Hello Flask

To get the hang of Flask, let's use a basic hello world.  Put the following Python code into `hello.py`.
 
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello MSAN692!\n"

app.run()
```

Run that from the commandline or from PyCharm.  You will see the following output at the beginning:

```
$ python hello.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

The default flask server listens at port 5000. To contact the server, we need the address of the machine, just our local host, and the port: 127.0.0.1:5000.

Now go to URL `http://127.0.0.1:5000` in your favorite browser (or click on that link if you are in PyCharm) and it should show text `Hello MSAN692!` in the browser. Or test it from the command line:

```bash
$ curl http://127.0.0.1:5000
Hello MSAN692!
```

**Exercise**: run your previous python "get" code using this URL to fetch the data. Now you have a server and a client on same machine talking to each other.

**Exercise**: Add this code so server spits out its IP address and have a partner use browser and python code from previous exercise to connect to your server. Then switch.

```python
import netifaces as ni
ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']
print "I'm at IP "+ip
...
app.run('0.0.0.0')
```

Ok, so that little Web server actually spits out lots of stuff that you don't see.  Using the `-v` option, you can see the entire conversation between the client, `curl`, and the server:

```bash
$ curl -v http://127.0.0.1:5000
* Rebuilt URL to: http://127.0.0.1:5000/
*   Trying 127.0.0.1...
* Connected to 127.0.0.1 (127.0.0.1) port 5000 (#0)
> GET / HTTP/1.1
> Host: 127.0.0.1:5000
> User-Agent: curl/7.49.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 15
< Server: Werkzeug/0.11.11 Python/2.7.12
< Date: Sun, 17 Sep 2017 19:11:27 GMT
< 
Hello MSAN692!
* Closing connection 0
```

Lines that start with `*`s look like informational notes to the user. Lines that start with `>` are the lines sent from the client to the server. Lines that start with `<` are the lines sent from the server back to the client.

Now, alter the URL that your server listens to by making this change:

```python
@app.route("/hello")
```

Restart your server. If you go to URL `http://127.0.0.1:5000/hello`, you should get the same output we saw before:

```bash
$ curl http://127.0.0.1:5000/hello
Hello MSAN692!
```

If you don't have `/hello`, you will get a "Not Found" error:

```bash
$ curl http://127.0.0.1:5000
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>
```

We can also use part of the URL as kind of a parameter. Make the following change:

```python
@app.route("/hello/<name>")
def hello(name):
    return "Hello %s!\n" % name
```

Restart your server and visit URL `http://127.0.0.1:5000/hello/parrt` should give output `Hello parrt!` in your browser:

```bash
$ curl http://127.0.0.1:5000/hello/parrt
Hello parrt!
```

Try it with different names after the `/hello/`:

```bash
$ curl http://127.0.0.1:5000/hello/Xue
Hello Xue!
```

*If you get error "address in use" or something like that, that means that you have a previous version of the program running somewhere. Or, sometimes you have to kill the program with control-C and then wait a minute or two for it to release that port.*

Try adding another function that return some text data with an annotation so that that there will be two URLs operating.

```pythhon
mydata = """
parrt, 10, 134.983
tombu, 11, 99.001
"""

@app.route("/data")
def foo():
        return mydata
```

Notice that the function name does not have to match the URL in any way.

Now, when we go to `http://127.0.0.1:5000/data`, we get that data in our browser:

```bash
$ curl http://127.0.0.1:5000/data

parrt, 10, 134.983
tombu, 11, 99.001
```

Notice that in the browser, it shows that data all on the same line. That's because the browser is expecting some HTML back and we sent it some text without HTML markup. The default is then just to show it all on the same line.

Modify the data so that it is an HTML string:

```python
mydata = """
<html>
<body>
<b>parrt</b>, 10, 134.983<br>
<b>tombu</b>, 11, 99.001<br>
</body>
</html>
"""
```

Now restart your server and visit the URL. You should see some nicely formatted data. Of course, now HTML will come to the command line if we use `curl`.

**Exercise**: Update your server so that it accepts URLs with an *argument*, `/data?format=txt`, and gives html by default or csv if `txt` format.

```python
from flask import request
...
mydata = """
parrt, 10, 134.983
tombu, 11, 99.001
"""
mydata_html = """
<b>parrt</b>, 10, 134.983<br>
tombu, 11, 99.001
"""
...
@app.route("/data")
def foo():
    if request.args.get("format")=='txt':
        return mydata
    else:
        return mydata_html
```
