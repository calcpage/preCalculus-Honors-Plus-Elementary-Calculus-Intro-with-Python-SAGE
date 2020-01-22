#MrG 2018.1002 Mean Value Theorem
show("#1) 89AB1")
show("#1a) factor f(x)=x^3-7*x+6 to find all roots of f(x)==0")
f(x)=x^3-7*x+6
show((f(x)/(x-1)).simplify_rational())
show(((x^2+x-6)/(x+3)).simplify_rational())
show(factor(f(x)))
show(solve(f(x)==0,x))
show("#1b) find tangent line to f(x) at x=-1")
g(x)=diff(f(x),x)
show(g(x))
show(f(-1))
show(g(-1))
show(plot([f(x),-4*(x+1)+12],-2,3))
show("#1c) find c such that 1<c<3 satisfying MVT for f(x)")
show(solve(g(x)==6,x)[1].rhs().n())