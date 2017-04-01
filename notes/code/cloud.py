from wordcloud import WordCloud
import matplotlib.pyplot as plt
import sys

from collections import Counter

f = open(sys.argv[1])
text = f.read()
words = text.split(' ')

histo = Counter(words) # create histogram of words
# get most common (key,count) pairs and back to dict
top = dict(histo.most_common(50))

wordcloud = WordCloud(width=1800,
                      height=1400,
                      max_words=500,
                      random_state=1,
                      relative_scaling=0.25)
wordcloud.fit_words(top)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()