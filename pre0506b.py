#MrG 2018.0307 pre506B Graphing Compounded Interest as a Sequence!
show("#1) find the continuous rate if p0=1000, R=7% APR and t=1")
show("#1) Finding the Continuous Rate!")
p0=1000
R=0.07
t=1
var('r')
show(solve(p0*(1+R)^t==p0*e^(r*t),r)[0].rhs().n())
show("#2) show that the limit as n->inf of P0*(1+r/n)^(n*t) = P0*e^(r*t)")
show("#2) let P0=$120000, r=6%, t=2")
show("#2) Graphing Compounded Interest as a Sequence!")
p(n)=120000*(1+0.06/n)^(2*n);show("p(n)=",p(n))
N=range(1000,501000,1000);show("number of compoundings per year n=");show(N)
P=[p(n).n(digits=8) for n in N];show("corresponding future values p(n)=");show(P)
show("euler's limit=",120000*e^(2*0.06).n(digits=8))
pts=zip(N,P);show("points to graph=");show(pts)
show(plot(point(pts)))
show("#3) How Many Digits? (E Day 2/7/2018)") 
show(e.n(digits=1000))
show(21^66)
show(len(str(21^66)))
