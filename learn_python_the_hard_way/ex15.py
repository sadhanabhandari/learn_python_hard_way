from sys import argv

script,filename=argv
#Create a new variable to use the open function to open the existing file
txt = open(filename)

print "Here's your file %r:" %filename
#use the read function to read the text in the txt variable
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again=open(file_again)

print txt_again.read()


