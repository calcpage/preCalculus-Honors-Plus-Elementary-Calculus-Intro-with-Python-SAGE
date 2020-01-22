#29) p185: f(x)==-x^2-6*x, find x-int, y-int, max, graph
f(x)=-x^2-6*x
show(solve(f(x)==0,x))
show(f(0))
show(6/(2*(-1)))
show(f(-3))
show(plot(f(x),-6,0))
#61) p185: maximize area of rectangular field with perimeter 400ft, let x=width
A(x)=x*(200-x)
show(solve(A(x)==0,x))
show(A(0))
show(-200/(2*(-1)))
show(A(100))
show(plot(A(x),0,200))
#75) p185: given crude oil prices for 1990-1996 use a quadratic regresion
#75) p185: to predict price in cents/10^6BTU in 1997
#75) p185: find when the min price occurs and what the min price is
var('a,b,c')
l=[[0,3.69],[1,2.93],[2,2.76],[3,2.40],[4,2.17],[5,2.34],[6,2.90]]
f(x)=a*x^2+b*x+c
q=find_fit(l,f,solution_dict=True)
show(q[a])
show(q[b])
show(q[c])
show(f(a=q[a],b=q[b],c=q[c]))
show(f(a=q[a],b=q[b],c=q[c],x=7))
show(-q[b]/(2*q[a]))
show(f(a=q[a],b=q[b],c=q[c],x=-q[b]/(2*q[a])))
point(l,color='blue')+plot(f(a=q[a],b=q[b],c=q[c]),0,7,color='red')
