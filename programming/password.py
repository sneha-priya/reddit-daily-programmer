#!/usr/bin/python3

import random

def gen_password():
    passlen = int(input("Enter the length of the password to be generated: "))
    sample = "abcdefghijklmnopqrstuvwxyz0123456789"
    sample_length = len(sample)
    password_list = []
    for i in range(passlen):
        random_position = random.randint(0,sample_length-1)
        random_char = sample[random_position]
        password_list.append(random_char)
        password = "".join(password_list)
    print(password)
  
gen_password()


