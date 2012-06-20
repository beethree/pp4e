# learn python the hard way : exercise 14
from sys import argv

script, first_name, last_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (first_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % first_name
likes = raw_input(prompt)

print "Where do you live %s?" % first_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

full_name = first_name + ' ' + last_name
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Do you sign your name %s ?
""" % (likes, lives, computer, full_name)
