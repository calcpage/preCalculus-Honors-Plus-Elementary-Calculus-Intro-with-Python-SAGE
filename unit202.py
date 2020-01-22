#MrG 2015.0318 UNIT 202: IVT, MIN/MIN, Continuity
show("#1) apply MIN/MAX Theorem on a closed interval")
f(x)=5*x^3-5*x
show(plot(f(x),0,2))
show(factor(f(x)))
show("")

show("#2) use IVT, Intermediate Value Theorem, to show the existance of the root")
g(x)=x^3+x-1
show(plot(g(x)))
show(solve(g(x)==0,x)[2].rhs().n())
show("")

show("#3) find the hole using the definition of continuity")
h(x)=(x^3-3*x^2-4*x+12)/(x-3)
show(plot(h(x),-4,4))
show(h(x).simplify_rational())
#show(h(3)) #should be an error
show("")

show("#4) AP Calculus AB FRQ: 76AB2 ")
show("#4) h(x)=f(x)/(x-3) when x!=3 ")
show("#4) h(x)=p when x=3 #2b) find p to make h continuous h(x)=f(x)/(x-3) ")
show(h(x)) 
show(factor(h(x))) 
show(solve(h(x)==0,x)) 
p1=plot(h(x),-4,3,color='red') 
p2=plot(h(x),3,4,color='green') 
show(p1+p2) 
#4) h(3)=p 
#4) lim(h(x),x=3,dir='left')=lim(h(x),x=3,dir='right')=5 
#4) p=5 
show("")

show("#5) h(x)=f(x)/(x-3) when x!=3 ")
show("#5) is h(x) an even function? ")
show(h(x)) 
show(h(-x)) 
#yes! 