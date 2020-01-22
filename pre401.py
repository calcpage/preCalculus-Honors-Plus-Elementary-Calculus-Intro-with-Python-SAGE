#MrG 2018.0312 401 Solving Polynomials Equations!
show("#1) analyze f(x)=2*x^3-x^2+2*x-3")
show("solve for x: 2*x^3-x^2+2*x-3==0")
f(x)=2*x^3-x^2+2*x-3
show(f(1))
show(factor(f(x)))
show((f(x)/(x-1)).simplify_rational())
show(solve(f(x)==0,x))
show(plot(f(x),-5,5))
show("")

show("#2) analyze f(x)=2*x^3+11*x^2-7*x-6")
show("solve for x: 2*x^3+11*x^2-7*x-6==0")
f(x)=2*x^3+11*x^2-7*x-6
show(f(1))
show(factor(f(x)))
show((f(x)/(x-1)).simplify_rational())
show((f(x)/((x-1)*(x+6))).simplify_rational())
show(solve(f(x)==0,x))
show(plot(f(x),-7,2))