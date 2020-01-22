#MrG 2018.0823 pre106 Linear Equations
#1) Find the equation of the line through A(1,2) and B(5,-3)
show("#1) Find the equation of the line through A(1,2) and B(5,-3)")
var('y')
dY=2-(-3)
dX=1-5
m=dY/dX;show("m=",m)
show(y-2==m*(x-1))
show(solve(y-2==m*(x-1),y))
show(y-(-3)==m*(x-5))
show(solve(y-(-3)==m*(x-5),y))
plot(-5*x/4+13/4,0,5)
show("")

#2) Given the line 4*x-y==2, find the x and y intercepts.
show("#2) Given the line 4*x-y==2, find the x and y intercepts.")
show(solve(4*x-y==2,y))
show(solve(4*0-y==2,y))
show(solve(4*x-0==2,x))
plot(4*x-2)
show("")

#3) Are 2*x+3*y==6 and 4*x==-6*y parallel, perpendicular or neither?
show("#3) Are 2*x+3*y==6 and 4*x+6*y==0 parallel, perpendicular or neither?")
show(solve(2*x+3*y==6,y))
show(solve(4*x==-6*y,y))
plot([-2*x/3+2,-2*x/3])
show("")

#4) Are y==-2*x/3+2 and y==3*x/2 parallel, perpendicular or neither?
show("#4) Are y==-2*x/3+2 and y==3*x/2 parallel, perpendicular or neither?")
plot([-2*x/3+2,3*x/2],aspect_ratio=1)
show("")

#5) Find a line containing the point (1,-2) and perpendicular to x+3*y==6
show("#5) Find a line containing the point (1,-2) and perpendicular to x+3*y==6")
show(solve(x+3*y==6,y))
show(y-(-2)==3*(x-1))
show(solve(y-(-2)==3*(x-1),y))
show(solve(-x/3+2==3*x-5,x))
plot([-x/3+2,3*x-5],0,3,aspect_ratio=1)