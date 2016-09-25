# TFIDF with NLTK and Scikit-Learn

## Goal

The goal of this homework is to learn a core technique used in text analysis called *TFIDF* or *term frequency, inverse document frequency*.  We will use what is called a *bag-of-words* representation where the order of words in a document don't matter--we care only about the words and how often they are present. A word's TFIDF value is often used as a feature for document clustering or classification. We will use it simply as a summarization tool for document. The more a term helps to distinguish its enclosing document from other documents, the higher its TFIDF score.

As a practical matter, you will learn how to process some real XML files (Reuters articles) in Python.

You will work in git repo *userid*-tfidf.

## Description

### Reading in Reuters' XML

As a first step, let's grab text from a Reuters article in XML format. Download the 3.8M compressed reuters corpus (44M uncompressed, 9164 files) from the files area of Canvas for this class.  This data should not be made public so just uncompress on your disk but please don't post the articles anywhere.  The articles look like this fictitious file contents:

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

Unlike in previous labs where we used the simple `untangle`, this time we will use `ElementTree`. (A [good tutorial on XML in Python](http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/)). Given a filename, read in the xml as a string, then use `ET.fromstring()` and `ElementTree()` to parse the XML text. From this XML tree, you can ask it to find the `title` tag. Then use XPath notation with `tree.iterfind()` to grab all of the tags underneath the `<text>` tag. In our case, these will be `<p>` tags so use XPath `.//text/*`. It means "*from the current node, find all text tag descendants then all of their children.*"

When you are packing the text together, make sure to put a space in between the elements you join. Otherwise, you might end up putting two words together forming a new nonsense word. 

In a file called `common.py`, create this function:

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

Now that we have some raw text without all of the XML, let's learn how to properly tokenize English text. It is a multistep process:

1. Convert everything to lowercase
2.  Strip punctuation, numbers, and `\r`, `\n`\, `\t`
3.  Tokenize using NLTK's `word_tokenize` function (You need to run `nltk.download()` to get the english tokenizer installed. It'll pop up a dialog box--select `all` and hit `download`)
4.  Drop words less than length 3
5.  Removes stop words using SciKit-Learn's `ENGLISH_STOP_WORDS` set. 
6.  Stem the words to help normalize the text.

In `common.py`, break this down into the two separate functions shown here:

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

Our sample application for tokenization will be summarizing a file, which is specified as a commandline argument via `sys.argv[1]`. Use the functions above to read in the XML, tokenize it, stem it, and then show the 10 most common words with their word count.  Use a `Counter` object to get the counts and wrap your main script stuff so that it only executes if we run `common.py` (as opposed to importing it):

```python
if __name__=="__main__":
    xmltext = ... text from filename in sys.argv[1] ...
    text = gettext(xmltext)
    ...
    counts = Counter(tokens)
    ...
```

Then you can walk the `counts` and print the most common 10 words out. Note that when you iterate through them they come out with most common first. Very convenient.

**Sample output.** For file `33313newsML.xml` in our `reuters-vol1-disk1-subset` data directory, we would get the following output:

```
$ python common.py ~/data/reuters-vol1-disk1-subset/33313newsML.xml
gener 19
transmiss 14
power 14
said 12
new 12
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
awb 8
tonn 6
said 6
wheat 6
crop 4
price 4
steadi 4
queensland 3
report 3
hard 2
```


For file `131705newsML.xml`, I get the following final output:

```
seita 4
share 3
cancer 2
go 2
franc 2
fell 2
link 2
tobacco 2
cigarett 2
ad 1
```

This works great but can we do better? 

### TFIDF

Our "most common word" mechanism is simple and pretty effective but not as good as we can do.  We need to penalize words that are not only common in that article but common across articles. E.g., `said` and `price` probably don't help to summarize an article as they are very common words.

We need to use TFIDF on a corpus of articles from which we can compute the term frequency across articles.  Here is how we will execute our program (`tfidf.py`):

```bash
$ python tfidf.py ~/data/reuters-vol1-disk1-subset  ~/data/reuters-vol1-disk1-subset/33313newsML.xml
```

So, we pass in the overall corpus and then a specific file for which we want the top TFIDF scored words. The output we get should look like:

```
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

where the output shows **three decimals of precision**.  Print only those words, scoring >= 0.09.

We'll use `scikit-learn` to compute TFIDF for us.  There are lots of examples on the web how to use the `TfidfVectorizer` but the parameters I use are:

```python
def tokenizer(text):
    call tokenize() from common.py
    call stemwords() from common.py
    ...
    return ... # list of tokens (words)
    
