animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

def checker(cardinal,list):
	print "The %dst animal is a %s and it is at %d" % (cardinal+1, list[cardinal], cardinal)
	print "The animal at %d is the %dst animal and is a %s." % (cardinal, cardinal+1, list[cardinal])

checker(0,animals)
checker(2,animals)
checker(0,animals)
checker(3,animals)
checker(4,animals)
checker(2,animals)
checker(5,animals)
checker(4,animals)
