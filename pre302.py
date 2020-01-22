#MrG 2015.0303 Power Functions
#1) Even Functions
p1=plot(x^2,-1,1,color='red')
p2=plot(x^4,-1,1,color='green')
p3=plot(x^10,-1,1,color='blue')
p1+p2+p3
#2) Odd Functions
p1=plot(x^3,-1,1,color='red')
p2=plot(x^5,-1,1,color='green')
p3=plot(x^7,-1,1,color='blue')
p1+p2+p3
#3) Symmetry
f(x)=x^4
show(bool(f(-x)==f(x)))
f(x)=x^5
show(bool(f(-x)==-f(x)))
#4) Limits
show(limit(x^4,x=+Infinity))
show(limit(x^4,x=-Infinity))
show(limit(x^5,x=+Infinity))
show(limit(x^5,x=-Infinity))