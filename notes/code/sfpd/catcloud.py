from wordcloud import WordCloud
from csvcols import get_columns
import matplotlib.pyplot as plt
import sys

categories = get_columns(sys.argv[1],col=1)

wordcloud = WordCloud(width=1800,
                      height=1400,
                      max_words=10000,
                      random_state=1,
                      relative_scaling=0.25)
wordcloud.fit_words(categories.most_common(len(categories)))

plt.imshow(wordcloud)
plt.axis("off")
wordcloud.to_file("SFPD-wordcloud.png")
plt.show()
