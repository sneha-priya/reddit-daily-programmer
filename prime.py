#!/usr/bin/python3

#program to check prime number

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("{0} is not a prime number".format(num))
            break
    else:
        print("{} is a prime number".format(num))
else:
    print("{} not a prime number".format(num))