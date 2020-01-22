#49 p800
#Maximize: z=f(x,y)=5*x+2*y
#Constraint 0: x>=0, y>=0
#Constraint 1: x+y<=10
#Constraint 2: 2*x+y>=10
#Constraint 3: x+2*y>=10
var('y')
show(solve(x+y==10,y))
show(solve(2*x+y==10,y))
show(solve(x+2*y==10,y))
show(plot([-x+10, -2*x+10, -x/2+5],0,10,fill=true,aspect_ratio=1))
f(x,y)=5*x+2*y
show(f(0,10))
show(f(10,0))
show(f(10/3,10/3).n())