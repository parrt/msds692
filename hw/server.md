# Building web servers

## Goal

The goal of this homework is to build a dynamic website using [Flask](http://flask.pocoo.org/) that displays stock history in an HTML table.  Given "file" `/history/stockname`, your server will pull stock history for `stockname` from Yahoo finance as you did in a previous lab and display it in table form. You will learn both GET and POST HTTP "methods".

Once you have your server working locally, you will go to [python anywhere](http://pythonanywhere.com) and register for a basic (free) account.  You must get your server running so that outside users can access stock history using:

```
http://userid.pythonanywhere.com/history/AAPL
```

where `userid` is the user name you used when creating an account at Python anywhere (please make this the same as your github account!):

<img src=figures/pythonanywhere.png width=400>

Your server is like a proxy for Yahoo finance.

You will work in git repo *userid*-web.

## Description

###  A basic stock history table

First, get the `readcsv` function from your previous project into your new file `server.py`:

```python
def readcsv(data):
    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """
    ... same code from a previous project ...
```

You also need a function that uses `urllib` (not `urllib2` because that does not work at Python anywhere apparently; or at least you have to login via bash console and install) to fetch stock history from Yahoo finance:

```python
def gethistory(ticker):
    """
    Return header list, data (list of lists) for ticker,
    obtained from Yahoo finance.
    """
    ...
```

Using your previous functionality, create a function that returns HTML based upon a list of header names and a list of rows of data:

```python
def htmltable(headers, data):
    """Return an HTML table representing the headers and data."""
    ...
```

Your main program for the `server.py` script looks like the following.
 
```python
app = Flask(__name__)

@app.route(...) <-- fill this in too
def history(ticker):
    """
    In response to url /history/ticker, get data from Yahoo finance on
    ticker and return an HTML table representing that data.
    """
    ...
    
app.run() # kickstart your flask server
```

Run your server then verify that when you go to URL `http://localhost:5000/history/AAPL` you get AAPL's history.

### POST and forms

Now, add a new method and `route` for a landing page that answers to URL `/`. For the local host, that would look like: `http://127.0.0.1:5000/`. That method should serve a static file using `send_static_file()`. Please call that file `index.html`, which must be stored in a directory called `static` underneath your project directory.

Create an html `form` in `index.html` so that it looks like this:

<img src=figures/stock-form.png width=350>

The target of the form submission should be URL `/history` and **use POST not GET**. Then create a method and route to handle that URL:

```python
@app.route(...) <-- fill this in
def post_history():
    ...
```

In response to a POST, the method should pull out the `ticker` form value and do the same functionality as your previous `history` function. You can search for [How to obtain values of request variables using Python and Flask](https://www.google.com/#q=How+to+obtain+values+of+request+variables+using+Python+and+Flask), to get some help.

You can test POST from the commandline with `curl` and `--data` option:

```bash
$ curl --data "ticker=TSLA" http://parrt.pythonanywhere.com/history
    <html>
    <body>
    <table>
    <tr><th>Date</th><th>Open</th><th>High</th><th>Low</th><th>Close</th><th>Volume</th><th>Adj Close</th></tr>
<tr><td>2016-08-25</td><td>223.110001</td><td>223.800003</td><td>220.770004</td><td>220.960007</td><td>1756800</td><td>220.960007</td></tr>
<tr><td>2016-08-24</td><td>227.050003</td><td>227.149994</td><td>222.220001</td><td>222.619995</td><td>2564100</td><td>222.619995</td></tr>
...
```

That does a POST not get to that URL.

### JSON output

Let's also generate some JSON, not just an HTML table.

Add methods and routes as necessary so that URL `/data/`*ticker* such as `/data/TSLA` returns JSON output for the indicated stock ticker. It should look something like this in your browser:

<img src=figures/tsla-json.png width=200>

```bash
$ curl http://parrt.pythonanywhere.com/data/TSLA
{  "headers":["Date", "Open", "High", "Low", "Close", "Volume", "Adj Close"],
"data":[ ...
```

### Python anywhere

Now you have your server working, it's time to deploy it to a publicly visible website. Once you have created an account at Python anywhere, Go to your dashboard and then to the `Web` tab and create a Flask app with python 2.7.  He will ask you where you want your code to live. **Use all of the default values (`/home/parrt/mysite/flask_app.py`).**  I was unable to get it to run with anything but the default configuration. By default, it creates a simple hello world flask application like we did above. Also set the working directory to ``/home/parrt/mysite` from the "web app" dashboard at Python anywhere.

Once the web application has started, you can go to URL `http://userid.pythonanywhere.com` and it should give you the simple hello world output in your browser.

Now,  replace the code in `flask_app.py` at Python anywhere with the copy from your `server.py` code. (I literally cut and pasted it.) Look under the `Files` tab of your dashboard to find the files. **Do not copy the final line that starts up the server:**

```python
app.run() # kickstart your flask server
```

Apparently Python anywhere will do that for us. If you have this code in there, your website will not work.

Also copy your `index.html` file into a `static` directory underneath your `mysite`. Please note that you can start a bash shell up at that server and manipulate files.  I think it's called bash console or something when you're looking at the files tab.

Now go back into your web app configuration and tell it to reload. Then go back to URL `http://userid.pythonanywhere.com/history/APPL` and it should give you your stock data. You should be able to go to `http://userid.pythonanywhere.com/` as well to get your form up. Type in a valid stock ticker and verify that you get your results.

## Deliverables

*  `server.py`
*  A running website `http://userid.pythonanywhere.com/history/ticker` during the grading period where *userid* is your joint github/pythonanywhere.com ID.

## Evaluation

We will run your server locally and then use `wget` or `curl` from the commandline to pull data from your `server.py` at 127.0.0.1. We will also check that your website lives at `userid.pythonanywhere.com` and that it gives the same results.

For convenience, here is a [testing script](https://github.com/parrt/msds692/blob/master/hw/code/web/testserver.sh) and output:

```bash
$ ./testserver.sh output
Testing TSLA
output/TSLA.html and /tmp/TSLA.html same
output/TSLA.html and /tmp/post-TSLA.html same
output/TSLA.json and /tmp/TSLA.json same
Testing VBK
output/VBK.html and /tmp/VBK.html same
output/VBK.html and /tmp/post-VBK.html same
output/VBK.json and /tmp/VBK.json same
```

Note that the [sample html/json output](https://github.com/parrt/msds692/tree/master/hw/code/web/output) will differ from fresh fetches as stock data gets updated everyday. I will test with fresh data.
