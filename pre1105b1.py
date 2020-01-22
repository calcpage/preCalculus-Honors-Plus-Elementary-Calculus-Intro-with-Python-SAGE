# Find the POI: 2*x+y==8, x+y==5
a=matrix([(2,1),(1,1)]);show(a)
b=matrix(2,1,[(8),(5)]);show(b)
show(a^(-1))
show(a^(-1)*b)
var('y')
show(solve([2*x+y==8, x+y==5],x,y))
plot([8-2*x,5-x],0,4)