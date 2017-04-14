print "This is a Pyg Latin: Which means a reverted name of a character"

name = raw_input("What is your name? ")
if name.isalnum() or name.isspace() or len(name)>0 :
    new_name = name[::-1]
    print new_name
else:
    print "Please enter alphabets"
