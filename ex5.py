#more python variable practice and string formatting 

my_name = "Ian Reineck"
my_age = 33 #not a lie
my_height = 74 #inches 
my_weight = 230 #lbs
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print "Let's talk about %s" % my_name # %s -> strings
print "He's %d inches tall" % my_height #%d -> deciaml/float?
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
