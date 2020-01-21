#!/usr/bin/python
#MrG 2016.0623 2016BC2
#2a) x(3)=14.377, y(3)=-0.5
from math import sin, sqrt

def f(t):
    return t**2+sin(3*t**2)

print "x(3) = "
a=float(0)
b=float(3)
for x in range(5):
    n=10**x
    h=(b-a)/n
    l=sum([f(a+i*h)*h for i in range(n)])
    r=l-f(a)*h+f(b)*h
    print 5+(l+r)/2

#2b) dy/dx=0.050 when t=3
print
print "dy/dx when t is 3 = ", 0.5/f(3)

#2c) abs(v(3))=9.969
print
print "abs(v(3)) = ", sqrt(f(3)**2+0.5**2)

#2d) l=4.350
def g(t):
    return sqrt(f(t)**2+4)

print
print "l1 = "
a=float(0)
b=float(1)
for x in range(5):
    n=10**x
    h=(b-a)/n
    l=sum([g(a+i*h)*h for i in range(n)])
    r=l-g(a)*h+g(b)*h
    l1=(l+r)/2
    print l1

def g(t):
    return sqrt(f(t)**2)

print
print "l2 = "
a=float(1)
b=float(2)
for x in range(5):
    n=10**x
    h=(b-a)/n
    l=sum([g(a+i*h)*h for i in range(n)])
    r=l-g(a)*h+g(b)*h
    l2=(l+r)/2
    print l2
    
print
print "l1+l2 = ", l1+l2
