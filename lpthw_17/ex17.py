from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "We will be copying from %r to %r" % (from_file, to_file)

# we can do this in one line?
# in_file = open(from_file)
# in_data = in_file.read()

# yes, we can!
in_data = open(from_file).read()

print "The input is %d bytes long" % len(in_data)

print "Does the outputfile exists? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("What's it gonna be boy? ")

out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alrighty, that went smooth :-)"

out_file.close()
# since we didn't use in_file, we don't have to close it
# in_file.close()
