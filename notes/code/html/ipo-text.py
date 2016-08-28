import sys
from bs4 import BeautifulSoup # needs: pip install beautifulsoup4
from collections import defaultdict, Counter
import re

def html2text(html_text):
    html_text = html_text.replace('&nbsp;', ' ') # replace html space specifier with space char
    soup = BeautifulSoup(html_text, 'html.parser')
    html_text = soup.get_text(' ', strip=False)  # space between tags, don't strip newlines
    return html_text

filename = sys.argv[1]
f = open(filename, "r")
html = f.read()
text = html2text(html)
f.close()

"""
If we tried to print now, we have an ASCII issue:

print text

Traceback (most recent call last):
  File "ipo-text.py", line 19, in <module>
    print text
UnicodeEncodeError: 'ascii' codec can't encode character u'\x92' in position 918: ordinal not in range(128)
"""

text = text.encode('ascii', 'ignore')
# print text

text = re.sub("[\\n ]+", ' ', text)
words = text.strip().split(' ')
print len(set(words)), "unique words"
hist = defaultdict(int)
for w in words:
    hist[w] += 1

print hist.items()

print Counter(words)