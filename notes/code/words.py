import sys
from collections import Counter

f = open(sys.argv[1])
text = f.read()
words = text.split(' ')
print words[0:100]
print Counter(words)
f.close()
