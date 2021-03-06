#MrG 2018.1010 pre502 How To Graph Exponential Curves?
show("#1) analyze and graph f(x)=2^x")
f(x)=2^x;show(f(x))
show(plot(f(x),-2,3))
show([f(x) for x in range(-2,3)])
show([f(x).n(digits=3) for x in range(-2,3)])
for x in range(-2,3):
    show([x,f(x)])
show("")
show("#2) analyze and graph f(x)=2^(-x)")
f(x)=2^(-x);show(f(x))
show(plot(f(x),-2,3))
show([f(x) for x in range(-2,3)])
show([f(x).n(digits=3) for x in range(-2,3)])
for x in range(-2,3):
    show([x,f(x)])
show("")
show("#3) analyze and graph f(x)=2^(-x)-3 with asymptote")
f(x)=2^(-x)-3;show(f(x))
show(plot([f(x),-3],-2,3))
show([f(x) for x in range(-2,3)])
show([f(x).n(digits=3) for x in range(-2,3)])
for x in range(-2,3):
    show([x,f(x)])
show("")
show("#4) solve for x: 3^(x+1)==81")
var('x')
show(solve(3^(x+1)==81,x))
show(plot([3^(x+1),81],0,5))
show("")
show("#5) solve for x: e^(-x^2)==e^(2*x)*e^(-3)")
show(solve(e^(-x^2)==e^(2*x)*e^(-3),x))
plot([e^(-x^2),e^(2*x)*e^(-3)],-4,2)
