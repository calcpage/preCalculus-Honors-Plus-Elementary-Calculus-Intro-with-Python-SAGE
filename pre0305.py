#MrG 2015.0310 More Rational Functions
#27) p228: f(x)=(x^2+x-12)/(x^2-x-6)
#show that horizontal asymptote is y=1
f(x)=(x^2+x-12)/(x^2-x-6)
show(f(x))
show(f(x).partial_fraction())
#why does f(x) only have 1 vertical asymptote?
show(factor(x^2+x-12))
show(factor(x^2-x-6))
show(factor(f(x)))
show(f(x).simplify_rational())
#show that the x-intercepts is (-4,0) 
show(solve(x^2+x-12==0,x))
show(solve(f(x)==0,x))
#show that the y-intercept is (0,2)
show(f(0))
#make a complete sketch of f(x)
show(plot([f(x),1],xmin=-10,xmax=5,ymin=-5,ymax=5))
#what's the domain?
#x!=-2, x!=3
#what is the range?
#y!=1, y!=7/5
#discuss the limits
show(lim(f(x),x=infinity))
show(lim(f(x),x=-infinity))
show(lim(f(x),x=-2,dir='left'))
show(lim(f(x),x=-2,dir='right'))
show(lim(f(x),x=3,dir='left'))
show(lim(f(x),x=3,dir='right'))
