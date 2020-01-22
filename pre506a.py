#MrG 2018.0307 pre506A Graphing Compounded Interest as a Sequence!
show("#1) find the effective yield if p0=1000, r=6% compounded continuously and t=1")
show("Finding the Effective Yield!")
p0=1000
r=0.06
t=1
var('R')
show(solve(p0*(1+R)*t==p0*e^(r*t),R)[0].rhs().n())
show("#2) show that the limit as n->inf of P0*(1+r/n)^n = P0*e^r")
show("#2) let P0=$1000, r=10%")
show("#2) Graphing Compounded Interest as a Sequence!")
p(n)=1000*(1+0.10/n)^n;show("p(n)=",p(n))
N=range(10,1210,10);show("number of compoundings per year n=");show(N)
P=[p(n).n(digits=6) for n in N];show("corresponding future values p(n)=");show(P)
show("euler's limit=",1000*e^0.10.n(digits=6))
pts=zip(N,P);show("points to graph=");show(pts)
show(plot(point(pts)))
show("#3) How Many Digits? (PI Day 3/14/18)")
show(pi.n(digits=1000))
show(66^21)
show(len(str(66^21)))