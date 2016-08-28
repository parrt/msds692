# Exporting data from Excel

Data of interest that we want to process in Python often comes in the form of an Excel spreadsheet. kept the easiest way to get access to it is to export the data in CSV format.

Let's get some data. Download [Sample Superstore Sales .xls file](https://community.tableau.com/docs/DOC-1236) or [my local copy](../data/SampleSuperstoreSales.xls) and open it in Excel. Select `File>Save As...` menu option and then "Comma separated values (.csv)" from the `Format:` drop-down menu. Set the filename to `SampleSuperstoreSales.csv` or similiar. That will warn you that the data cannot be saved as CSV without losing some information. Don't worry about that because it's only formatting and not data information that you will lose. Say "Save Active Sheet". Then it will helpfully give you a second warning. Tell it to continue.

If you use `cat` or `more` from the commandline, you will see some funny characters in the output and it will be all on one line:

<img src=figures/csv-funny-char.png width=800>

**First issue**. `^M` (control-M) is key sequence to get a "carriage return" character, which is the way Windows likes to see newlines. That is `'\r'` from within Python strings or the command line. Unix prefers "new line" (`^J`) so we need to flip that character (`'\n'` from Python strings or the command line).

**Second issue**. You will also see a weird `<A8>` character, which is ASCII code 168 (or A8 in hexadecimal). It turns out it's weirder than you think and is actually a two-byte character `U+00AE` encoding the registered trademark symbol &#x00AE;.  From experience with these data formats, it means that Excel is saving things using a [UTF-8](https://en.wikipedia.org/wiki/UTF-8) text encoding. Encoding is essentially ASCII but anything above code 127 gets encoded with 2 bytes not 1. So, we also need to fix that by stripping those out. 

We can accomplish that the first [iconv](https://www.gnu.org/software/libiconv/) command in the following script and the second command flips carriage return and newlines:

```bash
$ iconv -c -f utf-8 -t ascii ~/data/SampleSuperstoreSales.csv > /tmp/t.csv
$ tr '\r' '\n' < /tmp/t.csv > /tmp/u.csv
```

Ok, now we finally have some data we can pull into Python:

```
Row ID,Order ID,Order Date,Order Priority,Order Quantity,Sales,Discount,Ship Mode,Profit,Unit Price,Shipping Cost,Customer Name,Province,Region,Customer Segment,Product Category,Product Sub-Category,Product Name,Product Container,Product Base Margin,Ship Date
1,3,10/13/10,Low,6,261.54,0.04,Regular Air,-213.25,38.94,35,Muhammed MacIntyre,Nunavut,Nunavut,Small Business,Office Supplies,Storage & Organization,"Eldon Base for stackable storage shelf, platinum",Large Box,0.8,10/20/10
49,293,10/1/12,High,49,10123.02,0.07,Delivery Truck,457.81,208.16,68.02,Barry French,Nunavut,Nunavut,Consumer,Office Supplies,Appliances,"1.7 Cubic Foot Compact ""Cube"" Office Refrigerators",Jumbo Drum,0.58,10/2/12
...
```

##  Dealing with commas double quotes in CSV

For the most part, CSV files are very simple, but they can get complicated when we need to embed a comma. One such case from the above file shows how fields with commas get quoted:

```
"Eldon Base for stackable storage shelf, platinum"
```

What happens when we want to encode a quote? Well, somehow people decided that `""` double quotes was the answer (not!) and we get fields encoded like this:

```
"1.7 Cubic Foot Compact ""Cube"" Office Refrigerators"
```

The good news is that Python's `csv` package knows how to read Excel-generated files that use such encoding. Here's a sample script that reads such a file into a list of lists:

```python
import sys
import csv

table_file = sys.argv[1]
with open(table_file, "rb") as csvfile:
    f = csv.reader(csvfile, dialect='excel')
    data = []
    for row in f:
        data.append(row)
```

We can extend that a little bit if we want that data in a numpy `array`:
 
```python
data = np.array(data)
print type(data)
print data
```

```bash
 $ python csv2numpy.py /tmp/u.csv
<type 'numpy.ndarray'>
[['Row ID' 'Order ID' 'Order Date' ..., 'Product Container'
  'Product Base Margin' 'Ship Date']
 ['1' '3' '10/13/10' ..., 'Large Box' '0.8' '10/20/10']
 ['49' '293' '10/1/12' ..., 'Jumbo Drum' '0.58' '10/2/12']
 ..., 
 ['7906' '56550' '4/8/11' ..., 'Small Pack' '0.41' '4/10/11']
 ['7907' '56550' '4/8/11' ..., 'Small Box' '0.56' '4/9/11']
 ['7914' '56581' '2/8/09' ..., 'Medium Box' '0.65' '2/11/09']]
```

**Exercise**: Using