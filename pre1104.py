#1) Find the POI: 3*x-2*y==4, 6*x+y==13
a=matrix([(4,-2),(13,1)]);show(a)
b=matrix([(3,4),(6,13)]);show(b)
c=matrix([(3,-2),(6,1)]);show(c)
dA=det(a);show(dA)
dB=det(b);show(dB)
dC=det(c);show(dC)
x=dA/dC;show(x)
y=dB/dC;show(y)