## Searching streams

One of the most useful tools available on UNIX and the one you may use the most is grep. This tool matches regular expressions (which includes simple words) and prints matching lines to stdout.

The simplest incantation looks for a particular character sequence in a set of files. Here is an example that looks for any reference to System in the java files in the current directory.

```bash
$ grep System *.java
```

You may find the dot `.` regular expression useful. It matches any single character but is typically combined with the star, which matches zero or more of the preceding item. Be careful to enclose the expression in single quotes so the command-line expansion doesn't modify the argument. The following example, looks for references to any a forum page in a server log file:

```bash
$ grep '/forum/.*' /home/public/cs601/unix/access.log
```

or equivalently:

```bash
$ cat /home/public/cs601/unix/access.log | grep '/forum/.*' 
```

The second form is useful when you want to process a collection of files as a single stream as in:

```bash
$ cat /home/public/cs601/unix/access*.log | grep '/forum/.*'
```

If you need to look for a string at the beginning of a line, use caret `^`:

```bash
$ grep '^195.77.105.200' /home/public/cs601/unix/access*.log
```

This finds all lines in all access logs that begin with IP address 195.77.105.200.

If you would like to invert the pattern matching to find lines that do not match a pattern, use -v. Here is an example that finds references to non image GETs in a log file:

```bash
$ cat /home/public/cs601/unix/access.log | grep -v '/images'
```

Now imagine that you have an http log file and you would like to filter out page requests made by nonhuman spiders. If you have a file called spider.IPs, you can find all nonspider page views via:

```bash
$ cat /home/public/cs601/unix/access.log | grep -v -f /tmp/spider.IPs
```

Finally, to ignore the case of the input stream, use -i.

## Basics of file processing

**cut, paste**

```bash
cat ../data/coffee
```

cut grabs one or more fields according to a delimiter like strip in Python. It's also like SQL `select f1, f2 from file}.

```bash
cut -d ' ' -f 1 ../data/coffee > /tmp/1
cut -d ' ' -f 2 ../data/coffee > /tmp/2
```

```bash
cat /tmp/1
```

```bash
cat /tmp/2
```

paste combines files as if they were columns:

```bash
paste /tmp/1 /tmp/2
```

```bash
paste -d ', ' /tmp/1 /tmp/2
```

Get first and third column from names file

```bash
$ cut -d ' ' -f 1,3 names
```

`join` is like an INNER JOIN in SQL. (`zip()` in python) first column must be sorted.


```bash
$ cat ../data/phones
linux command line 131
132 exercises in computational analytics
parrt 5707
tombu 5001
jcoker 5099
$ cat ../data/salary
parrt 50
tombu  51
jcoker 99
$ join ../data/phones ../data/salary
parrt 5707 50
tombu 5001 51
jcoker 5099 99
```

Here is how I email around all the coupons for Amazon Web services without having to do it manually:

```bash
$ paste students aws-coupons
jim@usfca.edu	X
kay@usfca.edu	Y
sriram@usfca.edu	Z
...
```

and here is a little Python script to process those lines:

```python
import os
import sys
for line in sys.stdin.readlines():
    p = line.split('\t')
    p = (p[0].strip(), p[1].strip())
    print "echo '' | mail -s 'AWS coupon "+p[1]+"' "+p[0]
    os.system("echo '' | mail -s 'AWS coupon "+p[1]+"' "+p[0])
```

and here's how you run it:
 
```bash
$ paste students aws-coupons | python email_coupons.py 
```

## Processing log files

```bash
$ cut -d ' ' -f 1 access.log | sort | uniq -c | sort -r -n|head
```

Get unique list of IPs.

Find out who is hitting your site by getting histogram.

How many hits to the images directory? 

How many total hits to the website? 

Histogram of URLs.

