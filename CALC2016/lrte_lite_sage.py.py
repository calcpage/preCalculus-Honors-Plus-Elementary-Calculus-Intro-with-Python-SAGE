#MrG 2018.0517 506 What Is LRTE Lite?
show("506 What Is LRTE Lite?")
f(x)=x^2
a=0
b=4
n=7000
h=(b-a)/n
l=sum([h*f(a+i*h) for i in range(n)])
r=l-h*f(a)+h*f(b)
t=(l+r)/2;err=(r-l)/2
show("LSum=",l.n())
show("RSum=",r.n())
show("TRAP=",t.n())
show("ERROR=",err.n())