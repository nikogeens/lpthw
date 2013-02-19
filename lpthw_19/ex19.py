def cheese_and_crackers(cheese_count, boxes_of_crackers):
	cheese_count = int(cheese_count)
	boxes_of_crackers = int(boxes_of_crackers)
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket.\n"

print "Give numbers directly:"
cheese_and_crackers(raw_input("How many cheeses? "),raw_input("How many crackers? "))

print "Now we use variables."
amount_of_cheese = 10
amount_of_crackers = 30
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#print "Now try to input math:"
#cheese_and_crackers(raw_input("How many cheeses? "),raw_input("How many crackers? "))

print "Let's combine math and variables."
cheese_and_crackers(amount_of_cheese + 20,amount_of_cheese + 50)
