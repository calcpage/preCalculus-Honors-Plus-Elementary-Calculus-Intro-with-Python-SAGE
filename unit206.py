#MrG 2018.0912 UNIT206: Differentibility II
show("#81AB5 ")
f1(x)=2*x+1 
f2(x)=x^2/2+3 
f=piecewise([[(-2,2),f1],[(2,5),f2]]) 
show(plot(f))
show("")

show("#76AB7a")
var('h') 
f(x)=x^2+x 
show(lim((f(x+h)-f(x))/h,h=0)) 
show(lim((f(x+h)-f(x-h))/h,h=0)) 
show("")

show("#76AB7b")
f(x)=cos(x) 
show(lim((f(x+h)-f(x))/h,h=0)) 
show(lim((f(x+h)-f(x-h))/h,h=0)) 