from flask import Flask
from flask import request, make_response, redirect
from collections import Counter

app = Flask(__name__)

pageviews = Counter()

@app.route("/")
def home():
    user = ... # get cookie called 'user'
    if user:
        body = "logged in"
    else:
        body = "NOT logged in"
    return """
    <html>
    <h1>Home page</h1>
    %s
    </html>
    """ % body

@app.route("/badlogin")
def badlogin():
    return """
    <html>
    <h1>Bad login</h1>
    </html>
    """

@app.route("/login")
def login():
    # delete 'user' cookie
    return response

@app.route("/login")
def login():
    # get user, password arguments
    user = ...
    password = ...
    if len(user)>0 and len(password)>0:
        # create a redirect response that forces browser to flip pages to /
        # set cookie
        redirect_to_home = redirect('/')
        response = app.make_response(redirect_to_home)
        response.set_cookie('user', value=user)
    else:
        # redirect to / and do NOT set cookie
        redirect_to_home = redirect('/')
        response = app.make_response(redirect_to_home)
    return response

app.run()

