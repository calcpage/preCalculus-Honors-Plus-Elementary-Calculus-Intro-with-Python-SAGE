#1) Graph y^2==12*x
var('y')
show(solve(y^2==12*x,y))
show(plot([-2*sqrt(3*x),2*sqrt(3*x)],0,3,aspect_ratio=1))
#2) Graph x^2==-12*y
show(solve(x^2==-12*y,y))
show(plot(-x^2/12,-6,6,aspect_ratio=1))
#3) Graph (y-3)^2==8*(x+3)
show(solve((y-3)^2==8*(x+3),y))
show(plot([-2*sqrt(2*x+6)+3,2*sqrt(2*x+6)+3],-3,1,aspect_ratio=1))
#4) Graph x^2+4*x-4*y==0
show(solve(x^2+4*x-4*y==0,y))
show(plot(x^2/4+x,-4,0,aspect_ratio=1))