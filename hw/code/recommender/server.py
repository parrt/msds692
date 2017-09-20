from flask import Flask, render_template
from doc2vec import *
import sys

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""


@app.route("/article/<topic>/<filename>")
def article(topic,filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """


# initialization
glove_filename = sys.argv[1]
articles_dirname = sys.argv[2]

gloves = load_glove(glove_filename)
articles = load_articles(articles_dirname, gloves)

app.run(host='0.0.0.0', port=80)
