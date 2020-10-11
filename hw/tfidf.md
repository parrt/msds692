# TFIDF with NLTK and Scikit-Learn

*All projects in this class are individual projects, not group projects.  You may not look at or discuss code with others until after you have submitted your own individual effort.*

## Goal

The goal of this homework is to learn a core technique used in text analysis called *TFIDF* or *term frequency, inverse document frequency*.  We will use what is called a *bag-of-words* representation where the order of words in a document don't matter--we care only about the words and how often they occur. A word's TFIDF value is often used as a feature for document clustering or classification. The more a term helps to distinguish its enclosing document from other documents, the higher its TFIDF score. As such, words with high TFIDF scores are often very good summarizing keywords for document.

As a practical matter, you will learn how to process some real XML files (Reuters articles) in Python.

You will work in git repo `tfidf-`*userid*.

## Description

### Reading in Reuters' XML

As a first step, let's grab text from a Reuters article in XML format. Download the `reuters-vol1-disk1-subset.zip` 12.8M compressed Reuters corpus (44M uncompressed, 9164 files) from the files area of Canvas for this class.  This data should not be made public so please don't post the articles anywhere.  You can uncompress it to look at the files but we will process the zip file directly. The articles (text files) in the zip file look like this fictitious file's contents:

```xml
<?xml version="1.0" encoding="iso-8859-1" ?>
<newsitem itemid="99" id="root" date="1996-10-21" xml:lang="en">
<title>Cats Do Hip Hop</title>
<dateline>USA 1996-10-21</dateline>
<text>
<p>Check this out.</p>
<p>Hilarious.</p>
</text>
<link>http://www.huffingtonpost.co.uk/2014/06/06/kittens-dance-turn-it-down-for-what_n_5458093.html</link>
<metadata>
<codes class="bip:countries:1.0">
  <code code="USA">
    <editdetail attribution="Cat Reuters BIP Coding Group" action="confirmed" date="1996-10-21"/>
  </code>
</codes>
<dc element="dc.date.created" value="1996-10-21"/>
<dc element="dc.source" value="Cat Reuters"/>
</metadata>
</newsitem>
```        

Unlike in previous labs where we used the simple `untangle`, this time we will use `ElementTree` from the standard library to process XML. (A [good tutorial on XML in Python](http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/)). Given the text of a file as a string, use `ET.fromstring()` and `ElementTree()` to parse the XML text. From this XML tree, you can ask it to find the `title` tag. Then use XPath notation with `tree.iterfind()` to grab all of the tags underneath the `<text>` tag. In our case, these will be `<p>` tags so use XPath `.//text/*`, which means "*from the current node, find all text tag descendants then all of their children.*"

When you are packing the text together, make sure to put a space in between the elements you join. Otherwise, you might end up putting two words together forming a new, nonsense word. 

In our main file called `tfidf.py`, create this function:

```python
import xml.etree.cElementTree as ET
...
def gettext(xmltext):
    """
    Parse xmltext and return the text from <title> and <text> tags
    """
    ...
```

### Tokenizing text

Now that we have some raw text without all of the XML, let's properly tokenize English text. It is a multistep process (and some of it you can take from prior projects/labs):

1. Convert everything to lowercase
2.  Strip punctuation, numbers, and `\r`, `\n`\, `\t`
3.  Tokenize using NLTK's `word_tokenize` function (You need to run `nltk.download()` to get the english tokenizer installed. It'll pop up a dialog box--select `all` and hit `download`)
4.  Drop words less than length 3
5.  Removes stop words using SciKit-Learn's `ENGLISH_STOP_WORDS` set. 
6.  Stem the words to help normalize the text.

*The easiest way to do this is to use the code I have placed in the starter kit.*

Make sure to lower case everything before you try to stem the words.

In `tfidf.py`, break this down into the two separate functions shown here:

```python
def tokenize(text):
    """
    Tokenize text and return a non-unique list of tokenized words
    found in the text. Normalize to lowercase, strip punctuation,
    remove stop words, drop words of length < 3.
    """
    ...
```

```python
def stemwords(words):
    """
    Given a list of tokens/words, return a new list with each word
    stemmed using a PorterStemmer.
    """
    ...
```

