__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from sys import argv # Here gets "argv" the parameters as arguments what the script gets from the terminal

script, user_name = argv # Here we unpack "argv"; the first one is the name of the script and then comes the other arguments
# prompt = '> '
prompt = 'Please write your answer: '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer))
