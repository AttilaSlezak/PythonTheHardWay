__author__ = 'Slezak Attila'
# -- coding: utf-8 --
from sys import exit
from datetime import datetime, timedelta
from sys import argv
from ex36_ex35modul import Password

if len(argv) == 2 and argv[1] == 'key':
    key_to_gold_room = True
    print("You have activated your magic key!")
else:
    key_to_gold_room = False

print(datetime.now().date())
prompt = "> "

def gold_room():
    print("This room is full of gold. How much do you take?")

    next = input(prompt)
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def date_checker(get_date):
    current_time = datetime.strptime("2014-01-01", "%Y-%m-%d")
    try:
        current_time = datetime.strptime(get_date, "%Y-%m-%d")
        return current_time
    except ValueError as valerr:
        return current_time

def password_to_the_door():
    door_password = Password.send_back_the_password('valami')
    bear_angry = False
    while True:
        next = input((prompt))
        if next.lower() == door_password.lower() or next.lower() == door_password.lower()[0:len(door_password)-1]:
            print("'Congratulations! The answer is correct!' - said the door.")
            print("The door opened and you could go in.")
            gold_room()
        elif "key" in next and key_to_gold_room:
            print("You put your magic key into the keyhole and the door opened.")
            gold_room()
        elif "key" in next and not key_to_gold_room:
            print("You don't have the magic key to this door!")
            print("So, you have to answer the question of the door.")
        elif "ask the bear" in next and not bear_angry:
            print("The bear got angry:")
            print("'Do you know anything, at all??? You should know it!")
            print("Don't ask me again if you value your life!!!' - shouted the bear.")
            bear_angry = True
        elif "bear" in next and bear_angry:
            dead("The bear gets pissed off and took your head off.")
        elif "let" in next.lower():
            print("The answer is not complete.")
        else:
            print("The answer is incorrect.")

def door_opening():
    print("You stepped to the door. Then suddenly the door began to speak:")
    print("'I need to know the current date!' - said the door.")
    print("Please add the current date in format: YYYY-MM-DD")

    while True:
        next = input(prompt)
        current_time = date_checker(next)
        yesterday = datetime.now()-timedelta(days=1)
        yesterday = yesterday.date()

        if current_time.date() == datetime.now().date():
            print("'The answer is correct. But I need the password, too.' said the door.")
            password_to_the_door()
        elif "key" in next and key_to_gold_room:
            print("You put your magic key into the keyhole and the door opened.")
            gold_room()
        elif "key" in next and not key_to_gold_room:
            print("You don't have the magic key to this door!")
            print("So, you have to answer the question of the door.")
        elif next == "I ask the bear":
            print("The bear looked at the table where a yesterday's newspaper was.")
            print("'It's", yesterday, "today... ' - answered the bear and continued to eat the honey.")
        else:
            print("'This is not the correct answer.' - said the door")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input(prompt)

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
        elif next == "open door" and bear_moved:
            door_opening()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next = input(prompt)

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input(prompt)

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()