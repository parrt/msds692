from tfidf import *
import pickle
import sys

testfiles = [
	"33214newsML.xml",
	"33232newsML.xml",
	"33029newsML.xml",
	"32899newsML.xml",
	"32775newsML.xml",
	"32770newsML.xml",
	"32664newsML.xml",
	"32611newsML.xml",
	"32351newsML.xml",
	"32238newsML.xml",
	"3214newsML.xml",
	"32030newsML.xml",
	"2878newsML.xml",
	"2900newsML.xml",
	"2804newsML.xml",
	"2433newsML.xml",
	"198798newsML.xml"
]

zipfilename = sys.argv[1]
corpus = load_corpus(zipfilename)
print("Loaded %d files from %s" % (len(corpus), zipfilename))

with open('corpus.pkl', 'rb') as input:
    truth = pickle.load(input)

tfidf = compute_tfidf(corpus)

failures = 0
for fname in testfiles:
    scores = summarize(tfidf, corpus[fname], 20)

    # round to str with 3 decimals
    scores = [f"{item[1]:.3f} {item[0]}" for item in scores]
    truth[fname] = [f"{item[1]:.3f} {item[0]}" for item in truth[fname]] # round truth

    # sort both
    scores = sorted(scores, reverse=True)
    truth[fname] = sorted(truth[fname], reverse=True)

    if len(scores)!=len(truth[fname]):
        failures += 1
        print(f'-----------------\nFAIL {fname} EXPECTED {len(truth[fname])} scores FOUND {len(scores)}')
    elif scores!=truth[fname]:
        failures += 1
        print(f'-----------------\nFAIL {fname}')
        print(f"\t{'EXPECTED':<25s}\tFOUND")
        print('\t'+'\n\t'.join([f"{pair[0]:<25s}\t{pair[1]:<25s}" for pair in zip(truth[fname], scores)]))

if not failures:
    print("All tests pass")
