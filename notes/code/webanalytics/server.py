from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/track")
def hello():
    page = request.args.get('page', default='')
    if len(page)>0:
        print "Visit to page "+page
    return app.send_static_file('images/shim.gif')

app.run()