tfidf = TfidfVectorizer(input='filename', # argument to transform() is list of files
                        analyzer='word',
                        preprocessor=gettext, # convert xml to text
                        tokenizer=tokenizer,  # tokenize, stem
                        stop_words='english') # strip out stop words
```                        

Function `gettext` is the imported function from `common.py`.

Some files might have non-ascii char so you need tell `TfidfVectorizer()` to not puke (raise an exception) upon decoding error characters. See the [doc](http://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer).

Once you create that object, you can call functions `fit` and `transform` or together as `fit_transform`. That will return to you a sparse matrix (not sure why) containing the  index of the various words from the argument to `transform` plus the TFIDF scores:

```
  (0, 35257)	0.235473480686
  (0, 35011)	0.0094139540963
  (0, 34809)	0.0295038582366
  (0, 34761)	0.0219856151332
  ...
```

Calling `nonzero` on that matrix gives you the word indexes as the 2nd element of tuples like: (0,*word-index-we-want*). So just walk those indexes and collect tuples with the feature names (the words) and the TFIDF.  Then sort them in reverse order according to the second element of the tuple, the TFIDF score. Print these out using three decimals precision for the TFIDF.

For file `33312newsML.xml`, I get the following final output:

```
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

For file `33212newsML.xml`, I get the following final output:

```
eoe 0.490
unilev 0.428
option 0.340
royal 0.314
dutch 0.279
amsterdam 0.217
aex 0.153
spark 0.099
exceed 0.098
netherland 0.096
conflict 0.096
trade 0.094
price 0.094
```

Notice that `trade` has dropped out and `option` has dropped a bit in importance. `eoe` (European Option Exchange) jumps to the top as it is fairly unique to this article probably.

### Experiment

To show how amazing TFIDF is, try an experiment where your `tokenize()` does not remove stopwords and remove parameter `stop_words` from the `TfidfVectorizer` object. The TFIDF output is still the same, at least in terms of word order, though the scores will change. kept for example, if you run it again on `33212newsML.xml` without removing stop words, you will see scores:

```
eoe 0.473
unilev 0.413
option 0.328
royal 0.303
dutch 0.269
amsterdam 0.210
aex 0.147
the 0.145
spark 0.096
exceed 0.095
netherland 0.093
conflict 0.093
trade 0.091
price 0.090
```

This shows that removing stop words is a waste of time as we get essentially the same results. For our purposes, however, let's leave in the stop word removal as we can then simply call our previous `tokenize` function.

## Deliverables

* common.py
* tfidf.py (Print scores with **three decimals of precision**)

## Evaluation

We will test your two Python scripts from the command line using a number of sample files and then compare some or all of the words in your output with ours. Any difference in counts or TFIDF scores are treated as a 0 for that test. 50% of your grade comes from each script.

Test your code to make sure you get the same answers I do in the samples above. Because it takes so long to execute, we will test your code for grading purposes on a smaller set.

**Test rig**.

```bash
$ ./testrig.sh ~/data/testing-reuters-vol1-disk1-subset ~/data/results-testing-reuters-vol1-disk1-subset
Testing tfidf.py
..............................................
Testing common.py
..............................................
```

Here is testrig.sh:

```bash
CORPUS=$1
OUTPUT=$2

echo "Testing tfidf.py"
for f in $CORPUS/*.xml
do
	echo -n .
	name=$(basename -s .xml $f)
	python tfidf.py $CORPUS $f > /tmp/$name.tfidf
	python wordcompare.py /tmp/$name.tfidf $OUTPUT/$name.tfidf
done
echo

echo "Testing common.py"
for f in $CORPUS/*.xml
do
	#echo $f
	echo -n .
	name=$(basename -s .xml $f)
	python common.py $f > /tmp/$name.count
	python wordcompare.py /tmp/$name.count $OUTPUT/$name.count
done
echo
```

Here is wordcompare.py:

```python
import sys

def todict(s):
    d = {}
    lines = s.strip().split('\n')
    for line in lines:
        pair = line.split(" ")
        value = pair[1]
        if value[0]=='.':
            value = '0'+value
        d[pair[0]] = value
    return d

f1 = sys.argv[1]
f2 = sys.argv[2]

s1 = open(f1).read()
s2 = open(f2).read()

d1 = todict(s1)
d2 = todict(s2)

if d1 != d2:
    print "%s %s differ" % (f1,f2)
    print d1
    print d2
```
