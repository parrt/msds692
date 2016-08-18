# Building web servers

## Goal

The goal of this homework is to build a dynamic website using [Flask](http://flask.pocoo.org/) that displays stock history in an HTML table.  Given "file" `/history/stockname`, your server will pull stock history for `stockname` from Yahoo finance as you did in a previous lab and display it in table form.

Once you have your server working locally, you will go to [python anywhere](http://pythonanywhere.com) and register for a basic (free) account.  You must get your server running so that outside users can access stock history using:

```
http://userid.pythonanywhere.com/history/AAPL
```

where `userid` is the user name you used when creating an account at Python anywhere:

<img src=figures/pythonanywhere.png width=400>

Your server is like a proxy for Yahoo finance.

## Description

### Hello Flask

To get the hang of Flask, let's use a basic hello world.  Put the following Python code into `hello.py`.
 
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello MSAN692!"

app.run()
```

Run that from the commandline or from PyCharm.  You will see the following output at the beginning:

```
$ python hello.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now go to URL `http://127.0.0.1:5000` in your favorite browser (or click on that link if you are in PyCharm) and it should show text `Hello MSAN692!` in the browser.

Now, alter the URL that your server listens to by making this change:

```python
@app.route("/hello")
```

If you go to URL `http://127.0.0.1:5000/hello`, you should get the same output we saw before. If you don't have `/hello`, you will get a "Not Found" error.

We can also use part of the URL as kind of a parameter. Make the following change:

```python
@app.route("/hello/<name>")
def hello(name):
    return "Hello %s!" % name
```

Restart your server and then URL `http://127.0.0.1:5000/hello/parrt` should give output `Hello parrt!` in your browser. try it with different names after the `/hello/`.

*If you get error "address in use" or something like that, that means that you have a previous version of the program running somewhere.*

## Stock history server
 
Now that you have the basic Flask mechanism figured out, let's build a real server. First, get the `readcsv` function from your previous project into your new file `history.py`:

```python
def readcsv(data):
    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """
    ... same code from a previous project ...
```

You also need a function that uses `urllib` (not `urllib2` because that does not work at Python anywhere apparently) to fetch stock history from Yahoo finance:

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

Your main program for the `history.py` script looks like the following.
 
```python
app = Flask(__name__)

@app.route(...)
def history(ticker):
    """
    In response to url /history/ticker, get data from Yahoo finance on
    ticker and return an HTML table representing that data.
    """
    ...
    
app.run() # kickstart your flask server
```

Run your server then verify that when you go to URL `http://localhost:5000/history/AAPL` you get AAPL's history.

### Python anywhere

Now you have your server working, it's time to deploy it to a publicly visible website. Once you have created an account at Python anywhere, Go to your dashboard and then to the `Web` tab and create a Flask app with python 2.7.  He will ask you where you want your code to live. **Use all of the default values (`/home/parrt/mysite/flask_app.py`).**  I was unable to get it to run with anything but the default configuration. By default, it creates a simple hello world flask application like we did above.

Once the web application has started, you can go to URL `http://userid.pythonanywhere.com` and it should give you the simple hello world output in your browser.

Now,  replace the code in `flask_app.py` at Python anywhere with your `history.py` code. Look under the `Files` tab of your dashboard to find the files. **Do not copy the final line that starts up the server:**

```python
app.run() # kickstart your flask server
```

Apparently Python anywhere will do that for us. If you have this code in there, your website will not work.

Now go back into your web app configuration and tell it to reload. Then go back to URL `http://userid.pythonanywhere.com/history/APPL` and it should give you your stock data.

## Deliverables

*  history.py
*  A running website `http://userid.pythonanywhere.com/history/ticker` during the grading period.

## Evaluation

We will run your server locally and then use `wget` or `curl` from the commandline to pull data from your `history.py` at 127.0.0.1. We will also check that your website lives at `userid.pythonanywhere.com` and gives the same results.