### Sample application

Our sample application for tokenization will be in `common.py` and will summarize an article by showing the most common words. The input file is specified as a commandline argument and used from Python via `sys.argv[1]`. Use the functions above to read in the XML, tokenize it, stem it, and then show the 10 most common words with their word count.  Use a `Counter` object to get the counts:

```python
xmltext = ... text from filename in sys.argv[1] ...
text = gettext(xmltext)
...
```

Then you can walk the `counts` and print the most common 10 words out. Note that when you iterate through them they come out with most common first. Very convenient.

**Sample output.** For file `33313newsML.xml` in our `reuters-vol1-disk1-subset` data directory, we would get the following output:

```
$ python common.py ~/data/reuters-vol1-disk1-subset/33313newsML.xml
gener 19
power 14
transmiss 14
new 12
said 12
electr 11
cost 10
zealand 9
signal 8
tran 7
```

Note that `generation`, `generated`, `generator` all stem to `gener`. It nicely summarizes the article!

After tokenization but before removing stop words, I get this list:

```
the 51
transmission 14
power 14
for 13
new 12
said 12
that 12
electricity 11
was 10
and 9
```

After removing stop words but before stemming, I see this list:

```
transmission 14
power 14
new 12
said 12
electricity 11
zealand 9
generators 8
costs 8
trans 7
signals 6
```

For file `33312newsML.xml`, I get the following final output:

```
$ python common.py ~/data/reuters-vol1-disk1-subset/33312newsML.xml
awb 8
wheat 6
tonn 6
said 6
steadi 4
price 4
crop 4
report 3
queensland 3
australian 2
```

For file `131705newsML.xml`, I get the following final output:

```
$ python common.py ~/data/reuters-vol1-disk1-subset/131705newsML.xml 
seita 4
share 3
franc 2
cancer 2
link 2
tobacco 2
fell 2
cigarett 2
go 2
affect 1
```

This works great but can we do better? 

### TFIDF

Our "most common word" mechanism is simple and pretty effective but not as good as we can do.  We need to penalize words that are not only common in that article but common across articles. E.g., `said` and `price` probably don't help to summarize an article as they are very common words.

We need to use TFIDF on a corpus of articles from which we can compute the term frequency across articles.  Here is how we will execute our program (`summarize.py`):

```bash
$ python summarize.py ~/data/reuters-vol1-disk1-subset.zip 33313newsML.xml
transmiss 0.428
gener 0.274
power 0.254
electr 0.253
zealand 0.235
tran 0.215
signal 0.214
esanz 0.191
cost 0.162
leay 0.143
gisborn 0.143
charg 0.131
new 0.130
island 0.128
auckland 0.113
effici 0.110
pricipl 0.096
eastland 0.096
```

So, we pass in the overall corpus and then a specific file for which we want the top TFIDF scored words. The output shows max 20 words and with **three decimals of precision**. Print only those words scoring >= 0.09. In your `summarize()` function, discard any terms with scores < 0.09 so that it is consistent with my "ground truth" and then your summarize.py file main program doesn't have to filter them.

We'll use `scikit-learn` to compute TFIDF for us.  There are lots of examples on the web how to use the `TfidfVectorizer` but the parameters I use are:

```python
def tokenizer(text):
    return stemwords(tokenize(text))
    
tfidf = TfidfVectorizer(input='content',
                        analyzer='word',
                        preprocessor=gettext,
                        tokenizer=tokenizer,
                        stop_words='english',
                        decode_error = 'ignore')
```                        

You should take my recommendation and use the arguments to `TfidfVectorizer()` as-is.

Function `gettext` is the imported function from `tfidf.py`.

