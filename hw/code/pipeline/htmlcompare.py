import sys
from bs4 import BeautifulSoup

f1 = sys.argv[1]
f2 = sys.argv[2]

s1 = open(f1).read()
s2 = open(f2).read()

soup1 = BeautifulSoup(s1, 'html.parser')
soup2 = BeautifulSoup(s2, 'html.parser')

s1 = soup1.prettify()
s2 = soup2.prettify()

if s1 != s2:
    sys.stderr.write("%s and %s differ\n" % (f1,f2))
else:
    print("%s and %s same" % (f1, f2))
