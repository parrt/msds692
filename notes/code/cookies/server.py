from flask import Flask
from flask import request, make_response, redirect
from collections import Counter
from html import HTML

app = Flask(__name__)

pageviews = Counter()

@app.route("/")
def home():
    user = request.cookies.get('user')
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
    user = request.args.get('user', default='')
    password = request.args.get('password', default='')
    if len(user)>0 and len(password)>0:
        redirect_to_home = redirect('/')
        response = app.make_response(redirect_to_home)
        response.set_cookie('user', value=user)
    else:
        redirect_to_home = redirect('/')
        response = app.make_response(redirect_to_home)
    return response

app.run()

