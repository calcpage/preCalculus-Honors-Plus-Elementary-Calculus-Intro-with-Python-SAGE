#!/usr/bin/python
#MrG 2016.0621 2016AB2
#2c) x(0)=-3.815
import math
def f(t):
    return 1+2*math.sin(t**2/2)

a=float(0)
b=float(4)
for x in range(5):
    h=(b-a)/10**x
    l=sum([f(a+i*h)*h for i in range(10**x)])
    r=l-f(a)*h+f(b)*h
    print 2-(l+r)/2
