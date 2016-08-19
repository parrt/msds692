# Exporting data from Excel

Data of interest that we want to process in Python often comes in the form of an Excel spreadsheet. kept the easiest way to get access to it is to export the data in CSV format.

Let's get some data. Download [Sample Superstore Sales .xls file](https://community.tableau.com/docs/DOC-1236) or [my local copy](data/SampleSuperstoreSales.xls) and open it in Excel. Select `File>Save As...` menu option and then "Comma separated values (.csv)" from the `Format:` drop-down menu. Set the filename to `SampleSuperstoreSales.csv` or similiar. That will warn you that the data cannot be saved as CSV without losing some information. Don't worry about that because it's only formatting and not data information that you will lose. Say "Save Active Sheet". Then it will helpfully give you a second warning. Tell it to continue.

If you use `cat` or `more` from the commandline, you will see some funny characters in the output and it will be all on one line:

<img src=figures/csv-funny-char.png width=800>

`^M` (control-M) is key sequence to get a "carriage return" character, which is the way Windows likes to see newlines. That is `'\r'` from within Python strings or the command line. Unix prefers "new line" (`^J`) so we need to flip that character (`'\n'` from Python strings or the command line).  You will also see a weird `<A8>` character, which is ASCII code 168 (or A8 in hexadecimal). It turns out it's weirder than you think and is actually a two-byte character `U+00AE` &#00AE;

```bash
$ iconv -c -f utf-8 -t ascii ~/data/SampleSuperstoreSales.csv > /tmp/t.csv
$ tr '\r' '\n' < /tmp/t.csv > /tmp/u.csv
```