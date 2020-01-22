#MrG 2015.1118 Arc length and Surface Area
#91BC4: Let f(x)=integrate(sqrt(t^2+t),t,0,2*x). Find the arc length along F(x) from x=1 to x=2
g(x)=2*sqrt(4*x^2+2*x)
show(g(x))
show(g(x)^2)
show(1+g(x)^2)
show(sqrt(1+g(x)^2))
show(integrate(sqrt(1+g(x)^2),x))
show(integrate(sqrt(1+g(x)^2),x,1,2))
#2) Let f(x)=1/e^x, find the length of the curve for x=0 to x=100
f(x)=1/e^(x)
g(x)=diff(f(x),x)
show(g(x))
show(g(x)^2)
show(1+g(x)^2)
show(sqrt(1+g(x)^2))
show((integrate(sqrt(1+g(x)^2),x,0,1)).n())
show((integrate(sqrt(1+g(x)^2),x,0,10)).n())
show((integrate(sqrt(1+g(x)^2),x,0,100)).n())
#2) Let f(x)=1/e^x, find the surface are formed by revolving the curve about the x-axis for x=0 to x=100
show((2*pi*integrate(f(x)*sqrt(1+g(x)^2),x,0,1)).n())
show((2*pi*integrate(f(x)*sqrt(1+g(x)^2),x,0,10)).n())
show((2*pi*integrate(f(x)*sqrt(1+g(x)^2),x,0,100)).n())

