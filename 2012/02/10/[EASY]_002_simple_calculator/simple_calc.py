#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    args = [int(x) for x in sys.argv[1:]]


    print("sum of {}: {}".format(sys.argv[1:], sum(args)))


