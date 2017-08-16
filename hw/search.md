# Search Engine Implementation

The goal of this project is to learn how hashtables work and to *feel* just how much slower a linear search is. Along the way, you'll learn the basic mechanics of implementing a search engine, including displaying search results in a browser window and being able to navigate to documents. You'll also learn a tiny bit of HTML.

## Discussion

A **search engine** accepts one or more **terms** and searches a corpus for files matching all of those terms.  A **corpus** is just a directory and possibly subdirectories full of text files. If you go to the [American National corpus](http://www.anc.org/data/oanc/contents/), you'll see lots of fun text data. I have extracted articles from [Slate](https://github.com/parrt/msan692/blob/master/data/slate.7z) magazine and also from [Berlitz travelogues](https://github.com/parrt/msan692/blob/master/data/berlitz1.7z).  These are your data sets.  Berlitz is smaller and so I use that in some of my [unit tests](https://github.com/parrt/msan692/tree/master/hw/code/search/test_search.py).  Here is a fragment of a sample search results page as displayed in Chrome (activated from Python); clicking on a link brings up the actual file.

| HTML output        | File Content |
| ---------- | -----
| <img src="figures/search-page.png" width=300> |<img src="figures/search-file-page.png" width=350>|

In repo `search-`*userid*, you're going to implement 3 different search mechanisms using code derived from the [starter kit files](https://github.com/parrt/msan692/tree/master/hw/code/search). The actual search   mechanism of your code goes in these three files:

1. Linear search; file [linear_search.py](https://github.com/parrt/msan692/tree/master/hw/code/search/linear_search.py)
2. Hashtable via built in Python `dict` objects; file [index_search.py](https://github.com/parrt/msan692/tree/master/hw/code/search/index_search.py)
3. Hashtable that you implement yourself; file [myhtable_search.py](https://github.com/parrt/msan692/tree/master/hw/code/search/myhtable_search.py)

All three mechanism should give exactly the same results, but you will notice that the linear search is extremely slow. On my really fast machine with an SSD, it takes about five seconds to search through the Slate data. It has to open and search about 4500 files. With either of the hash tables, it's a matter of milliseconds.

File [search.py](https://github.com/parrt/msan692/tree/master/hw/code/search/search.py) is the main program, which you execute like this from the `search-`*userid* directory:

```bash
$ python search.py linear ~/data/slate
$ python search.py index ~/data/slate
$ python search.py myhtable ~/data/slate
```

assuming you have placed the `slate` directory under a `data` directory in your home directory.

Here is what the program looks like in action:

```bash
$ python search.py linear ~/data/slate
4534 files
Search terms: Reagan Iran
```

After you enter the search terms and hit return, the Python program pops up your default browser on the HTML file you have just generated as a result of the search.

**Please do not add data files to your repository!** I don't need them and it takes forever to download your repos if you add the data. 

### Linear search

Your first task is to perform a brain-dead linear search, which looks at each file in turn to see if it contains all of the search terms. If it does, that filename is included in the list (not `set`) of matching documents. The time complexity is *O(n)* for *n* total words in all files.

Given a list of fully-qualified filenames for files containing the search terms, the main program in [search.py](https://github.com/parrt/msan692/tree/master/hw/code/search/search.py) uses function `results()` to get a string containing HTML, which `search.py` writes to file `/tmp/results.html`. It then requests, via `webbrowser.open_new_tab()`, that your default browser open that page.

### HTML output

You can create whatever fancy HTML you want to show search results, but here is the basic form you should follow:

```
<html>
<body>
<h2>Search results for <b>ronald reagan</b> in 164 files</h2>
    
<p><a href="file:///Users/parrt/github/msan692/data/slate/1/Article247_42.txt">/Users/parrt/github/msan692/data/slate/1/Article247_42.txt</a><br>
A Shared Vision pairs Ronald Reagan and Margaret Thatcher. Yes, they<br><br>
    
<p><a href="file:///Users/parrt/github/msan692/data/slate/10/Article247_3363.txt">/Users/parrt/github/msan692/data/slate/10/Article247_3363.txt</a><br>
wartime. "I hope that neither President Carter or Governor Reagan, if he should<br>pay $5,000 and $3,500, respectively. After Ronald Reagan, who was elected<br><br>
    
<p><a href="file:///Users/parrt/github/msan692/data/slate/11/Article247_3408.txt">/Users/parrt/github/msan692/data/slate/11/Article247_3408.txt</a><br>
 I'd like to learn a decent salad dressing other than vinaigrette. Ideas? Well at least something other than the usual Masonic vinaigrette to Ronald Reagan brought the hall to its feet. The best of social<br><br>    
...    
</body>
</html>
```      

Notice that the links are URLs just like you see going to websites except they refer to a file on the local disk instead of another machine because of the `file://` prefix.  For example, if my data is in the `github/msan692/data` subdirectory of my home directory, we see URLs like:
 
```
file:///Users/parrt/github/msan692/data/slate/10/Article247_3363.txt
```

(My data is stored in a slightly different spot than yours will be.)

Also notice that in my search results, I am showing up to 2 lines containing at least one of the search term(s).

You can use the template engine [jinja2](http://jinja.pocoo.org/docs/2.9/), which is part of the flask webserver that we will use later, or just slap together strings in order to create the HTML.

### Creating an index using `dict`

Rather than looking through each file for every search, it's better to create a fast lookup index that maps a word to all of the files that contain that word. To compute the search results for multiple words, find the intersection of documents among the document set (`index[w]`) for each word. The resulting set will be just the documents that have all words.  `index[w]` returns a set (or unique list) of integers representing document indexes into your document list, `files`. In this way we don't have to duplicate the string for filenames in all of the `index` values. You can then convert a set of file indexes to filenames using the `files` list created during index creation.

It takes about the same time to create the index as it does to do one linear search because both are linearly walking through the list of files. The complexity of index creation is *O(n)* for *n* total words in all files. BUT, searching takes just *O(1)*, or constant time, once we have the index.  

The main program uses the following sequence for this `dict` version of the search engine:

```python
index = create_index(files) # files is a list of fully-qualified filenames
docs = index_search(files, index, terms) # terms is a list of normalized words
```

Once the index is created, function `index_search()` can crank out search results faster than you can take your fingers off the keyboard.

Here are the two key methods you must implement:
 
```python
def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """
```

```python
def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    doc IDs whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """
```

These functions will use expressions like `index[w]`, where `index` is a `dict`, to access the documents containing word `w`. 

### Creating an index using your own hashtable

This version of the search engine should look and perform just like the version using `dict`. The difference is **you cannot use the built-in dictionary operations** like `index[k]` for `dict` `index` and key `k`. You will build your own hashtable and call your own get and put functions explicitly to manipulate the index.

Because we are not studying the object-oriented aspects of Python, we are going to represent a hashtable as a list of lists (list of buckets):
 
```python
def htable(nbuckets):
    """Return a list of nbuckets empty lists"""
```

The number of buckets should be a prime number to avoid hash code collisions. in memory, the empty hash table looks like:

<img src=figures/hashtable-empty.png width=400>

Each element in a bucket is an association `(key,value)` where `value` is a set or unique list of document indexes. The buckets are themselves lists; do not confuse the buckets with the set of document indexes in each association. For example, `htable_put(index,'parrt', [99])` should add tuple `('parrt',[99])` to the bucket associated with key string `parrt`. The following method embodies the put operation:

```python
def htable_put(table, key, value):
    """
    Perform table[key] = value
    Find the appropriate bucket indicated by key and then append value to the bucket.
    If the bucket for key already has a key,value pair with that key then replace it.
    Make sure that you are only adding (key,value) associations to the buckets.
    """
```

*The functionality that replaces an existing key->value mapping is something we will not use here, but I include it here for completeness.*

In our case our values for the association are sets of document indexes.  If `ronald` is in documents 9 and 3 and `reagan` is in document 17 and both of those terms hashed to bucket 0, you would see the following 2-element bucket 0 with two associations:

<img src=figures/hashtable2.png width=800>


To make that work, you need a function that computes hash codes:

```python
def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
```

Notice that we are only computing hash codes for strings and integers. The hash code for a string could be just the sum of all of all the character ASCII codes, via `ord()`, but that would mean a lot of collisions like `pots` and `stop`.  A collision is when different keys hash to the same bucket. Ideally we would have one association per bucket. The "distribution" of elements to buckets is a function of how many buckets we have and how good our hash function is. The multiplication by prime number 31 starts shifting the bits around and gets a bit of "randomness" into our key computation.

The hash code is not directly used to get the bucket index because the hash code will typically be many times larger than the number of buckets.  The index of a bucket is the hash code modulo the number of buckets:

```python
bucket = hashcode(key) % nbuckets
```

To get a value out of the hash table associated with a particular key, we use this function:

```python
def htable_get(table, key):
    """
    Return table[key].
    Find the appropriate bucket indicated by the key and look for the association
    with the key. Return the value (not the key and not the association!)
    Return None if key not found.
    """
```

It computes the bucket where `key` lives and then linearly searches that (hopefully) small bucket for an association with key `key`. It then returns the value, the second element, from that association.

## Getting started

Please go to the [Search starterkit](https://github.com/parrt/msan692/tree/master/hw/code/search) and grab all the python files.  Store these in your repo `search-`*userid*, wherever you store that directory. E.g., I might put mine in `/Users/parrt/msan/search-parrt`.

Store the [Slate](https://github.com/parrt/msan692/blob/master/data/slate.7z) and [Berlitz](https://github.com/parrt/msan692/blob/master/data/berlitz1.7z) data sets outside of your repo so that you are not tempted to add that data to the repository. Perhaps you can make a general data directory for use in lots of classes such as `~/data` or just for this class `~/msan692/data`.

I recommend that you start by getting the simple linear search to work, which involves computing HTML and all of the basic machinery for extracting words from file content. So start by fleshing out `words.py` and `linear_search.py`.  You can use the unit tests in `test_search.py`, although the tests will fail for the indexed-based searches until you get those implemented. 

## Deliverables

You must complete and add these to root of your `search-`*userid* repository:

* htable.py
* index_search.py
* linear_search.py
* myhtable_search.py (no `dict`s allowed in this file!)
* words.py
* search.py (copy this from starterkit unchanged)
* test_htable.py (copy this from starterkit unchanged)
* test_search.py (copy this from starterkit unchanged)

**Please do not add the data to your repository!**

Ultimately, you want the test results to look like the following.

```bash
$ python -m pytest -v test_search.py 
...
test_search.py::test_linear_berlitz_none PASSED
test_search.py::test_index_berlitz_none PASSED
test_search.py::test_myhtable_berlitz_none PASSED
test_search.py::test_linear_berlitz PASSED
test_search.py::test_index_berlitz PASSED
test_search.py::test_myhtable_berlitz PASSED
...
$ python -m pytest -v test_htable.py 
...
test_htable.py::test_empty PASSED
test_htable.py::test_single PASSED
test_htable.py::test_a_few PASSED
test_htable.py::test_str_to_set PASSED
...
```

(You might need to install `pytest` with `pip`.)

I will test your project using something like the test file [test_search.py](https://github.com/parrt/msan692/tree/master/hw/code/search/test_search.py) but on a new data set you have not seen.

Let me point out that my unit tests are incredibly anemic and are meant only to show the basic mechanism of testing. You are free to extend the tests to include a lot more.

## Submission

To submit your project, ensure that all of your Python files are submitted to your repository. Those files should be in the root of your `search`-*userid* repository.

**Use of any `dict` objects within your `myhtable_search.py` file yields a 0 for that part of the project.**

Do not define any Python `class`es.

*Please do not add the data sets to your repository as it is a waste of space and network bandwidth.*
