from flask import Flask
from flask import request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return redirect('/homepage')

@app.route('/homepage')
def homepage():
    return "<h1>Home page</h1>"

app.run()
