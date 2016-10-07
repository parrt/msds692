import sys

from csvcols import get_columns

categories = get_columns(sys.argv[1],col=1)
descriptions = get_columns(sys.argv[1],col=2)

for c, n in categories.most_common(len(categories)):
    print "%6d %s" % (n, c)

for d, n in descriptions.most_common(len(descriptions)):
    print "%6d %s" % (n, d)
