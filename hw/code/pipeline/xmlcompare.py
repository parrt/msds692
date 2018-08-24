import sys
import xmltodict

f1 = sys.argv[1]
f2 = sys.argv[2]

xml1 = xmltodict.parse(open(f1).read())
xml2 = xmltodict.parse(open(f2).read())

txt_xml1 = xmltodict.unparse(xml1, pretty=True)
txt_xml2 = xmltodict.unparse(xml2, pretty=True)

if txt_xml1 != txt_xml2:
    sys.stderr.write("%s and %s differ\n" % (f1,f2))
else:
    print("%s and %s same" % (f1, f2))
