# Extracting text from HTML file

There are lots of data sources from which we might want to extract information, such as initial public offerings for various companies. E.g., [Tesla's IPO prospectus](https://www.sec.gov/Archives/edgar/data/1318605/000119312510017054/ds1.htm). One can imagine trying to mine such documents in an effort to predict which IPOs will flop.

HTML has both text as well as so-called markup like `<b>`, which is used to specify formatting information.

We will use the well-known [Beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python library to extract text. 

## Main script

Our main program accepts a file name parameter from the commandline, opens it, gets its text, converts the HTML to text, and close the file. Our first attempt, after looking at the documentation, might be the following (file `ipo-text.py`):


```python
import sys
from bs4 import BeautifulSoup

filename = sys.argv[1]
f = open(filename, "r")
html_text = f.read()
soup = BeautifulSoup(html_text, 'html.parser')
text = soup.get_text()
f.close()
print text
```

## Tidy up

Let's improve our program by creating a function to extract text from HTML text:

```python
def html2text(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text()
    return text
```

Then, our main program looks like:

```python
import sys
from bs4 import BeautifulSoup

def html2text(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text()
    return text

filename = sys.argv[1]
f = open(filename, "r")
html_text = f.read()
text = html2text(html_text)
f.close()
print text
```

## Stripping non-ASCII characters

If you try to redirect the output of that program to a file or even use a pipe to `more`, you see some characters beyond the 0..127 ASCII range. You will see the following error:

```bash
python ipo-text.py tesla.html > tesla.txt
...
UnicodeEncodeError: 'ascii' codec can't encode character u'\xa0' in position 197: ordinal not in range(128)
```

or

```bash
python ipo-text.py tesla.html | more
...
UnicodeEncodeError: 'ascii' codec can't encode character u'\xa0' in position 197: ordinal not in range(128)
```

That character is out of range (the "registered trademark" symbol), and the encoder will give us an error.  The character fits within one byte (value 0x92=146) but the Python string printing routine wants everything less than 128.  Note this is not a UTF-8 issue, because the HTML does not have multi-byte characters. The characters are simply out of range.

Fortunately this is very easy to fix. All we have to do is tell the string to encode self as ASCII before printing it out:

```python
text = text.encode('ascii', 'ignore')
print text
```

Which will strip out those non-ASCII characters. 

Now, we get the right output:

```bash
$ python ipo-text.py tesla.html
 S-1
 1
 ds1.htm
 REGISTRATION STATEMENT ON FORM S-1
 
 
 Registration Statement on Form S-1 
 
 
 Table of Contents 
 As filed with the Securities and Exchange Commission on January 29, 2010  
 Registration No. 333-                 
             UNITED STATES    SECURITIES AND EXCHANGE COMMISSION    Washington, D.C. 20549            FORM S-1  
   REGISTRATION STATEMENT    UNDER    THE SECURITIES ACT OF 1933            Tesla Motors, Inc.    (Exact name of Registrant as
specified in its charter)              
...
```

## Handling missing spaces

The problem with the output for the program so far is that we end up with text like `Largeacceleratedfiler` because the input HTML has `&nbsp;` (non-breaking space) tags that gets stripped (`Large&nbsp;accelerated&nbsp;filer`). We need to convert those to physical space characters with:

```python
html_text = html_text.replace('&nbsp;', ' ')
```

And, while we are at it, it's safest to tell beautiful soup to inject a space character in between any of the tags. Otherwise input `<b>hi</b>mom` gives output `himom`. A better version of our function is the following.

```python
def html2text(html_text):
    html_text = html_text.replace('&nbsp;', ' ') # replace html space specifier with space char
    soup = BeautifulSoup(html_text, 'html.parser')
    text = soup.get_text(' ', strip=False)  # space between tags, don't strip newlines
    return text
```


**Exercise**

* Print out the number of unique words in the document. For Tesla's IPO, I get 12884 unique words.
* Create a histogram using a dictionary that maps words to the word count. I use `defaultdict(int)` to define my histogram; very convenient. Print out the list of items and you will see things like `[('', 29449), ('considered,', 1), ('Leasehold', 2), ...`.
* Get rid of the blank strings by collapsing spaces and newlines into a single space using: `re.sub("[\\n ]+", ' ', text)`. I then get: `[('considered,', 1), ('S-8', 1), ('S-1', 5), ...`.
* Now, create the histogram the easy way using `Counter`. If you print that object, it will show you `Counter({'the': 6483, 'of': 5788, 'and': 4274, ...`.


## Stripping non-ASCII characters

If there are characters within the file that are non-ASCII and larger than 255, the file will have a two byte character. Here's a simple version of the problem I put into file `/tmp/foo.html`:

<img src=figures/html-funny-char.png width=75>

I deliberately injected a Unicode code point > 255, which requires two bytes to store.  Most of the characters require just one byte.

Here is how you could strip any non-one-byte characters from the file before processing:

```bash
$ iconv -c -f utf-8 -t ascii /tmp/foo.html 
<html>
<body>

</body>
</html>
```