import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../../data/SampleSuperstoreSales.csv")
print(df)

plt.scatter(df.Discount,df.Sales)
plt.show()