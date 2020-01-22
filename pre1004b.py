#50 p672: Graph 2*y^2-x^2+2*x+8*y+3==0
var('y')
show(2*y^2-x^2+2*x+8*y+3==0)
print(solve(2*y^2-x^2+2*x+8*y+3==0,y))
plot([-1/2*sqrt(2*x^2 - 4*x + 10) - 2,1/2*sqrt(2*x^2 - 4*x + 10) - 2],-3,5,aspect_ratio=1)
