__author__ = 'Slezak Attila'
# -- coding: utf-8 --

x = "There are %d types of people." % 10 # We create a variable "x" and give it a string with a specialized string format sequence.
binary = "binary" # It's too simple to describe it
do_not = "don't" # Ok, it assign "don't" to the variable "do_not"
y = "Those who know %s and those who %s." % (binary, do_not) # Now we assign a string to "y" and it contents two string format

print(x) # we print the value of the variable "x"
print(y)

print("I said: %r." % x) # we print "I said: " and then the value of the variable "x"
print("I also said: '%s'." % y)

hilarious = False # We define a variable of type of bool and assign the value "False" to it
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) # Here we concatenat two different string with the character "+"