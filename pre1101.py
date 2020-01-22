#MRG 2014.0923 find POI: 2*x+y==5, -4*x+6*y==12
var('y')
show(solve([2*x+y==5, -4*x+6*y==12],x,y))
plot([-2*x+5,2*x/3+2],0,2)