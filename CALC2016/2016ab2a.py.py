#!/usr/bin/python
#MrG 2016.0622 2016AB2
#2a) particle is slowing down
from math import sin
from turtle import *

def f(t):
    return t**2+sin(3*t**2)
print f(4)

def diff(t,h):
    return (f(t+h)-f(t))/h

for x in range(7):
    print diff(4.0,10**-x)