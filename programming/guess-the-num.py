#!/usr/bin/python3

import random


def number():
    num = random.randint(1,100)  
    while True:
        user = int(input("Guess the random number: "))
        
        if user == num:
            print("Your guess is correct!")
            break
        elif user < num:
            print("The guess is too low")
        else:
            print("Your guess is too high")

number()