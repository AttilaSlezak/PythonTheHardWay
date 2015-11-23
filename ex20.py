__author__ = 'Slezak Attila'
# -- coding: utf-8 --

from sys import argv

script, input_file = argv # Here we unpack the arguments

def print_all(f):
    # print(type(f))
    print(f.read()) # Here we print the whole content of the file

def rewind(f):
    f.seek(0) # Here we jump to the beginning of the file

def print_a_line(line_count, f):
    print(line_count, f.readline()) # Here we print out only one line

current_file = open(input_file) # We open the file for reading here

print("First let's print the whole file:\n")

print_all(current_file) # Here we call the function print_all and give it the parameter current_file

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1 # value = 1
print_a_line(current_line, current_file)

current_line = current_line + 1 # value = 2
print_a_line(current_line, current_file)

current_line += 1 # value = 3
print_a_line(current_line, current_file)