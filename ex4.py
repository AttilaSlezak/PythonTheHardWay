__author__ = 'Slezak Attila'
cars = 100 # This defines a variable and sets its value to 100
space_in_a_car = 4.0
drivers = 30 # This assigns 30 as a value to the variable drivers
passengers = 90
cars_not_driven = cars - drivers # This creates a new variable and sets its value to the result of the substraction of cars and drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car # Here give we the result of the multiplication of cars_driven and space_in_a_car to the variable carpool_capacity
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.") # Here print we how many cars are available
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", int(carpool_capacity), "people today.") # In this printing I have converted the value of carpool_capacity to integer, because a "fraction person" wouldn't be such a kind thing, anyway...
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

print("Hey %s there." % "you") # This prints a text so that inserts the "you" part in place of %s