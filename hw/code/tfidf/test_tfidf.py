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
