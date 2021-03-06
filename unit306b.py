#MrG 2018.0509 UNIT306b: What Is Optimization?
show("#1) Maximize Profit aka p(x) given")
show("#1) r(x)=8*sqrt(x) and c(x)=2*x^2")
show("Maximize Profit aka p(x)")
r(x)=8*sqrt(x);show("r(x)=",r(x))
c(x)=2*x^2;show("c(x)=",c(x))
p(x)=r(x)-c(x);show("p(x)=",p(x))
pp(x)=diff(p(x),x);show("p'(x)=",pp(x))
show(solve(pp(x)==0,x))
show(p(1))