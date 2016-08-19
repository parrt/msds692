import sys
import re

filename = sys.argv[1]
f = open(filename, "r")
lines = f.readlines()
f.close()

records = []
for line in lines:
    ip = re.findall('^.*? ', line)
    ip = ip[0].strip()
    # print ip
    date_brackets = re.findall('\\[.*\\]', line)
    date = date_brackets[0]
    date = date[1:len(date)-1]
    # print date
    quoted_strings = re.findall('".*?"', line)
    quoted_strings = [s[1:len(s)-1] for s in quoted_strings]
    # print quoted_strings
    records.append( [ip,date]+quoted_strings )

for r in records:
    print r
