__author__ = 'Slezak Attila'
# -- coding: utf-8 --
from sys import argv

script, filename = argv

txt = open(filename) # We open a file here

print("Here's your file %r:" % filename)
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again) # We open a file (what's more, the same file) again!

print(txt_again.read())
txt_again.close()