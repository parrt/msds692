# DOC on parameters: http://wern-ancheta.com/blog/2015/04/05/getting-started-with-the-yahoo-finance-api/

QuoteURL = "http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s"

import sys
import requests

ticker = sys.argv[1]  # AAPL
fields = "ab" # ask, bid price
r = requests.get(QuoteURL % (ticker,fields))
csvdata = r.text

# csv Python lib prefers reading from files, and it's easy to handle ourselves.
for row in csvdata.strip().split("\n"):
    cols = row.split(',')
    print cols
