from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file %r" % filename
print txt.read()

print "Type filename again"
file_again = raw_input("file: ")

txt_again = open(file_again)

print txt_again.read()
txt.close()
txt_again.close()
