#!/usr/bin/python3

#program to print factorial of a number

num = int(input("Enter a  number: "))

factorial = 1

if num == 0:
    print("Factorial doesnt exists to this number.")
elif num < 0:
    print("Factorial doesnt exists to this number.")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("The factorial of a {0} is {1}".format(num,factorial))