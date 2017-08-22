"""For your reference; It defines what is in corpus.pkl"""
from tfidf import *
import pickle

testfiles = [
    "131679newsML.xml",
    "31930newsML.xml",
    "134529newsML.xml",
    "25775newsML.xml",
    "25828newsML.xml",
    "134424newsML.xml",
    "135959newsML.xml",
    "31902newsML.xml",
    "133023newsML.xml",
    "133062newsML.xml",
    "33313newsML.xml",
    "134130newsML.xml"
]

zipfilename = sys.argv[1]
corpus = load_corpus(zipfilename)
print "Loaded %d files from %s" % (len(corpus), zipfilename)

tfidf = compute_tfidf(corpus)

m = {}
for fname in testfiles:
    scores = summarize(tfidf, corpus[fname], 20)
    m[fname] = scores

output = open('corpus.pkl', 'wb')
pickle.dump(m, output)
output.close()
