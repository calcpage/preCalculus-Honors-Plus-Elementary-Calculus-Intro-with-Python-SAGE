#MrG 2018.0823 pre203 Function Library
#1) What do y==m*x+b, y-y1==m*(x-x1), x/a+y/b==1, A*x+B*y==C look like?
show("#1) What does y=m*x+b look like?")
var('y')
plot(2*x-4,0,2)
show(solve(y+4==2*(x-0),y))
show(solve(x/2-y/4==1,y))
show(solve(2*x-y==4,y))
show("")

#2) What does y=x^2 look like?
show("#2) What does y=x^2 look like?")
f(x)=x^2
show("f(-x)=",f(-x))
plot(f(x))
show("")

#3) What does y=x^3 look like?
show("#3) What does y=x^3 look like?")
f(x)=x^3
show("f(-x)=",f(-x))
plot(f(x))
show("")

#4) What does y=1/x look like?
show("#4) What does y=1/x look like?")
f(x)=1/x
show("f(-x)=",f(-x))
plot(f(x),xmin=-1,xmax=1,ymin=-10,ymax=10)
show("")

#5) What does y=abs(x) look like?
show("#5) What does y=abs(x) look like?")
f(x)=abs(x)
show("f(-x)=",f(-x))
plot(f(x))
show("")

#6) What does y=floor(x) look like?
show("#6) What does y=floor(x) look like?")
f(x)=floor(x)
show("f(-x)=",f(-x))
plot(f(x),0,10)
show("")

#7) What is a piece-wise defined function?
show("#7) What is a piece-wise defined function?")
f(x) = piecewise([((0,1), x^3), ([-1,0], x)])
plot(f(x))
show("")

#8) Find the inverse of y=x^2
show("#8) Find the inverse of y=x^2")
show(solve(x==y^2,y))
plot([x^2,sqrt(x),-sqrt(x)],aspect_ratio=1)
