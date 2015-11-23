__author__ = 'Slezak Attila'
# -- coding: utf-8 --

def while_loop_test(max_number):
    i = 0
    numbers = []

    while i < max_number:
        print("At the top i is %d" % i)
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)

while_loop_test(7)