def numberfiller(start,stop, incr):
	numbers = []
	while start < stop:
#		print "At the top start is %d" % start
		numbers.append(start)
#		print "Numbers now:", numbers
		start = start + incr
#		print "At the bottom start is %d" % start
	return numbers

def numberfiller2(start,stop, incr):
	numbers = []
	numbers.append(start)
	for i in range (start, stop, incr):
		numbers.append(i+incr)
	numbers.pop()
	return numbers

print numberfiller(5, 10, 1)
print numberfiller(0, 200, 20)

'''
print "The numbers: "
for num in numbers:
	print num
'''

print "Alternative method 1:"
print numberfiller2(5, 10, 1)
print numberfiller2(0, 200, 20)

print "Alternative method 2:"
print range(5, 10, 1)
print range(0, 200, 20)

