import sys
import csv
import re

# python csvfilter.py filename -cat=
filename = sys.argv[1]
args = sys.argv[2:]
catfilter = descfilter = datefilter = None
for arg in args:
    if arg.startswith("-cat="):
        catfilter = arg[5:]
    elif arg.startswith("-desc="):
        descfilter = arg[6:]
    elif arg.startswith("-date="):
        datefilter = arg[6:]

catmatches = []
descmatches = []
datematches = []

with open(filename, 'rb') as f:
    reader = csv.reader(f, dialect='excel')
    headers = reader.next()
    i = 0
    for row in reader:
        cat = row[1]
        desc = row[2]
        date = row[4]
        if catfilter and re.search(catfilter, cat):
            catmatches.append(i)
        if descfilter and re.search(descfilter, desc):
            descmatches.append(i)
        if datefilter and re.search(datefilter, date):
            datematches.append(i)
        i += 1

matches=None
if catfilter:
    matches = set(catmatches)
if descfilter:
    matches = matches.intersection(descmatches) if matches else set(descmatches)
if datefilter:
    matches = matches.intersection(datematches) if matches else set(datematches)

with open(filename, 'rb') as f:
    reader = csv.reader(f, dialect='excel')
    headers = reader.next()
    i = 0
    for row in reader:
        if i in matches:
            print row
        i += 1