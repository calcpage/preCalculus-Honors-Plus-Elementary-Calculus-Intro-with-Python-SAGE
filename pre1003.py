#1) Graph x^2/25+y^2/9==1
var('y')
show(x^2/25+y^2/9==1)
show(solve(x^2/25+y^2/9==1,y))
show(plot([-3/5*sqrt(25-x^2),3/5*sqrt(25-x^2)],-5,5,aspect_ratio=1))
#2) Graph x^2+y^2/9==1
show(x^2+y^2/9==1)
show(solve(x^2+y^2/9==1,y))
show(plot([-3*sqrt(1-x^2),3*sqrt(1-x^2)],-1,1,aspect_ratio=1))
#3) Graph (x-2)^2/9+(y+3)^2/4==1
show((x-2)^2/9+(y+3)^2/4==1)
show(solve((x-2)^2/9+(y+3)^2/4==1,y))
show(plot([-2/3*sqrt(-x^2 + 4*x + 5) - 3,2/3*sqrt(-x^2 + 4*x + 5) - 3],-1,5,aspect_ratio=1))
#4) Graph 4*x^2+y^2-8*x+4*y+4==0
show(4*x^2+y^2-8*x+4*y+4==0)
print(solve(4*x^2+y^2-8*x+4*y+4==0,y))
show(plot([-2*sqrt(-x^2 + 2*x) - 2,2*sqrt(-x^2 + 2*x) - 2],0,2,aspect_ratio=1))