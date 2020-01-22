#MrG 2018.0823 pre103 The Cartesian Plane & Solving Equations
#1a) Find the distance between point A(1,3) and point B(5,6)
#1b) Find the slope of the line joining point A(1,3) and point B(5,6)
show("#1a) Find the distance between point A(1,3) and point B(5,6)")
show("#1b) Find the slope of the line joining point A(1,3) and point B(5,6)")
Z=point([0,0])
A=point([1,3])
B=point([5,6])
plot(Z+A+B)
dX=1-5;show("dX=",dX);show("dX^2=",dX^2)
dY=3-6;show("dY=",dY);show("dY^2=",dY^2)
show("AB=",sqrt(dX^2+dY^2))
show("m=dY/dX=",dY/dX)
show("")

#2a) Rewrite the equation of a line in slope-intercept form: 2*y+3*x-5==4
#2b) Find the x-intercept of the line: 2*y+3*x-5==4
#2c) Find the y-intercept of the line: 2*y+3*x-5==4
show("#2a) Rewrite the equation of a line in slope-intercept form: 2*y+3*x-5==4")
show("#2b) Find the x-intercept of the line: 2*y+3*x-5==4")
show("#2c) Find the y-intercept of the line: 2*y+3*x-5==4")
var('y')
show(solve(2*y+3*x-5==4,y))
show(solve(2*0+3*x-5==4,x))
show(solve(2*y+3*0-5==4,y))
plot(-3*x/2+9/2,-3,3)
show("")

#3a) Solve for y: 6*x^2+3*y==36
#3b) Find the x-intercept: 6*x^2+3*y==36
#3c) Find the y-intercept: 6*x^2+3*y==36
show("#3a) Solve for y: 6*x^2+3*y==36")
show("#3b) Find the x-intercept: 6*x^2+3*y==36")
show("#3c) Find the y-intercept: 6*x^2+3*y==36")
show(solve(6*x^2+3*y==36,y))
show(solve(6*x^2+3*0==36,x))
show(solve(6*0^2+3*y==36,y))
plot(-2*x^2+12,-sqrt(6),sqrt(6))
show("")

#4) solve for x: 3*(x-2)==5*(x-1)
show("#4) solve for x: 3*(x-2)==5*(x-1)")
show(solve(3*(x-2)==5*(x-1),x))
plot([3*(x-2),5*(x-1)])
show("")

#5) solve for x: x^2==12-x
show("#5) solve for x: x^2==12-x")
show(solve(x^2==12-x,x))
show("")

#6) solve for x: x^2+x-12==0
show("#6) solve for x: x^2+x-12==0")
a=1
b=1
c=-12
d=b^2-4*a*c
show("x1=",(-b+sqrt(d))/(2*a))
show("x2=",(-b-sqrt(d))/(2*a))
def xOne(a,b,c):
    d=b^2-4*a*c
    return (-b+sqrt(d))/(2*a)
def xTwo(a,b,c):
    d=b^2-4*a*c
    return (-b-sqrt(d))/(2*a)
show("x1=",xOne(1,1,-12))
show("x2=",xTwo(1,1,-12))
def quad(a,b,c):
    d=b^2-4*a*c
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    return [x1,x2]
show(quad(1,1,-12))
plot(x^2+x-12,-4,4)