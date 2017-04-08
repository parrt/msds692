# Python-based websites with flask

Making a web server in Python is fairly easy if we use, yet another library, [Flask](http://flask.pocoo.org/).  Flask provides *annotations* that **map URL paths to Python functions**. Every URL for which you want the server to respond, requires an annotation/function combination.
 
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

Try adding another function within annotation, so that that there will be two URLs operating.

```pythhon
@app.route("/data")
def foo():
        return mydata
```

Notice that the function name does not have to match the URL in any way.  Let's say that `mydata` is CSV:

mydata = """
parrt, 10, 134.983
tombu, 11, 99.001
"""

Now, when we go to `http://127.0.0.1:5000/data`, we get that data in our browser.