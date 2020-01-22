#19) p672: Graph x^2/25-y^2/9==1
var('y')
show(x^2/25-y^2/9==1)
print(solve(x^2/25-y^2/9==1,y))
a=plot([-3/5*sqrt(x^2 - 25),3/5*sqrt(x^2 - 25)],5,7,color='red',aspect_ratio=1)
b=plot([-3/5*sqrt(x^2 - 25),3/5*sqrt(x^2 - 25)],-7,-5,color='green',aspect_ratio=1)
a+b