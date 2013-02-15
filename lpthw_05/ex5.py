name = "Samson"
age = 8
height = 54  # cm
weight_kg = 36  # kg
weight_pound = weight_kg * 0.453592
eyes = "deep brown"
teeth = "sharp as knives"
hair = "long and white, with some dark strokes"

print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d kg heavy.  That's %d in pounds" % (weight_kg, weight_pound)
print "Actually, that's not too heavy."
print "He's got %s eyes and his hair is %s." % (eyes, hair)
print "His teeth are usually %s." % teeth

# print all variables with the %r formatter
print "%r %r %r %r %r %r %r" % (name, age, height, weight_kg, eyes, teeth, hair)
