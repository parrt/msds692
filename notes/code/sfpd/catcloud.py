from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd
import sys

df_sfpd = pd.read_csv(sys.argv[1])

if len(sys.argv)>2:
	df_sfpd = df_sfpd[df_sfpd['Analysis Neighborhood']==sys.argv[2]]

df_sfpd = df_sfpd[~df_sfpd['Incident Category'].isnull()]
categories = Counter(df_sfpd['Incident Category'])

cloud = WordCloud(width=1800,
                      height=1400,
                      max_words=10000,
                      random_state=1,
                      relative_scaling=0.25)
cloud.fit_words(categories)

plt.imshow(cloud)
plt.axis("off")
cloud.to_file("SFPD-wordcloud.png")
plt.show()
