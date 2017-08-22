# CSV data

## Exporting data from Excel

Data of interest that we want to process in Python often comes in the form of an Excel spreadsheet. The easiest way to get access to it is to export the data in CSV format.

Let's get some data. Download [Sample Superstore Sales .xls file](https://community.tableau.com/docs/DOC-1236) or [my local copy](../data/SampleSuperstoreSales.xls) and open it in Excel. Select `File>Save As...` menu option and then "Comma separated values (.csv)" from the `Format:` drop-down menu. Set the filename to `SampleSuperstoreSales.csv` or similiar. That will warn you that the data cannot be saved as CSV without losing some information. Don't worry about that because it's only formatting and not data information that you will lose. Say "Save Active Sheet". Then it will helpfully give you a second warning. Tell it to continue.

If you use `cat` or `more` from the commandline, you will see some funny characters in the output:

<img src=figures/csv-funny-char.png width=600>

That weird `<A8>` character is ASCII code 168 (or A8 in hexadecimal). It turns out it's weirder than you think and is actually a two-byte character `U+00AE` encoding the registered trademark symbol &#x00AE;.  From experience with these data formats, it means that Excel is saving things using a "Latin-1" text encoding (0..255 char values). That encoding is essentially ASCII but anything above code 127 is Euro-specific. So, we need to fix that by stripping those out. 

We can accomplish that using the [iconv](https://www.gnu.org/software/libiconv/) command from the terminal:

```bash
$ iconv -c -f utf-8 -t ascii ~/data/SampleSuperstoreSales.csv > /tmp/t.csv
```

Ok, now we finally have some plain CSV data we can pull into Python:

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

The first two rows should look like:

```python
>>> print data[0]
['Row ID', 'Order ID', 'Order Date', 'Order Priority', 'Order Quantity', 'Sales', 'Discount', 'Ship Mode', 'Profit', 'Unit Price', 'Shipping Cost', 'Customer Name', 'Province', 'Region', 'Customer Segment', 'Product Category', 'Product Sub-Category', 'Product Name', 'Product Container', 'Product Base Margin', 'Ship Date']
>>> print data[1]
['1', '3', '10/13/10', 'Low', '6', '261.54', '0.04', 'Regular Air', '-213.25', '38.94', '35', 'Muhammed MacIntyre', 'Nunavut', 'Nunavut', 'Small Business', 'Office Supplies', 'Storage & Organization', 'Eldon Base for stackable storage shelf, platinum', 'Large Box', '0.8', '10/20/10']
```

We can extend that a little bit if we want that data in a numpy `array` (See the full [csv2numpy.py](https://github.com/parrt/msan692/blob/master/notes/code/csv2numpy.py)):
 
```python
data = np.array(data)
print type(data)
print data.shape # print the dimensions
print data
```

```bash
 $ python csv2numpy.py /tmp/u.csv
<type 'numpy.ndarray'>
(8400, 21)
[['Row ID' 'Order ID' 'Order Date' ..., 'Product Container'
  'Product Base Margin' 'Ship Date']
 ['1' '3' '10/13/10' ..., 'Large Box' '0.8' '10/20/10']
 ['49' '293' '10/1/12' ..., 'Jumbo Drum' '0.58' '10/2/12']
 ..., 
 ['7906' '56550' '4/8/11' ..., 'Small Pack' '0.41' '4/10/11']
 ['7907' '56550' '4/8/11' ..., 'Small Box' '0.56' '4/9/11']
 ['7914' '56581' '2/8/09' ..., 'Medium Box' '0.65' '2/11/09']]
```

**Exercise**: Extract the quantity and unit price columns and multiply them together to get the sale value. My solution uses a list comprehension across the list of lists, one per column I need. Then I create a numpy array of those and simply multiply them with `*`. Remember that `data[1:]` gives you all but the first element (a row in this case) of a list. `float(x)` converts string or integer `x` to a floating point number. If you get stuck, see [readcsv.py](https://github.com/parrt/msan692/blob/master/notes/code/readcsv.py).

## Pandas Data frames

In the end, the easiest way to deal with loading CSV files is probably with [Pandas](http://pandas.pydata.org/). For example, to load our sales CSV, we don't even have to open a file:

```python
table = pandas.read_csv("SampleSuperstoreSales.csv")
```

Pandas hides all of the details. I also find that pulling out columns is nice with pandas. Here's how to print the customer name column:

```python
names = table['Customer Name']
print names[0:5]
```

yields:

```
0    Muhammed MacIntyre
1          Barry French
2          Barry French
3         Clay Rozendal
4        Carlos Soltero
```

I also like to convert this to a numpy matrix so that I can pull out various rows conveniently:

```python
m = table.as_matrix()
print m[0:2]
```

yields:

```
[[1 3 '10/13/10' 'Low' 6 261.54 0.04 'Regular Air' -213.25 38.94 35.0
  'Muhammed MacIntyre' 'Nunavut' 'Nunavut' 'Small Business'
  'Office Supplies' 'Storage & Organization'
  'Eldon Base for stackable storage shelf, platinum' 'Large Box' 0.8
  '10/20/10']
 [49 293 '10/1/12' 'High' 49 10123.02 0.07 'Delivery Truck' 457.81 208.16
  68.02 'Barry French' 'Nunavut' 'Nunavut' 'Consumer' 'Office Supplies'
  'Appliances' '1.7 Cubic Foot Compact "Cube" Office Refrigerators'
  'Jumbo Drum' 0.58 '10/2/12']]
```

## CSV kung fu from the command line

You might be surprised how much data slicing and dicing you can do from the command line using some simple tools and I/O redirection + piping. (See [A Quick Introduction to Pipes and Redirection](http://bconnelly.net/working-with-csvs-on-the-command-line/#a-quick-introduction-to-pipes-and-redirection)).

We've already seen I/O redirection where we took the output of a command and wrote it to a file (`/tmp/t.csv`):
 
```bash
$ iconv -c -f utf-8 -t ascii ~/data/SampleSuperstoreSales.csv > /tmp/t.csv
```

Now, let me introduce you to the `grep` command that lets us filter the lines in a file according to a regular expression.

```bash
grep 'Annie Cyprus' ../data/SampleSuperstoreSales.csv
