#MrG 2015.0414 UNIT302: Quotient and Product Rules
show("#1) find the derivative of f(x)=(x^2-1)/(x^2+1)")
f(x)=(x^2-1)/(x^2+1)
show(diff(f(x),x).simplify_rational())
p1=plot(f(x),color='red')
p2=plot(diff(f(x),x),color='green')
show(p1+p2)
show("")

show("#2) find the derivative of f(x)=(x^2+1)*(x^3+3)")
f(x)=(x^2+1)*(x^3+3)
show(diff(f(x),x).expand())
p1=plot(f(x),color='red')
p2=plot(diff(f(x),x),color='green')
show(p1+p2)
show("")

show("#3) find the derivative of f(x)=sin(x)/cos(x)")
f(x)=sin(x)/cos(x)
show(diff(f(x),x).simplify_trig())
p1=plot(f(x),color='red')
p2=plot(diff(f(x),x),color='green')
p1+p2