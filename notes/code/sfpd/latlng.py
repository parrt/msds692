import sys
import csv

with open(sys.argv[1], 'rb') as f:
    reader = csv.reader(f, dialect='excel')
    for row in reader:
        print "{lat:%s, lng:%s}," % (row[10], row[9])
