#MrG 2018.0823 pre202 Function Properties
#1) f(x)=2*x^2-3*x find the average value of f(x) from x=1 to x=2
#1) Find the equation of the secant line from x=1 to x=2
show("#1) f(x)=2*x^2-3*x find the average value of f(x) from x=1 to x=2")
show("#1) Find the equation of the secant line from x=1 to x=2")
var('y')
f(x)=2*x^2-3*x
show("f(1)=",f(1))
show("f(2)=",f(2))
m=(f(1)-f(2))/(1-2);show("m=",m)
show(y-2==m*(x-2))
plot([f(x),3*x-4],0,2,aspect_ratio=1)
show("")

#2) g(x)=6*x^3-12*x+5 find the average value of g(x) from x=0 to x=2
#2) Find the equation of the secant line from x=0 to x=2
show("#2) g(x)=6*x^3-12*x+5 find the average value of g(x) from x=0 to x=2")
show("#2) Find the equation of the secant line from x=0 to x=2")
g(x)=6*x^3-12*x+5
show("g(1)=",g(1))
show("g(2)=",g(2))
m=(g(1)-g(2))/(1-2);show("m=",m)
show(y+1==m*(x-1))
plot([g(x),30*x-31],0,2)
show("")

#3) Is f(x)=x^2-5 an even or odd function?
#3) even: f(-x)=f(x), odd: f(-x)=-f(x)
show("#3) Is f(x)=x^2-5 an even or odd function?")
show("#3) even: f(-x)=f(x), odd: f(-x)=-f(x)")
f(x)=x^2-5;show("f(x)=",f(x));show("f(-x)=",f(-x))
plot(f(x))
show("")

#4) Is f(x)=x^3-x an even or odd function?
#4) even: f(-x)=f(x), odd: f(-x)=-f(x)
show("#4) Is f(x)=x^3-x an even or odd function?")
show("#4) even: f(-x)=f(x), odd: f(-x)=-f(x)")
f(x)=x^3-x;show("f(x)=",f(x));show("f(-x)=",f(-x))
plot(f(x))
show("")

#5) Is f(x)=x^3-1 an even or odd function?
#5) even: f(-x)=f(x), odd: f(-x)=-f(x)
show("#5) Is f(x)=x^3-1 an even or odd function?")
show("#5) even: f(-x)=f(x), odd: f(-x)=-f(x)")
f(x)=x^3-1;show("f(x)=",f(x));show("f(-x)=",f(-x))
plot(f(x))
show("")

#6) Is f(x)=abs(x) an even or odd function?
#6) even: f(-x)=f(x), odd: f(-x)=-f(x)
show("#6) Is f(x)=abs(x) an even or odd function?")
show("#6) even: f(-x)=f(x), odd: f(-x)=-f(x)")
f(x)=abs(x);show("f(x)=",f(x));show("f(-x)=",f(-x))
plot(f(x))
