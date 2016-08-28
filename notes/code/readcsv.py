"Read Excel table from CSV file argument into list of lists"
import numpy as np
import sys
import csv

table_file = sys.argv[1]
with open(table_file, "rb") as csvfile:
    f = csv.reader(csvfile, dialect='excel')
    data = []
    for row in f:
        data.append(row)

# for row in data:
#     print row

# data = np.array(data)
# print type(data)
# print data

# Row ID,Order ID,Order Date,Order Priority,Order Quantity,Sales,Discount,Ship Mode,Profit,Unit Price,Shipping Cost,Customer Name,Province,Region,Customer Segment,Product Category,Product Sub-Category,Product Name,Product Container,Product Base Margin,Ship Date

quantity = np.array([float(d[4]) for d in data[1:]])
unitprice = np.array([float(d[9]) for d in data[1:]])
print quantity * unitprice

