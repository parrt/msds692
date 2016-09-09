from flask import Flask
from flask import request, make_response, redirect
import random

app = Flask(__name__)

passwords = {"parrt":"foo", "maryk":"bar"}

@app.route("/")
def home():
    user = request.cookies.get('ID') # get cookie called 'ID'
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
    # get user, password arguments
    user = request.args.get("user", '')
    password = request.args.get("password", '')
    if len(user)>0 and len(password)>0 and \
        user in passwords and password==passwords[user]:
        # create a redirect response that forces browser to flip pages to /
        # set cookie
        response = app.make_response(redirect('/'))
        ID = random.randint(1000,200000)
        response.set_cookie('ID', str(ID))
    else:
        # redirect to / and do NOT set cookie
        response = app.make_response(redirect('/badlogin'))
    return response

@app.route("/logout")
def logout():
    # delete 'user' cookie
    response = app.make_response(redirect('/'))
    response.set_cookie('ID', expires=0)
    return response

app.run()