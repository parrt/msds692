from flask import Flask
from flask import request
from collections import Counter
from html import HTML

app = Flask(__name__)

pageviews = Counter()

@app.route("/dashboard")
def dashboard():
    page = HTML()
    t = page.table()
    r = t.tr
    r.th("Count")
    r.th("Page name")
    for name in pageviews:
        r = t.tr
        r.td(str(pageviews[name]))
        r.td(name)
    return str(page)

@app.route("/track.gif")
def track():
    page = request.args.get('page', default='')
    if len(page)>0:
        pageviews[page] += 1
        print "Visit to page "+page
    return app.send_static_file('images/shim.gif')

app.run()
