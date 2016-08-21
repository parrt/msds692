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

fofo


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
>>> chr(3000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: chr() arg not in range(256)
>>> unichr(3000)
u'\u0bb8'
```
