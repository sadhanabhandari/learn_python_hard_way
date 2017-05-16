from sys import argv

script,filename1,filename2=argv
#Create a new variable to use the open function to open the existing file
txt = open(filename1)

print "Here's your file %r:" % filename2
#use the read function to read the text in the txt variable
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again=open(file_again)

print txt_again.read()


