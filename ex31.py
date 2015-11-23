__author__ = 'Slezak Attila'
# -- coding: utf-8 --
prompt = "> "

print("You enter a dark room with two doors. Do you go through door #1 or door 2#?")

door = input(prompt)

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(prompt)

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)
        print("The cake is there. What do you do?")
        print("1. Eat the cake.")
        print("2. Looking around.")
        cake = input(prompt)

        if cake == "1":
            print("The cake was poisoned, so your body suddenly burnt in a big fire. Good job!")
        elif cake == "2":
            print("While you are looking around, suddenly the bear came back with another bears "
                  "and eat your whole body. Good job!")
        else:
            print("%s is the best! You are runaway from the death!" % cake)

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(prompt)

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")