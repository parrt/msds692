"Read Excel table from CSV file argument into a numpy array"
import numpy as np

import sys
import csv

table_file = sys.argv[1]
with open(table_file, "rb") as csvfile:
    f = csv.reader(csvfile, dialect='excel')
    data = []
    for row in f:
        data.append(row)

data = np.array(data)
print type(data)
print data
