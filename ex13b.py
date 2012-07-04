# learn python the hard way : exercise 13
from sys import argv

script, first = argv

print "The script is called:", script
print "You like:", first

likes = raw_input("Is there anything else you like? ")

print "So, this script is called %r, you like %r, and you also like %r ." % (script, first, likes)
