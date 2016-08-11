HistoryURL = "http://ichart.finance.yahoo.com/table.csv?s=%s"

import sys
import urllib2

ticker = sys.argv[1]  # AAPL
response = urllib2.urlopen(HistoryURL % ticker)
csvdata = response.read()
print csvdata

"""
...
1998-02-23,20.125,21.624999,20.00,21.250001,119372400,0.694818
1998-02-20,20.50,20.5625,19.8125,20.00,81354000,0.653947
...
"""

# csv Python lib prefers reading from files, and it's easy to handle ourselves.
for row in csvdata.strip().split("\n"):
    cols = row.split(',')
    print cols
