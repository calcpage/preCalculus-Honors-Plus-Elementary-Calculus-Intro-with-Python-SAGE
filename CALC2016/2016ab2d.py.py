#!/usr/bin/python
#MrG 2016.0621 2016AB2
#2d) d=5.301
import math
def f(t):
    return 1+2*math.sin(t**2/2)

a=float(0)
b=2.7074679792
for x in range(4):
    h=(b-a)/10**x
    l=sum([f(a+i*h)*h for i in range(10**x)])
    r=l-f(a)*h+f(b)*h
    d1=(l+r)/2
    print d1
    
a=2.7074679792
b=float(3)
for x in range(4):
    h=(b-a)/10**x
    l=sum([f(a+i*h)*h for i in range(10**x)])
    r=l-f(a)*h+f(b)*h
    d2=(l+r)/2
    print d2
    
print "ans=", d1-d2