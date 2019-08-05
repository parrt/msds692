import sys
import requests

HistoryURL = "https://www.quandl.com/api/v3/datatables/WIKI/PRICES.csv?ticker=%s&api_key=%s"

ticker = sys.argv[1]  # AAPL
APIKEY = sys.argv[2]

url = HistoryURL % (ticker,APIKEY)
r = requests.get(url)
csvdata = r.text
print(csvdata)
