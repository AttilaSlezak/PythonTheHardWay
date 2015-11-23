__author__ = 'Slezak Attila'
# -- coding: utf-8 --

# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Dog is-a object which is some kind of Animal (inherited from Animal)
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name

# Cat is-a object which is some kind of Animal (inherited from Animal)
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name

# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# Employee is-a object which is an instance of Person (inherited from Person)
class Employee(Person):

    def __init__(self, name, salary):
        # This magic is to get the name of the Employee as a Person and his pet, too
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salamon is-a object which is some kind of Fish (inherited from Fish)
class Salamon(Fish):
    pass

# Halibut is-a object which is some kind of Fish (inherited from Fish)
class Halibut(Fish):
    pass

# rover is a Dog (which is an object of Dog class)
rover = Dog("Rover")

# satan is a Cat (which is an object of Cat class)
satan = Cat("Satan")

# mary is a Person (which is an object of Person class)
mary = Person("Mary")

# mary has a pet which is a Cat called Satan
mary.pet = satan

# frank is an Employee which means he is a Person in the same time (he is an instance of Employee which is
# a class inherited from the class Person
frank = Employee("Frank", 120000)

# frank has a pet which is a Dog called Rover
frank.pet = rover

# flipper is a fish (an object from the class Fish)
flipper = Fish()

# crouse is a Salamon (an instance of the class Salamon which is a class inherited from the class Fish)
crouse = Salamon()

# harry is a Halibut (an instance of the class Halibut which is a class inherited from the class Fish)
harry = Halibut()