#1) solve for x: 2*sin(x)^2-3*sin(x)+1==0
show(solve(2*sin(x)^2-3*sin(x)+1==0,x))
show(plot(2*sin(x)^2-3*sin(x)+1,0,2*pi))
#2) solve for x: 3*cos(x)+3==2*sin(x)^2
show(solve(3*cos(x)+3==2*sin(x)^2,x))
show(plot([3*cos(x)+3,2*sin(x)^2],0,2*pi))
#3) solve for x: cos(x)^2+sin(x)==2
show(solve(cos(x)^2+sin(x)==2,x))
show(plot([cos(x)^2+sin(x),2],0,2*pi))
#4) solve for x: 5*sin(x)+x==3
show(solve(5*sin(x)+x==3,x))
show(plot([5*sin(x)+x,3],0,2*pi))