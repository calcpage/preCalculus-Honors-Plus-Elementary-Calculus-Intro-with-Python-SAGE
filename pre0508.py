#MrG 2018.1017 pre508 Exponential and Logarithic Regression
show("#1 p355) Find the Exponential Curve of Best Fit!")
var('a,b')
l=[[0,1000],[1,1415],[2,2000],[3,2828],[4,4000],[5,5656],[6,8000]]
f(x)=a*b^x
q=find_fit(l,f,solution_dict=True)
show(q[a])
show(q[b])
show(f(a=q[a],b=q[b]))
show(f(a=q[a],b=q[b],x=7))
show(points(l,color='blue')+plot(f(a=q[a],b=q[b]),0,7,color='red'))
show("#9 p355) Find the Logarithmic Curve of Best Fit!")
var('a,b')
l=[[5,12],[10,-3],[15,-11],[20,-17],[25,-22],[30,-25],[35,-27]]
f(x)=a+b*log(x)
q=find_fit(l,f,solution_dict=True)
show(q[a])
show(q[b])
show(f(a=q[a],b=q[b]))
show(f(a=q[a],b=q[b],x=23).n())
show(points(l,color='blue')+plot(f(a=q[a],b=q[b]),0,35,color='red'))
