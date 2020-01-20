#!/usr/bin/python
#MrG 2016.0624 Pythonic Calculus Executive Summary!
from math import sqrt,pi
from turtle import *

#1) define a function, ie f(x)=x**2-2
def f(x):
    return x**2-2
print "f(sqrt(2)) = ", f(sqrt(2))

#2) find the numerical derivative as a limit
def diff(x,h):
    return (f(x+h)-f(x))/h

print 
print "f'(2) = "
for x in range(5):
    print diff(2,10**-x)

#3) find roots using newton's method as a limit
def root(g):
    return g-f(g)/diff(g,10**-6)

print 
print "the closest root of f(x)==0 near x=1 is:"
g=1
for x in range(5):
    print g
    g=root(g)

#4) find the definite integral as a limit
print
print "the definite integral of f(x) from 0 to pi ="
a=float(0)
b=pi
for x in range(5):
    n=10**x
    h=(b-a)/n
    l=sum([f(a+i*h)*h for i in range(n)])
    r=l-f(a)*h+f(b)*h
    print (l+r)/2
    
#5) plots using turtle.py package from idle
#5) f(x)=x**2-2 ==> f(1)==-1
#5) f'(x)=2*x ==> f'(1)==2
#5) tangent line to f(x) at x=1 is:
#5) y-y1==m*(x-x1) ==> y-f(x1)==f'(x1)*(x-x1)
#5) y+1==2*(x-1) ==> y+1==2*x-2 ==> y=2*x-3
def g(x):
    return 2*x-3

def plot(size):
    #canvas
    setworldcoordinates(-size,-size,size,size)
    #hide turtle
    ht()
    # x-axis
    pu()
    color("green")
    setpos(-size,0)
    pd()
    fd(2*size)
    # y-axis
    pu()
    color("green")
    setpos(0,-size)
    rt(270)
    pd()
    fd(2*size)
    # plot f(x)
    pu()
    color("red")
    setpos(-size,f(-size))
    pd()
    x=-size
    while x <= size:
        x+=0.1
        goto(x,f(x))
    # plot g(x)
    pu()
    color("blue")
    setpos(-size,g(-size))
    pd()
    x=-size
    while x <= size:
        x+=0.1
        goto(x,g(x))
    #delay
    mainloop()

plot(3)