
name = 'Zed A. Shaw'
age  = 35 #not a lie
height =74 # inches
weight=180 #lbs
eyes ='Blue'
teeth ='White'
hair = 'Brown'

print "Let's talk about %s." %name
print "He's %d inches tall." % height
print "He's %d pounds heavy." %weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair" % (eyes,hair)
print "His teeth are usually %s depending on the coffee." %teeth

print "punj's teeth is %r"%(teeth)
#variable to convert pound to kilogram

pound_to_kilogram_converter = weight * 0.453

print pound_to_kilogram_converter




# this line is tricky, try to get it exactly right

print " If I add %d, %d, and %d I get %d." %(
    age,height,weight,age + height +weight)