Some files might have non-ascii char so you need tell `TfidfVectorizer()` to not puke (raise an exception) upon decoding error characters. See the [doc](http://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer).

Once you create that `tfidf` object, you can call function `fit` to compute all of the IDF (inverse document scores) for the corpus (list of doc strings) passed in. To get TFIDF scores for a document, call function `transform`, which returns a matrix whose rows are documents and whose columns are the words in the corpus vocabulary. It is actually a sparse matrix containing the (row,column) of the various words from the argument to `transform` plus the TFIDF scores:

```
  (0, 35257)	0.235473480686
  (0, 35011)	0.0094139540963
  (0, 34809)	0.0295038582366
  (0, 34761)	0.0219856151332
  ...
```

Calling `nonzero` on that matrix gives you the word indexes as the 2nd element of tuples like: (0,*word-index-we-want*). The "0" is because we've only passed in one document and so we only care about the word index which is the second index. So just walk those indexes and collect tuples with the feature names (the words) and the TFIDF.  Then sort them in reverse order according to the second element of the tuple, the TFIDF score.

For file `33312newsML.xml`, I get the following final output:

```
$ python summarize.py ~/data/reuters-vol1-disk1-subset.zip 33312newsML.xml
awb 0.698
wheat 0.328
tonn 0.251
crop 0.213
queensland 0.213
steadi 0.190
frost 0.148
assess 0.112
price 0.107
weekli 0.102
hard 0.095
impact 0.092
australian 0.092
```

Notice that `said` has dropped out and `price` has dropped significantly. Hooray!

For file `131705newsML.xml`, I get the following final output:

```
$ python summarize.py ~/data/reuters-vol1-disk1-subset.zip 131705newsML.xml
seita 0.733
cancer 0.255
cigarett 0.246
tobacco 0.225
link 0.176
overdon 0.150
franc 0.143
lung 0.141
fell 0.136
share 0.131
smoke 0.123
lawsuit 0.119
happen 0.093
studi 0.090
```

Notice that `share` and `go` have dropped out and `tobacco` and `cigarett` have move up in importance.

### Experiment

*Just for fun, not required*

To show how amazing TFIDF is, try an experiment where your `tokenize()` does not remove stopwords and then remove parameter `stop_words` from the `TfidfVectorizer` object. The TFIDF output is still the same, at least in terms of word order, though the scores will change. For example, if you run it again on `131705newsML.xml` without removing stop words, you will see scores:

```
seita 0.708
cancer 0.247
cigarett 0.237
tobacco 0.218
link 0.170
overdon 0.145
go 0.141
franc 0.138
lung 0.136
fell 0.132
share 0.127
smoke 0.119
lawsuit 0.115
happen 0.090
```

This shows that removing stop words is a waste of time for TFIDF as we get essentially the same results. For our purposes, however, let's leave in the stop word removal as we can then simply call our previous `tokenize` function.

## Getting started

I have provided a [starter kit](https://github.com/parrt/msds692/tree/master/hw/code/tfidf) with all of the commented function definitions you need. Also download the `reuters-vol1-disk1-subset.zip` file from the files area of Canvas. You will be processing that file as a zip but you can unzip it as well so that you can test individual files.

## Deliverables

In your repository `tfidf-`*userid*, you must have the following files in the root of your repository directory:
 
* `tfidf.py`; Implement methods `gettext()`, `tokenize()`, `stemwords()`, `compute_tfidf()`, `summarize()`, `load_corpus()`
* `common.py`; Print most common 10 "*word* *score*" pairs
* `summarize.py`; Print up to 20 scores with **three decimals of precision**

## Evaluation

*You must read xml files from the .zip file; don't extract then read nor assume files have been extracted!*

We will test your TFIDF functionality using `test_tfidf.py`, which uses the entire corpus for "training" but then uses just a small subset of the files for testing. For example, on my machine:

```bash
$ time python test_tfidf.py  ~/data/reuters-vol1-disk1-subset.zip 
Loaded 9164 files from /Users/parrt/data/reuters-vol1-disk1-subset.zip
All tests pass

real	0m32.524s
user	0m32.372s
sys	0m0.350s
```

Any difference in words or TFIDF scores are treated as a 0 for that test. There are 12 randomly-selected test files used and you must get everything right for each file. I have computed the right values and stored them in a pickled file, `corpus.pkl`, which is how the test compares your work for correctness. (It compares the filename to list of (value,tfidf score) tuples).

Your tests should run in less than about 45s when I test it on my fast box.

We will also make a quick check that your `common.py` and `summarize.py` scripts generate the right output.
