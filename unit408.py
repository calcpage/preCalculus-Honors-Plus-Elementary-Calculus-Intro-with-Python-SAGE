#MrG 2018.1009 UNIT408 How To Optimize?
show("#1) 1972 AB 4: find abs max of the area")
A(x)=2*x^2+(85-3*x/2)^2
show(A(x).expand())
aPrime=A(x).diff(x)
show(aPrime)
show(solve(aPrime==0,x))
show(A(20))
show(A(30))
show(A(50))
p1=plot(A(x),20,50,color='red')
p2=plot(aPrime(x),20,50,color='green')
show(p1+p2)