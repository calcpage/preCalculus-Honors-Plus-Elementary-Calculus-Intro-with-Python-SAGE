#3) Find all POIs: x^2-y^2==4, y==x^2
var('y')
show(solve([x^2-y^2==4,y==x^2],x,y))
show(solve(x^2-y^2==4,y))
a=plot([-sqrt(x^2-4)],-4,-2,color='red')
b=plot([-sqrt(x^2-4)],2,4,color='red')
c=plot([sqrt(x^2-4)],-4,-2,color='green')
d=plot([sqrt(x^2-4)],2,4,color='green')
e=plot([x^2],-4,4,color='orange')
show(a+b+c+d+e)
show(a+b+c+d+e,aspect_ratio=1)