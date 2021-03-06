from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, press return."

raw_input("? ")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I will ask you for 3 lines."

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I will now write these lines to the file"

"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "Let's see what we have now: "
target = open(filename)
print target.read()

print "And finally, we close it. Bye."
target.close()

