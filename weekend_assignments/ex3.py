#Define a function that can accept two strings as input and print the string with maximum length in console.
#  If two strings have the same length, then the function should print al l strings line by line.
def max_length(first_string,second_string):
    if len(first_string)>len(second_string):
        print first_string
    elif len(first_string)==len(second_string):
        print first_string,second_string
    else:
        print second_string

max_length("appe","punj")