#!/usr/bin/python
#MrG 2016.0621 2016AB1BC1
#1c) 49786 l
import math
f="2000*math.exp(-x**2/20)"
a=float(0)
b=float(8)
n=10

def lSum(f,a,b,n):
    h=(b-a)/n
    return sum([f(a+i*h)*h for i in range(n)])

def rSum(f,a,b,n):
    h=(b-a)/n
    return sum([f(a+i*h)*h for i in range(n)])-f(a)*h+f(b)*h

print "l\t\tr\t\tt"
for j in range(4):
    n=10**j
    l=50000-8050+lSum(lambda x: eval(f),a,b,n)
    r=50000-8050+rSum(lambda x: eval(f),a,b,n)
    print l,"\t",r,"\t",(r+l)/2