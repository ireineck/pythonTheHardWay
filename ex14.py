# Propting And Passing

from sys import argv

script, user_name = argv
prompt = '> '
print "Hi %s, I'm the %s script." % (user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?" 
computer = raw_input(prompt)

is_mac = " "

if computer.upper() == "MAC":
	is_mac = "Awesome! me too"
else:
	is_mac = "nice"

print """
Alright so you said %r about liking me. 
YOu live in %r.  Not sure where that is.
And you have a %r computer. %s.
""" % (likes, lives, computer, is_mac)



