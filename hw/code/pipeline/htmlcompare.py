import sys

f1 = sys.argv[1]
f2 = sys.argv[2]

s1 = open(f1).read()
s2 = open(f2).read()

s1 = s1.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')
s2 = s2.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r', '')

if s1 != s2:
    sys.stderr.write("%s and %s differ\n" % (f1,f2))
else:
    print "%s and %s same" % (f1, f2)
