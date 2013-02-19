def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

print "Let's do some math with functions"

age = add(30, 6)
height = subtract(200,20)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %r, height: %r, weight: %r, iq: %r" % (age, height, weight, iq)

print "Here is the puzzle outcome"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print " That becomes: ", what, "Can you do it by hand?"

print divide(add(24, 34),subtract(100, 1023))

print subtract(add(24, divide (34, 100)), 1023)
