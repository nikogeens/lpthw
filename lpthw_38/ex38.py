 
ten_things = "Apples, Oranges, Crow, Telephone, Light, Sugar"
print "Wait, there's not 10 things in that list, let's fix that."

stuff = ten_things.split(', ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: %r" % next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # count from the last
print stuff.pop()
print ' '.join(stuff) # join the list in a string, concatenated by ' '
print '#'.join(stuff[3:5]) # join item 3 to 5 with a '#'

print stuff

