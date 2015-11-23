__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from sys import argv

script, filename = argv # We make the unpack of argv here.

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).") # CTRL-C really terminates the whole procedure
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # Here open we the file for writing

print("Truncating the file. Goodbye!")
target.truncate() # Here erase we the whole content of the file

print("Now I'm going to ask you for three lines.")
# In these lines we just ask the user for data, and put them in simple variables:
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# In this/(these) lines we write the data asked the user for before in the file:
target.write("%s \n%s \n%s \n" % (line1, line2, line3))
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close() # We close the file which is a very important procedure whenever we have a file opened before.