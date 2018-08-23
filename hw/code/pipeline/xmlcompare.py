import sys
import xmltodict

f1 = sys.argv[1]
f2 = sys.argv[2]

xml1 = xmltodict.parse(open(f1).read())
xml2 = xmltodict.parse(open(f2).read())

if xml1 != xml2:
    sys.stderr.write("%s and %s differ\n" % (f1,f2))
else:
    print("%s and %s same" % (f1, f2))
