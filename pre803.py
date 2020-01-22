#1) Solve SAS Triangle: a=2,b=3,C=60deg
var('a,b,c,C,B')
a=2
b=3
C=60*pi/180
show(solve(c^2==a^2+b^2-2*a*b*cos(C),c))
c=sqrt(7)
show((solve(b^2==a^2+c^2-2*a*c*cos(B),B)[0].rhs()*180/pi).n())
show((180-60-solve(b^2==a^2+c^2-2*a*c*cos(B),B)[0].rhs()*180/pi).n())