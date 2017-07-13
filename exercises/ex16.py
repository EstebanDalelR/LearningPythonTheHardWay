from sys import argv

script, filename = argv

print "We will erase %r" % filename
print "To cancel use CTRL+C"
print "To continue press ENTER"

raw_input("Continue?")

print "Opening %r" % filename
target = open(filename, "w")

print "bye file"
target.truncate()

print "Now we create a new text"
target.write(raw_input("first line: "))
target.write("\n")
target.write(raw_input("second line: "))
target.write("\n")

print "And now we close it"
target.close()
