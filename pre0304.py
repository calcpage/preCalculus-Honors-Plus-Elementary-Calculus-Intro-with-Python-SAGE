#MrG 2015.0309 Rational Functions
f(x)=x^3/(x^4-1)
show(f(x))
#find x-intercepts
show(solve(x^3==0,x))
#find y-intercepts
show(f(0))
#what's the domain?
show(solve(x^4-1==0,x))
#what's the range?
show(plot(f(x),-2,2))
#state the limits!
show(lim(f(x),x=infinity))
show(lim(f(x),x=-infinity))
show(lim(f(x),x=1,dir='left'))
show(lim(f(x),x=1,dir='right'))
show(lim(f(x),x=-1,dir='left'))
show(lim(f(x),x=-1,dir='right'))
