#!/usr/bin/python
#MrG 2016.0622 2016AB2
#2b) v(2.707)==0
import math

def f(t):
    return 1+2*math.sin(t**2/2)
print f(4)

def diff(t,h=10**-6):
    return (f(t+h)-f(t))/h

def newton(g):
    return g-f(g)/diff(g)

g=2.5
for x in range(5):
    print g
    g=newton(g)
