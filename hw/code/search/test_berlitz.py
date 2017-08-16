import sys

from linear_search import linear_search

from index_search import index_search, create_index
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, filenames

"""
Run with

$ python -m pytest -v test_berlitz.py berlitz1rootdir
...
test_berlitz.py::test_linear_berlitz_none PASSED
test_berlitz.py::test_index_berlitz_none PASSED
test_berlitz.py::test_myhtable_berlitz_none PASSED
test_berlitz.py::test_linear_berlitz PASSED
test_berlitz.py::test_index_berlitz PASSED
test_berlitz.py::test_myhtable_berlitz PASSED
...
$
"""

rootdir = sys.argv[len(sys.argv) - 1]

print "testing with dir", rootdir


def test_linear_berlitz_none():
    terms = "missspellinnng"

    files = filelist(rootdir)

    terms = words(terms)

    linear_docs = linear_search(files, terms)

    expected = []
    assert filenames(linear_docs) == expected


def test_index_berlitz_none():
    terms = "missspellinnng"

    files = filelist(rootdir)

    terms = words(terms)

    index = create_index(files)
    index_docs = index_search(files, index, terms)

    expected = []
    assert filenames(index_docs) == expected


def test_myhtable_berlitz_none():
    terms = "missspellinnng"

    files = filelist(rootdir)

    terms = words(terms)

    index = myhtable_create_index(files)
    myhtable_docs = myhtable_index_search(files, index, terms)

    expected = []
    assert filenames(myhtable_docs) == expected


def dotest(terms, expected, which):
    files = filelist(rootdir)
    terms = words(terms)
    # print terms

    if which == 0:
        linear_docs = linear_search(files, terms)
        # print filenames(linear_docs)
        names = filenames(linear_docs)
        names.sort()
        expected.sort()	
        #assert filenames(linear_docs) == expected
        assert names == expected, "found "+str(names)+" != expected "+str(expected)
    elif which == 1:
        index = create_index(files)
        index_docs = index_search(files, index, terms)
        # print filenames(index_docs)
        names = filenames(index_docs)
        names.sort()
        expected.sort()
        #assert filenames(index_docs) == expected
        assert names == expected, "found "+str(names)+" != expected "+str(expected)
    else:
        index = myhtable_create_index(files)
        index_docs = myhtable_index_search(files, index, terms)
        # print filenames(index_docs)
        names = filenames(index_docs)
        names.sort()
        expected.sort()
        #assert filenames(index_docs) == expected
        assert names == expected, "found "+str(names)+" != expected "+str(expected)


def threetest(terms, expected):
    for i in range(3):
        dotest(terms=terms, expected=expected, which=i)


def test_hawaii_linear():
    dotest(terms="hawaii travel", expected=['HistoryHawaii.txt'], which=0)

def test_hawaii_index():
    dotest(terms="hawaii travel", expected=['HistoryHawaii.txt'], which=1)

def test_hawaii_myhtable():
    dotest(terms="hawaii travel", expected=['HistoryHawaii.txt'], which=2)

def test_greek_linear():
    dotest(terms="greek travel",
              expected=['WhatToGreek.txt', 'WhereToLosAngeles.txt', 'WhereToFrance.txt',
                        'WhatToJapan.txt', 'WhereToMadrid.txt', 'WhereToDublin.txt',
                        'WhereToEdinburgh.txt', 'WhereToEgypt.txt', 'HistoryGreek.txt',
                        'WhereToGreek.txt', 'WhereToIndia.txt', 'WhereToIsrael.txt',
                        'WhereToIstanbul.txt', 'WhereToItaly.txt', 'WhereToJapan.txt',
                        'WhereToJerusalem.txt'], which=0)

def test_greek_index():
    dotest(terms="greek travel",
              expected=['WhatToGreek.txt', 'WhereToLosAngeles.txt', 'WhereToFrance.txt',
                        'WhatToJapan.txt', 'WhereToMadrid.txt', 'WhereToDublin.txt',
                        'WhereToEdinburgh.txt', 'WhereToEgypt.txt', 'HistoryGreek.txt',
                        'WhereToGreek.txt', 'WhereToIndia.txt', 'WhereToIsrael.txt',
                        'WhereToIstanbul.txt', 'WhereToItaly.txt', 'WhereToJapan.txt',
                        'WhereToJerusalem.txt'], which=1)

