
#Escape Sequences

# puts a tab on the display
tabby_cat="\tI'm tabbed in."
# puts the text after the \n in a brand new line
persian_cat="I'm split\non a line."
#puts a backslash in between each word of the text
backlash_cat="I'm \\ a \\ cat."

#using \t* puts a list using a tab
fat_cat= """
I'll do a list:
\t* Cat food
\t* Finishes
\t* Catnip\n\t* Grass 
"""
#prints all the varibles discribed above
print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

#while True:
   # for i in ["/","-","|","\\","||"]:
        #print "%s\r" % i,
#puts a backslash between words in the string
print "hi\\how\\are\\you\\doing?"
#escape sequence to make clear to python that it needs to omit the single quotes that is coming up
print "Punj\' wife?"

dinner="""
dishes:
\t* Biryani
\t* Momo
\t* Pizza
\t* Fries
"""

print dinner
