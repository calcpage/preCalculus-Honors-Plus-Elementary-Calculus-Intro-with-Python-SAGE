#MrG 2015.1118 Arc Length
#Find the length of the path f(x)=4*sqrt(2)/3*x^(3/2)-1 for 0<=x<=1
f(x)=4*sqrt(2)/3*x^(3/2)-1
show(plot(f(x),0,1))
g(x)=diff(f(x),x)
show(g(x))
show(g(x)^2)
show(g(x)^2+1)
show((sqrt(g(x)^2+1)))
show(integrate(sqrt(g(x)^2+1),x))
show(integrate(sqrt(g(x)^2+1),x,0,1))
show(integrate(sqrt(g(x)^2+1),x,0,1).n())