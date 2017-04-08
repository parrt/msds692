import sys
import requests

HistoryURL = "http://ichart.finance.yahoo.com/table.csv?s=%s"

ticker = sys.argv[1]  # AAPL
r = requests.get(HistoryURL % ticker)
csvdata = r.text
print csvdata

"""
...
1998-02-23,20.125,21.624999,20.00,21.250001,119372400,0.694818
1998-02-20,20.50,20.5625,19.8125,20.00,81354000,0.653947
...
"""

# csv is easy to handle ourselves:
for row in csvdata.strip().split("\n"):
    cols = row.split(',')
    print ', '.join(cols)
