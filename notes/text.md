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
f.write(u'Watch: \u231A, Hourglass: \u231B\n')
f.close()
```

```bash
$ iconv -f utf-8 /tmp/utf8.txt 
Watch: ⌚, Hourglass: ⌛
```

## Language within a text file

If I tell you that a file is a text file, it tells you only that, with a proper decoder, the file represents a string of characters from a language's alphabet

compression, entropy