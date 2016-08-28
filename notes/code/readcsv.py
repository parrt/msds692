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

for row in data:
    print row

data = np.array(data)
print type(data)
print data