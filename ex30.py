__author__ = 'Slezak Attila'
# -- coding: utf-8 --

people = 30
cars = 40
buses = 15

if cars > people > buses:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses > cars:
    print("That's too many buses.")
elif buses < cars or people == cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")

x = 7
if x in range(1,10):
    print("X between 1 and 10.")