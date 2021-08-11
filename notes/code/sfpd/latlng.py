import sys
import pandas as pd

filename = sys.argv[1]

df = pd.read_csv(filename)
print(df[['Latitude','Longitude']].head(5))
