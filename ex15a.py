# learn python the hard way : exercise 15a
# The line below imports the sys module to get command line args
#from sys import argv

# The line below defines two variables passed via argv
#script, filename = argv

# The line below defines a variable and issues a command
#txt = open(filename)

#print "Here's your file %r:" % filename
#print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.readline()
txt_again.close()
