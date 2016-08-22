# Representing text in a computer

As with everything else in the computer, we represent text using numbers. If you look at [7-bit ascii codes](http://www.asciitable.com/), you'll see how Americans encoded the English character set (upper and lower case, numbers, punctuation, and some other characters like newlines and tab). They represent the numbers < 127, which fits in 7 bits.  A string such as "abc" was represented by three bytes, one byte per character. It is a very dense encoding, meaning very few bits are wasted.

For a very long time, other languages were out of luck. A number of countries used the remaining 128..255 numeric values to encode characters useful to their language such as accented letters like ś and ŝ. The problem is that lots of countries used the number 201, but for different characters. Enter Unicode. See [Unicode vs ascii in python](https://docs.python.org/2/howto/unicode.html) for more details than I have here.

Unicode is an agreed-upon standard that maps characters to numeric values (called code points). Conveniently, the first 127 values map exactly to ASCII characters. Here is a [mapping of character to numeric value](http://unicode-table.com/en/). There are some maps, for example you can look directly at [how Bengali characters are encoded](http://unicode-table.com/en/blocks/bengali/):

<img src=figures/bengali.png width=700>

Reading from this table left to right,  the first character is 980+0, the second is 980+1, etc...  The only trick is that the numbers on the left are in hexadecimal. You will see the notation U+0981. Hexadecimal, base 16, is used because all possible values within 16 bits fit in 4 hexadecimal digits.

To represent Unicode we have to use 16-bit not 8-bit characters. Rats. Oh well, we can buy more memory. According to the documentation:

> Under the hood, Python represents Unicode strings as either 16- or 32-bit integers, depending on how the Python interpreter was compiled.

So, regular Python string `"abc"` takes three bytes but if we represented as a Unicode string, it takes 3 x 2 bytes = 6 bytes.  We can verify this char size with the `getsizeof` function:

```python
>>> from sys import getsizeof
>>> getsizeof('')   # 37 bytes of overhead for a string object
37
>>> getsizeof('a')
38
>>> getsizeof('ab')
39
>>> getsizeof('abc')
40
```

```python
>>> getsizeof(u'') # 50 bytes of overhead for a Unicode string object
50
>>> getsizeof(u'a')
52
>>> getsizeof(u'ab')
54
>>> getsizeof(u'abc')
56
```

Unicode strings are different objects than regular Python strings. We use notation `u'abc'` vs `'abc'` or `unicode('abc')`. We also have `unichr(x)` vs `chr(x)`:

```python
>>> chr(100)
'd'
>>> unichr(100)
u'd'
>>> chr(255)
'\xff'
```

If you give a character numeric value beyond what fits in one byte, you will get an error unless you indicate that it's Unicode character:

```python
>>> chr(3000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: chr() arg not in range(256)
>>> unichr(3000)
u'\u0bb8'
```

For fun, you can get the Unicode name from a numeric character value:

```python
>>> import unicodedata
>>> unicodedata.name(unichr(9999))
'PENCIL'
>>> unicodedata.name(unichr(9991))
'TAPE DRIVE'
```

The `\xFF` notation means FF in hexadecimal (all bits on) or 255 in decimal. A byte can be described in 2 hexadecimal digits, which is why we tend to use hexadecimal. 

To express 16 bit Unicode characters, we have to use the Unicode string not a regular string and we use `\uABCD` notation for a two byte character.

```python
>>> print u'\u00ab'
«
```

Note `\xAB` notation still works in Unicode strings.

## Text file encoding

*Now, let's make a distinction between strings and memory and text files stored on the disk.*

Storing a regular Python string with eight bit characters and will file is straightforward. Every character in the string is written to the file as a byte. Compression algorithms can reduce that space requirement but, for an uncompressed format, it's very tight.

Not so for 16-bit Unicode characters. Such largess doubles the size requirement to store a string, even if all of the characters fit in ASCII (< 127). 

Instead of blindly storing two bytes per character, we optimize for the case where characters fit within one byte using an *encoding* called **UTF-8**. UTF stands for "Unicode Transformation Format" but I typically call it "Unicode To Follow" because of the way it does encoding.  

UTF-8 is a simple encoding of Unicode strings that is optimized for the ASCII characters. In each byte of the encoding, the high bit determines if more bytes follow. A high bit of zero means that the byte has enough information to fully represent a character; ASCII characters require only a single byte. From [UTF-8](http://www.fileformat.info/info/unicode/utf8.htm):

1st Byte |   2nd Byte  |  3rd Byte  |  4th Byte  |  Number of Free Bits | Maximum Expressible Unicode Value
---------|---------|---------|---------|---------|---------
0xxxxxxx |  |||              7 |  007F |hex (127)
110xxxxx |   10xxxxxx |     |     | (5+6)=11  |  07FF hex (2047)
1110xxxx |   10xxxxxx  |  10xxxxxx   |     |(4+6+6)=16|  FFFF hex (65535)
11110xxx  |  10xxxxxx   | 10xxxxxx  |  10xxxxxx   | (3+6+6+6)=21 |   10FFFF hex (1,114,111)


*Encodings are used when converting between raw 8-bit bytes and 16-bit Unicode characters.* For example, the default file character encoding for files on a US computer is `UTF-8`. On a Japanese machine, the encoding might be `euc-jp`, which is optimized for the Japanese character set.

**Bottom line:** If you are reading text from a file, you must know the encoding. If you receive a file from Japan, you should not expect it to have the same encoding as a file created locally on your US machine. This becomes even more relevant when we start talking about computers communicating over the network. Strings must be encoded for efficiency

As we will see when discussing the HTTP web protocol, servers can send back headers that are essentially properties. One of the properties that browsers look for is the encoding of the data coming back from the server. Our computer science Web server, for example, response to page fetches with header (among other things):

```
content-type=text/html; charset=UTF-8
```

### Saving text

Ok, now let's write out some text using different encodings. First, let's write out a simple string of ASCII characters from a regular Python string:

```python
# Write an ASCII-encoded text file
f = open("/tmp/ascii.txt", "w")
f.write("Hi mom\n")
f.close()
```

We can verify that all of the bytes are associated with single characters:

```bash
$ od -c -t dC /tmp/ascii.txt 
0000000    H   i       m   o   m  \n                                    
           72 105  32 109 111 109  10                                    
0000007
$ od -c -t xC /tmp/ascii.txt 
0000000    H   i       m   o   m  \n                                    
           48  69  20  6d  6f  6d  0a                                    
0000007
```

You can look up the `od` command but the `-c` tells it to print out the bytes as characters and `-t dC` tells it to print out the decimal values of those characters; `-t xC` tells it to print those character values in hexadecimal.

Writing out a Unicode string should be done with an encoder and UTF-8 is the most commonly used encoder:

```python
# Write a UTF-8-encoded text file
import codecs
f = codecs.open('/tmp/utf8.txt', encoding='utf-8', mode='w')
f.write(u'Power: \u23FB, Stop: \u23F9\n')
f.close()
```

If we look at the file, we see
 
```bash
$ od -c /tmp/utf8.txt
0000000    P   o   w   e   r   :     342 217 273   ,       S   t   o   p
0000020    :     342 217 271  \n                                        
0000026
```

 If we try to look at that file with a browser, we see nonsense because the browser exists in ASCII text:
 
<img src=figures/utf8-chrome.png width=250>
 
We get a problem when we try to read it back in as ASCII:

```python
>>> f = open("/tmp/utf8.txt", "r")
>>> print f.read()
Power: ⏻, Stop: ⏹
```

This is actually misleading; I'm not sure why the Mac is printing something that looks like a stop button. The browser is showing nonsense which it should.

We have to read it back using a decoder:

```python
import codecs

f = codecs.open('/tmp/utf8.txt', encoding='utf-8', mode='r')
s = f.read()
f.close()
print repr(s)  # show a Python string representation of s
```

We get output `u'Power: \u23fb, Stop: \u23f9\n'`. If I print the string I don't see anything interesting because my development environment only knows about the ASCII character set. On a computer that had the proper "locale" set up, we would see a block the proper characters:

<img src=figures/start-stop.png width=40>

## Language within a text file

If I tell you that a file is a text file, it tells you only that, with a proper decoder, the file represents a string of characters from some language's alphabet.  Character-based (text) files are an incredibly common way to store information. All of the following types of files are text-based:

* comma-separate values (CSV)
* XML
* HTML
* Natural language text
* Python, JavaScript, Java, C++, any programming language
* JSON

Examples of non-textbased formats: mp3, png, jpg, .mpg, ...

As we learn to process data files, you will see that they are all textbased but the text inside follows the grammar of a specific format: CSV, XML, etc...

For your first project, you will be working with stock history obtained from Yahoo finance in CSV format. Your project will partially be to convert it to HTML, JSON, XML. The file sizes for the various formats are as follows.

```bash
$ ls -l
total 9728
-rw-r--r--@ 1 parrt  wheel   583817 Aug 22 12:06 AAPL.csv
-rw-r--r--  1 parrt  wheel  1177603 Aug 22 12:06 AAPL.html
-rw-r--r--  1 parrt  wheel  1438395 Aug 22 12:06 AAPL.json
-rw-r--r--  1 parrt  wheel  1771234 Aug 22 12:06 AAPL.xml
```

You can see that the same information takes a lot more storage, depending on the format. Compression tells us something about how much information is actually in a file. I discovered that when compressed the file sizes are very similar, indicating that all of the extra fluff in XML is a waste of space.

To compress everything with `7z`, we can use a simple `for` loop from the bash shell:

```bash
$ for f in *; do 7z a $f.7z $f; done
```

Then, we can look at the compressed file sizes:

```bash
$ ls -l *.7z
-rw-r--r--  1 parrt  wheel  146388 Aug 22 12:18 AAPL.csv.7z
-rw-r--r--  1 parrt  wheel  159252 Aug 22 12:18 AAPL.html.7z
-rw-r--r--  1 parrt  wheel  182134 Aug 22 12:18 AAPL.json.7z
-rw-r--r--  1 parrt  wheel  187013 Aug 22 12:18 AAPL.xml.7z
```

The ratio of original to compressed for CSV is 4 where is the ratio for JSON is 7.9 and 9.5 for XML. Hideous waste of space apparently for these other formats. The venerable CSV is actually pretty efficient way to store data as text. Of course, that doesn't mean we can't still compress it 4 to 1.