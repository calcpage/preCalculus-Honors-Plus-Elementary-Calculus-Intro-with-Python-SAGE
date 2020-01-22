#MrG 2015.1118 Area
#81AB2: find the area bound by y=4-x^2, y=3*x and the y-axis
f(x)=4-x^2
g(x)=3*x
show(plot([f(x),g(x)],0,1,aspect_ratio=1))
show(integrate(f(x),x))
show(integrate(f(x),x,0,1))
show(integrate(f(x),x,0,1).n())
#83AB4: find the area bound by sqrt(x)+sqrt(y)=2, the x-axis and the y-axis for 0<=x<=1
f(x)=(2-sqrt(x))^2
show(expand(f(x)))
show(integrate(f(x),x))
show(integrate(f(x),x,0,1))