import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/SampleSuperstoreSales.csv")

plt.scatter(df.Discount,df.Sales)
plt.show()