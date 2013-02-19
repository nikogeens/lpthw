
# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that was pretty pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this one takes only one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes none
def print_none():
	print "I don't want any."

print_two("first", "second")
print_two_again("first_again", "second_again")
print_one("only one")
print_none()
