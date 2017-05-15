age = raw_input("How old are you?")
height=raw_input("How tall are you?")
weight=raw_input("How much do you weigh?")

print "So, you're %r old, %r tall and %r heavy."%(age,height,weight)


# %r is used for debugging and is a "raw representation" It uses the repr function.. A __repr__ goal is to be unambiguous
# %s is used for display... It uses str function.. A __str__goal is to be readable 