# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

import sys
import webbrowser

from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results

"""
Usage:

$ python search.py linear ~/data/slate
$ python search.py index ~/data/slate
$ python search.py myhtable ~/data/slate
"""

impl = sys.argv[1]
rootdir = sys.argv[2]
files = filelist(rootdir)
# Uncomment the next line to test just the first 100 files instead of all files
# files = files[:100]
N = len(files)
print N, "files"

index = None

while True:
    terms = raw_input("Search terms: ")
    terms = words(terms)

    if impl=='linear':
        docs = linear_search(files, terms)
    elif impl == 'index':
        if index is None:
            index = create_index(files)
            print "Index complete"
        docs = index_search(files, index, terms)
    elif impl == 'myhtable':
        if index is None:
            index = myhtable_create_index(files)
            print "Index complete"
        docs = myhtable_index_search(files, index, terms)
    else:
        print "Invalid search type:", impl
        break
    page = results(docs, terms)
    f = open("/tmp/results.html", "w")
    f.write(page)
    f.close()
    webbrowser.open_new_tab("file:///tmp/results.html")
