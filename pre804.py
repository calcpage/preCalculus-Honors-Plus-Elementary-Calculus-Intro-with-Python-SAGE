#1) find the area of the SSS triangle:
#1) a=6, b=8, c=10
var('a,b,c')
a=6
b=8
c=10
show(a^2+b^2==c^2)
show((1/2)*a*b)
#2) find the area of the SSS triangle:
#2) a=4, b=5, c=7
a=4
b=5
c=7
show(a^2+b^2==c^2)
s=(a+b+c)/2
show(s)
show(sqrt(s*(s-a)*(s-b)*(s-c)))
show((sqrt(s*(s-a)*(s-b)*(s-c))).n())
#3) find the area of the SAS triangle:
#3) a=8, b=6, C=30
var('C')
a=8
b=6
C=30
show((1/2)*a*b*sin(C*pi/180))