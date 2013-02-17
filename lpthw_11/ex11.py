"""
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
"""

print "Hoogte in cm?", 
hoogte = float(raw_input())
print "Gewicht in kg?", 
gewicht = float(raw_input())

bmi = gewicht / (hoogte * hoogte) * 10000

print "Uw bmi is %r" % bmi

