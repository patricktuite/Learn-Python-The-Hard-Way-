name = 'Zed A. Shaw'
age = 35 # not a lie
height_inches = 74 # inches 
weight_pounds = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_centimeters = height_inches * 2.54
weight_metric = weight_pounds * 0.453592

print "Let's talk about %s." % name
print "He's %d inches tall." % height_inches 
print "He's %d pounds heavy." % weight_pounds
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair. " % (eyes, hair)
print "His teeth are usuall %s depending on the coffee." % teeth 

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height_inches, weight_pounds, age + height_inches + weight_pounds)
print height_centimeters
print weight_metric