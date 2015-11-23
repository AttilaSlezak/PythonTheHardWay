__author__ = 'Slezak Attila'
# -- coding: utf-8 --
# a karakterkódos sor a fenti módon is működik, meg az ex2.py-ben található módon is.

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %r." % name)
print("He's %r inches (%d centimeters) tall." % (height, height * 2.54))
print("He's %r pounds (%d kilos) heavy" % (weight, weight * 0.4535))
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes.lower(), hair))
print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right éá
print("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))

print("1.733 rounded is", round(1.733))