#MrG 2018.1011 pre503 HowTo Graph Logarithms?
show("#1) Inverse Functions: Logs vs. Exponentials")
#1) note: log(x) in SAGE means ln(x)
#1) f(g(x))==g(f(x)) iff g(x) is the inverse of f(x)
#1) g(x) is a reflection of f(x) iff g(x) is the inverse of f(x)
f(x)=e^x
g(x)=log(x)
show(f(g(x)))
show(g(f(x)).simplify())
show(bool(f(g(x)==g(f(x)))))
show(plot([f(x),x,g(x)],0,2,aspect_ratio=1))
show("")
show("#2) graph y=-ln(x+2) based on the graph of y=ln(x)")
f(x)=ln(x)
p1=plot(f(x),-2,2,color='red')
p2=plot(f(x+2),-2,2,color='green')
p3=plot(-f(x+2),-2,2,color='blue')
show(p1+p2+p3,aspect_ratio=1)
show("")
show("#3) solve for x: log base 3 (4*x-7)==2")
show(solve(log(4*x-7)/log(3)==2,x))
show(plot([log(4*x-7)/log(3),2],2,5,aspect_ratio=1))
show("")
show("#4) solve for x: log base x (64) == 2")
show(solve(log(64)/log(x)==2,x))
show("")
show("#5) solve for x: e^(2*x)==5")
show(solve(e^(2*x)==5,x))
show(solve(e^(2*x)==5,x)[0].rhs().n())
show(solve(e^(2*x)==5,x)[1].rhs().n())
