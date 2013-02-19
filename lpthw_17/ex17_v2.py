from sys import argv
from os.path import exists

script, from_file, to_file = argv

if exists(to_file):
    print "The target-file already exists.  Continuing will overwrite..."
    print "hit RETURN to continue, CTRL-C to abort."
    raw_input("What's it gonna be boy? ")

open(to_file, 'w').write(open(from_file).read())

print "Done."
