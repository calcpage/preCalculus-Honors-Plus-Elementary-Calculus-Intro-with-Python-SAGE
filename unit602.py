#MrG 2015.1118 Disk Method!
#1) Find the volume formed when the region bound by y=2*x-x^2 and the x-axis in QI is revolved about the x-axis
f(x)=2*x-x^2
show(plot(f(x),0,2))
show(solve(f(x)==0,x))
show(expand(f(x)^2))
show(integrate(f(x)^2,x))
show(pi*integrate(f(x)^2,x,0,2))
#2) Find the volume formed when the region bound by y=1/x^2 and the y-axis in QI is revolved about the y-axis for 1<=y<=4
var('y')
f(x)=1/x^2
show(plot(f(x)),xmin=0,xmax=1,ymin=0,ymax=4,aspect_ratio=1)
show(solve(y==f(x),x))
show(integrate(1/y,y))
show(pi*integrate(1/y,y,1,4))