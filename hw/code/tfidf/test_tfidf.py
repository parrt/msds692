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

input = open('corpus.pkl', 'rb')
truth = pickle.load(input)
input.close()

tfidf = compute_tfidf(corpus)

failures = 0
for fname in testfiles:
    scores = summarize(tfidf, corpus[fname], 20)
    if len(scores)!=len(truth[fname]):
        failures += 1
        print '-----------------\nFAIL %s: EXPECTED %d scores FOUND %d' % (fname, len(truth[fname]),len(scores))
    elif scores!=truth[fname]:
        failures += 1
        print '-----------------\nFAIL %s: EXPECTED %s\nFOUND %s' % (fname, str(truth[fname]),str(scores))

if not failures:
    print "All tests pass"
