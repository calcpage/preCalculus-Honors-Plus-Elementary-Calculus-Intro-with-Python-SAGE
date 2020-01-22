#MrG 2018.0917 UNIT301: Product Rule!
show("#1) h(x)=f(x)*g(x)=(x^2)*(x^3), find h'(x).")
f(x)=x^2
g(x)=x^3
show(diff(f(x),x))
show(diff(g(x),x))
show(diff(f(x)*g(x),x))
show(f(x)*diff(g(x),x)+g(x)*diff(f(x),x))
show("")

show("#2) h(x)=f(x)*g(x)=(x^2)*(x^3), find h'(x).")
f(x)=x^2
g(x)=sin(x)
show(diff(f(x),x))
show(diff(g(x),x))
show(diff(f(x)*g(x),x))
show(f(x)*diff(g(x),x)+g(x)*diff(f(x),x))
show("")

show("#3) h(x)=f(x)*g(x)=(x^2)*(x^3), find h'(x).")
f(x)=x^3
g(x)=cos(x)
show(diff(f(x),x))
show(diff(g(x),x))
show(diff(f(x)*g(x),x))
show(f(x)*diff(g(x),x)+g(x)*diff(f(x),x))