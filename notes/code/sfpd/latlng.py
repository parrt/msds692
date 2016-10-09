import sys
import csv

filename = sys.argv[1]
raw = False
if len(sys.argv)>2:
    if sys.argv[2]=='-raw':
        raw = True

with open(filename, 'rb') as f:
    reader = csv.reader(f, dialect='excel')
    for row in reader:
        if raw:
            print "%s %s" % (row[10], row[9])
        else:
            print "{lat:%s, lng:%s}," % (row[10], row[9])
