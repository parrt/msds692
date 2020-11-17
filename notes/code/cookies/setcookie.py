from flask import Flask
from flask import request, make_response, redirect

app = Flask(__name__)

@app.route('/setcookie')
def cookie_insertion():
    response = app.make_response("i set some cookies. haha!\n")
    response.set_cookie('ID',value='212392932')
    return response

@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('ID')
   if name is None:
       return "<h1>You are a mysterious visitor</h1>"
   return '<h1>Welcome ID '+name+'</h1>'

app.run()
