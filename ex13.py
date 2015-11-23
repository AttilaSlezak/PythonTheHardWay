__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from sys import argv

script, first, second, third, fourth = argv # Here we unpack the argv

fifth = input("I need the fifth variable: ")
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)
print("Your fifth variable is:", fifth)