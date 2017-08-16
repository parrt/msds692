from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, filenames

rootdir = "/Users/parrt/github/msan501/data/berlitz1"


def test_linear_berlitz_none():
    terms = "missspellinnng"

    files = filelist(rootdir)

    terms = words(terms)

    linear_docs = linear_search(files, terms)

    expected = []
    assert filenames(linear_docs)==expected

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

def test_linear_berlitz():
    terms = "hawaii travel"

    files = filelist(rootdir)

    terms = words(terms)

    linear_docs = linear_search(files, terms)

    expected = ['HistoryHawaii.txt']
    assert filenames(linear_docs)==expected

def test_index_berlitz():
    terms = "hawaii travel"

    files = filelist(rootdir)

    terms = words(terms)

    index = create_index(files)
    index_docs = index_search(files, index, terms)

    expected = ['HistoryHawaii.txt']
    assert filenames(index_docs) == expected

def test_myhtable_berlitz():
    terms = "hawaii travel"

    files = filelist(rootdir)

    terms = words(terms)

    index = myhtable_create_index(files)
    myhtable_docs = myhtable_index_search(files, index, terms)

    expected = ['HistoryHawaii.txt']
    assert filenames(myhtable_docs) == expected

test_linear_berlitz()
