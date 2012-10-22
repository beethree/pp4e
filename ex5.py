my_name = 'bill'
my_age = 42  # not a lie
my_height = 71.5  # inches
my_weight = 200  # lbs
my_eyes = 'hazel'
my_teeth = 'white'
my_hair = 'brown'

print "Let's talk about %s." % my_name
print "He's %f inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are ususally %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
        my_age, my_height, my_weight, my_age + my_height + my_weight)
