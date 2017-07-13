from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)

print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print """
So you said %s about liking me
and live in %s
""" % (likes, lives)
