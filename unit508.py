#MrG 2015.1112 FTC
#1) FTCI: Why does integrate(5,x,1,4)=15?
show(integrate(5,x,1,4))
show(plot(5,1,4))
#2) FTCI: Why does integrate(sqrt(4-x^2),x,-2,2)=2*pi?
show(integrate(sqrt(4-x^2),x,-2,2))
show(plot(sqrt(4-x^2),-2,2))
#3) FTCII: Given f(x)=integrate(t^2,t,0,x), what is f'(x)?
var('t')
f(x)=integrate(t^2,t,0,x)
g(x)=diff(f(x),x)
show(f(x))
show(g(x))
#4) FTCII: Given f(x)=integrate(cos(t),t,-pi,x), what is f'(x)?
f(x)=integrate(cos(t),t,-pi,x)
g(x)=diff(f(x),x)
show(f(x))
show(g(x))
#5) FTCII + Chain Rule: Given f(x)=integrate(cos(t),t,-pi,x^2), what is f'(x)?
f(x)=integrate(cos(t),t,-pi,x^2)
g(x)=diff(f(x),x)
show(f(x))
show(g(x))