#1) solve for (x,y): 2*x-y==2, 6*x+8*y==39
#1) old way!
var('y')
show(solve([2*x-y==2, 6*x+8*y==39],x,y))
show(solve(2*x-y==2,y))
show(solve(6*x+8*y==39,y))
plot([2*x-2,-3*x/4+39/8],0,3)