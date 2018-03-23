#!/usr/bin/python3

#program to get a multiplication table

num = int(input("Enter a number: "))

for i in range(1,11):
    print(num ,'x' , i , '=' ,num*i)