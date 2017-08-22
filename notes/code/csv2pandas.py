"$ python code/csv2pandas.py ../data/FB-AAPL-2015.csv"

import sys
import pandas

table_file = sys.argv[1]
table = pandas.read_csv(table_file)

print "type is", type(table)
print "shape is", table.shape

print table['Customer Name'][0:5]

m = table.as_matrix()
print m[0:2]
