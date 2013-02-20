print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t This magic moment
so different and so new
was like any other
untill I kissed you
\n\t And then it happened
It took me by suprise
I knew that you felt it too
by the look in your eyes
"""
print "-" * 10
print poem
print "-" * 10

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 5000
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 1000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

print "We could also do it like this:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

print "Good job!"
