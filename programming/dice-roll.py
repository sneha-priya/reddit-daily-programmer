#!/usr/bin/pyhton3

import random

def game():
    str(input("Press enter to roll!"))

def roll():
    num = random.randint(1,6)
    print("The die value is {0}".format(num))
    print("Would you like to roll the dice again? ")
    choice = str(input("Type 'Y' if you want to roll again else 'N': "))
    if choice == "Y":
        print("The die value is", random.randint(1,6))
    else:
        print("Quit")

game()
roll()
