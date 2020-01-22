#79 p436) Find the Sine Curve of Best Fit!
var('a,b,c,d')
l=[[1,24.2],[2,28.4],[3,32.7],[4,39.7],[5,47],[6,53],[7,56],[8,55],[9,49.4],[10,42.2],[11,32],[12,27.1]]
f(x)=a*sin(b*x+c)+d
q=find_fit(l,f,solution_dict=True)
show(q[a])
show(q[b])
show(q[c])
show(q[d])
show(f(a=q[a],b=q[b],c=q[c],d=q[d]))
show(points(l,color='blue')+plot(f(a=q[a],b=q[b],c=q[c],d=q[d]),0,12,color='red'))