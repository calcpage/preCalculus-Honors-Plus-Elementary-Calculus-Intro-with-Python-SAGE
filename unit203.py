#MrG 2018.0907 UNIT 203: Definition Of The Derivative
show("#1a) what's the slope of the tangent line at t=1sec? [h]=ft of ball off the ground")
h(t)=1024-16*t^2 
show(h(t)) 
show((h(1)-h(8))/(1-8)) 
show((h(1)-h(7))/(1-7)) 
show((h(1)-h(6))/(1-6)) 
show((h(1)-h(5))/(1-5)) 
show((h(1)-h(4))/(1-4)) 
show((h(1)-h(3))/(1-3)) 
show((h(1)-h(2))/(1-3)) 
plot(h(t),0,8)
show("")

show("#1b) apply definition of f'(x) to f(x)=1024-16*x^2")
f(x)=1024-16*x^2 
var('h') 
show(f(x+h)) 
show(expand(f(x+h)-f(x))) 
show(((expand(f(x+h)-f(x)))/h).simplify_rational()) 
show(lim((f(x+h)-f(x))/h,h=0))
show("")

show("#2) apply definition of f'(x) to f(x)=x^2")
f(x)=x^2 
var('h') 
show(expand(f(x+h))) 
show(expand(f(x+h)-f(x))) 
show(((expand(f(x+h)-f(x)))/h).simplify_rational()) 
show(lim((f(x+h)-f(x))/h,h=0)) 
show("")

show("#3) apply definition of f'(x) to f(x)=x^3")
f(x)=x^3 
var('h') 
show(expand(f(x+h))) 
show(expand(f(x+h)-f(x))) 
show(((expand(f(x+h)-f(x)))/h).simplify_rational()) 
show(lim((f(x+h)-f(x))/h,h=0)) 