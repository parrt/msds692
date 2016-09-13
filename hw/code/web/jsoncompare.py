import json
import sys

f1 = sys.argv[1]
f2 = sys.argv[2]

json1 = json.loads(open(f1).read())
json2 = json.loads(open(f2).read())

if json1 != json2:
    sys.stderr.write("%s and %s differ\n" % (f1,f2))
else:
    print "%s and %s same" % (f1, f2)
