from sys import argv
script, filename = argv
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

print "Please type the filename again:"
# file_again = raw_input("> ")
# txt_again = open(file_again)
txt_again = open(raw_input("> "))
print txt_again.read()
txt_again.close()
