#MrG 2018.0823 pre201 Functions
#1) Given y=f(x)=2*x-5 on the closed interval 1<=x<=6, find the range
show("#1) Given y=f(x)=2*x-5 on the closed interval 1<=x<=6, find the range")
f(x)=2*x-5
show("f(x)=",f(1))
show("f(6)=",f(6))
plot(f(x),0,6)
show("")

#2) Given g(x)=2*x^2-3*x, calculate the following:
show("#2) Given g(x)=2*x^2-3*x, calculate the following:")
g(x)=2*x^2-3*x
show("g(x)=",g(x))
show("g(3)=",g(3))
show("g(-x)=",g(-x))
show("-g(x)=",-g(x))
show("-g(-x)=",-g(-x))
show("g(x)+g(3)=",g(x)+g(3))
show("g(x+3)=",g(x+3).expand())
show("")

#3) State the domain & range: f(x)=x^2+5*x
show("#3) State the domain & range: f(x)=x^2+5*x")
f(x)=x^2+5*x
show("-b/(2*a)=",-5/(2*1))
show("f(-2.5)=",f(-2.5))
plot(f(x),-5,5)
show("")

#4) State the domain & range: f(x)=3*x/(x^2-4)
show("#4) State the domain & range: f(x)=3*x/(x^2-4)")
f(x)=3*x/(x^2-4)
show("f DNE x=",solve(x^2-4==0,x))
show("f(0)=",f(0))
plot(f(x),xmin=-5,xmax=5,ymin=-10,ymax=10)
show("")

#5) State the domain & range: f(x)=sqrt(4-3*x)
show("#5) State the domain & range: f(x)=sqrt(4-3*x)")
f(x)=sqrt(4-3*x)
show("f DNE x>=",solve(4-3*x==0,x))
show("f(0)=",f(0))
plot(f(x),-5,4/3)
