import codecs

f = codecs.open('/tmp/utf8.txt', encoding='utf-8', mode='r')
s = f.read()
f.close()
print repr(s)
