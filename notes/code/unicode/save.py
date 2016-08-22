import codecs

# Write an ASCII-encoded text file
f = open("/tmp/ascii.txt", "w")
f.write("Hi mom\n")
f.close()

# Write a UTF-8-encoded text file
f = codecs.open('/tmp/utf8.txt', encoding='utf-8', mode='w')
# f.write(u'Watch: \u231A, Hourglass: \u231B\n')
f.write(u'Power: \u23FB, Stop: \u23F9\n')
f.close()