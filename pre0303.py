#11) p205: analyze a polynomial with roots {-1,1,3}
f(x)=(x+1)*(x-1)*(x-3)
show(f(x))
show(expand(f(x)))
show(limit(f(x),x=-Infinity))
show(limit(f(x),x=+Infinity))
show(plot(f(x),-2,4))
show(max([f(x) for x in srange(-1,1,.01)]))
show(min([f(x) for x in srange(1,3,.01)]))
#17) p205: analyze f(x)=3*(x-7)*(x+3)^2
f(x)=3*(x-7)*(x+3)^2
show(f(x))
show(expand(f(x)))
show(limit(f(x),x=-Infinity))
show(limit(f(x),x=+Infinity))
show(plot(f(x),-4,8))
show(max([f(x) for x in srange(-4,-2,.01)]))
show(min([f(x) for x in srange(3,4,.01)]))

