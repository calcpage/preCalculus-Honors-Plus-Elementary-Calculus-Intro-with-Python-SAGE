#1) find all POIs: 3*x-y==-2, 2*x^2-y==0
var('y')
show(solve(3*x-y==-2,y))
show(solve(2*x^2-y==0,y))
show(solve([3*x-y==-2, 2*x^2-y==0],x,y))
show(plot([3*x+2,2*x^2],-1,3))
show(plot([3*x+2,2*x^2],-1,3,aspect_ratio=1))