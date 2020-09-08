#!/bin/python

import math
import os
import random
import re
import sys

def consumer():
    while True:
        x = yield
        print(x)

def producer(n):
    for x in range(1,n+1):
        print  "generating", x
        yield x


# Complete the 'rooter', 'squarer', and 'accumulator' function below.

def squarer():
    # Write your code here
    while True:
        x = yield
        print "squarer", x
        yield x*x

def accumulator():
    # Write your code here
    prev = 0
    while True:
        x = yield
        print "accumulator", x
        prev +=x
        yield prev

def pipeline(prod,cons):
    for num in prod:
        print "1111111111", num, square
        num = square.send(num)
        print "2222222222", num, accumulate
        num = accumulate.send(num)
        print "3333333333", num
        cons.send(num)
    cons.close()
    accumulate.close()
    square.close()


if __name__ == '__main__':
    prod = producer(3)

    cons = consumer()
    next(cons)
    
    accumulate = accumulator()
    next(accumulate)

    square = squarer()
    next(square)

    pipeline(prod, cons)

