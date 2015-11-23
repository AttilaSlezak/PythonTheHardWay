__author__ = 'Slezak Attila'
# -- coding: utf-8 --
def cheese_and_crackers(cheese_count, boxes_of_crackers): # Here we define a function which has two arguments
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

def my_function_print_anything(*args):
    numbers_sum = 0
    for i in range(len(args)):
        print(args[i])
        if type(args[i]) is int:
            numbers_sum += args[i]
    print("Integer arguments sum is: ", numbers_sum)
    return "Process succesfully finished"

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # Here we call the function with a variable and a math expression

print(my_function_print_anything("valami", 22, "más_valami", 41))
print(my_function_print_anything(["Most itt van valami.", 33], 44, 235, ("Hihi", 33)))