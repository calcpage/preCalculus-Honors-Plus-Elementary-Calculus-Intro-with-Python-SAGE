#2) Find all POIs: x^2+y^2==13, x^2-y==7
var('y')
show(solve(x^2+y^2==13,y))
show(solve(x^2-y==7,y))
show(solve([x^2+y^2==13,x^2-y==7],x,y))
show(plot([-sqrt(13-x^2),sqrt(13-x^2),x^2-7],-sqrt(13),sqrt(13)))
plot([-sqrt(13-x^2),sqrt(13-x^2),x^2-7],-sqrt(13),sqrt(13),aspect_ratio=1)
