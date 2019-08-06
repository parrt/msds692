from bs4 import BeautifulSoup
import requests
import pandas as pd

html = requests.get('https://www.cde.ca.gov/nr/ne/yr12/yr12rel96.asp')
page = html.content
soup = BeautifulSoup(page, "lxml")
tables = soup.find_all('table')
for i,table in enumerate(tables):
	print(f"\nTable {i+1}")
	df = pd.read_html(str(table))[0]
	print(df)