def test_greek_myhtable():
    dotest(terms="greek travel",
              expected=['WhatToGreek.txt', 'WhereToLosAngeles.txt', 'WhereToFrance.txt',
                        'WhatToJapan.txt', 'WhereToMadrid.txt', 'WhereToDublin.txt',
                        'WhereToEdinburgh.txt', 'WhereToEgypt.txt', 'HistoryGreek.txt',
                        'WhereToGreek.txt', 'WhereToIndia.txt', 'WhereToIsrael.txt',
                        'WhereToIstanbul.txt', 'WhereToItaly.txt', 'WhereToJapan.txt',
                        'WhereToJerusalem.txt'], which=2)

def test_lisbon_linear():
    dotest(terms="lisbon",
              expected=['HistoryMadeira.txt', 'HandRLisbon.txt', 'IntroMadeira.txt',
                        'WhereToMadeira.txt'], which=0)

def test_lisbon_index():
    dotest(terms="lisbon",
              expected=['HistoryMadeira.txt', 'HandRLisbon.txt', 'IntroMadeira.txt',
                        'WhereToMadeira.txt'], which=1)

def test_lisbon_myhtable():
    dotest(terms="lisbon",
              expected=['HistoryMadeira.txt', 'HandRLisbon.txt', 'IntroMadeira.txt',
                        'WhereToMadeira.txt'], which=2)

def test_india_linear():
    dotest(terms="india", expected=['WhereToLosAngeles.txt', 'HistoryMalaysia.txt',
                                       'WhereToMalaysia.txt', 'WhatToIndia.txt',
                                       'IntroIndia.txt', 'WhereToEgypt.txt',
                                       'WhatToMalaysia.txt', 'HistoryEgypt.txt',
                                       'HistoryFrance.txt', 'HistoryFWI.txt',
                                       'HistoryGreek.txt', 'HistoryHongKong.txt',
                                       'WhereToIndia.txt', 'HistoryIndia.txt',
                                       'HistoryIstanbul.txt'], which=0)

def test_india_index():
    dotest(terms="india", expected=['WhereToLosAngeles.txt', 'HistoryMalaysia.txt',
                                       'WhereToMalaysia.txt', 'WhatToIndia.txt',
                                       'IntroIndia.txt', 'WhereToEgypt.txt',
                                       'WhatToMalaysia.txt', 'HistoryEgypt.txt',
                                       'HistoryFrance.txt', 'HistoryFWI.txt',
                                       'HistoryGreek.txt', 'HistoryHongKong.txt',
                                       'WhereToIndia.txt', 'HistoryIndia.txt',
                                       'HistoryIstanbul.txt'], which=1)

def test_india_myhtable():
    dotest(terms="india", expected=['WhereToLosAngeles.txt', 'HistoryMalaysia.txt',
                                       'WhereToMalaysia.txt', 'WhatToIndia.txt',
                                       'IntroIndia.txt', 'WhereToEgypt.txt',
                                       'WhatToMalaysia.txt', 'HistoryEgypt.txt',
                                       'HistoryFrance.txt', 'HistoryFWI.txt',
                                       'HistoryGreek.txt', 'HistoryHongKong.txt',
                                       'WhereToIndia.txt', 'HistoryIndia.txt',
                                       'HistoryIstanbul.txt'], which=2)
def test_dublin_and_hawaii_linear():
    dotest(terms="hawaii dublin", expected=[], which=0)

def test_dublin_and_hawaii_index():
    dotest(terms="hawaii dublin", expected=[], which=1)

def test_dublin_and_hawaii_myhtable():
    dotest(terms="hawaii dublin", expected=[], which=2)

test_lisbon_myhtable()

#test_hawaii()
#test_greek()
#test_lisbon()
#test_india()
#test_dublin_and_hawaii()
