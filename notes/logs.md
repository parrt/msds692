# Parsing log files

Most servers generate log information to so-called log files. One of the most common is the access log for a Web server such as this [sample log file](https://github.com/parrt/msan501/blob/master/data/access.log):

```
64.221.136.91 - - [02/Sep/2003:00:00:09 -0700] "GET / HTTP/1.1" 200 11690 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Win 9x 4.90; Q312461)"
64.221.136.91 - - [02/Sep/2003:00:00:10 -0700] "GET /images/shim.gif HTTP/1.1" 200 43 "http://www.antlr.org/" "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Win 9x 4.90; Q312461)"
...
```

Note: There is a [Python library to read log files](https://github.com/piwik/piwik-log-analytics) (though I have not tried that).

Reading in this file line by line of course very simple:

```python
filename = sys.argv[1]
f = open(filename, "r")
lines = f.readlines()
f.close()
```

Then, we could split on the space character to get the columns per row, but it splits row elements such as the following that really should be  treated as a single element:

```
"GET / HTTP/1.1"
```

Instead we get three strings

```
'"GET', '/', 'HTTP/1.1"'
```

Ok, so we cannot treat this as a simple space separated file and need to do some parsing. 

The easiest thing to do is probably use regular expressions to grab chunks of text that follow patterns of interest. The most important tool when using regular expressions is [pythex](http://pythex.org/) because it lets you visualize what portion of a string a regular expression matches. We will need three regular expressions, One to grab the IP address, such as `64.221.136.91`, one to grab the date field, such as `[02/Sep/2003:00:00:09 -0700]`, and one to grab the quoted strings. Here are the Python strings holding regular expressions that will get us what we want:

* `'^.*? '` Match non-greedily anything up to and including a space char from the start of the string.
* `'\\[.*\\]'` Match anything in between square brackets; as a regular expression, that is actually just `\[.*\]` but we need to escape the escape character in Python.
* `'".*?"'` Match non-greedily anything in between quotes

Here is what the regular expression visualizer shows for the quoted-string  grabber:

<img src=figures/pythex.png width=600>

Notice how it shows multiple things being selected, because multiple substrings match.

Ok, so how do we get the text associated with those expressions? The easiest thing to do is to call `findall` on each line, which will return a list of one or more elements that match:

```python
ip = re.findall('^.*? ', line)
ip = ip[0].strip()
```

```python
date_brackets = re.findall('\\[.*\\]', line)
date = date_brackets[0]
```

```python
quoted_strings = re.findall('".*?"', line)
```

Once we have these individual elements, we can pack them together as a single list to represent a record and add it to an overall list of records:

```python
records.append( [ip,date]+quoted_strings )
```

The records look like:

```bash
$ python load.py ~/github/msan501/data/access.log
['64.221.136.91', '[02/Sep/2003:00:00:09 -0700]', '"GET / HTTP/1.1"', '"-"', '"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Win 9x 4.90; Q312461)"']
['64.221.136.91', '[02/Sep/2003:00:00:10 -0700]', '"GET /images/shim.gif HTTP/1.1"', '"http://www.antlr.org/"', '"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Win 9x 4.90; Q312461)"']
...
```

That's pretty good but it seems like we should remove the square brackets and the quotes around those strings. We can do that with some simple string splicing:

```python
date = date[1:len(date)-1] # strip first and last character
quoted_strings = [s[1:len(s)-1] for s in quoted_strings]
```

Now the output looks like much cleaner: 
 
```
['64.221.136.91', '02/Sep/2003:00:00:09 -0700', 'GET / HTTP/1.1', '-', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Win 9x 4.90; Q312461)']
['64.221.136.91', '02/Sep/2003:00:00:10 -0700', 'GET /images/shim.gif HTTP/1.1', 'http://www.antlr.org/', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Win 9x 4.90; Q312461)']
...
```

Here is the [full source code](/code/logs/load.py) for this example.