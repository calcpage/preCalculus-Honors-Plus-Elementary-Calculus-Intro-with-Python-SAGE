#MrG 2018.0823 pre107 Linear Regression
#7 p80) Find the equation of the line through the points:
#7 p80) (3,4), (4,6), (5,7), (6,10), (7,12), (8,14), (9,16)
#7 p80) interpolate f(7.5), extrpolate f(11.2)
show("#7 p80) Find the equation of the line through the points:")
show("#7 p80) (3,4), (4,6), (5,7), (6,10), (7,12), (8,14), (9,16)")
show("#7 p80) interpolate f(7.5), extrpolate f(11.2)")
var('m,b')
l=[[3,4], [4,6], [5,7], [6,10], [7,12], [8,14], [9,16]]
f(x)=m*x+b
q=find_fit(l,f,solution_dict=True)
show("m=",q[m])
show("b=",q[b])
show("y=",f(m=q[m],b=q[b]))
show("y(7.5)=",f(m=q[m],b=q[b],x=7.5))
show("y(11.2)=",f(m=q[m],b=q[b],x=11.2))
points(l,color='blue')+plot(f(m=q[m],b=q[b]),0,10,color='red')
show("")

#24 p80) Find the equation of the line through the points:
#24 p80) (1991,1366.1), (1992,1381.7), (1993,1374.8), (1994,1392.8), (1995,1407.8), (1996,1412), (1997,1414), (1998,1441)
#24 p80) extrpolate f(9) and f(20) for the years 1999 and 2000. [x]=year, [y]=billion $ spent by the federal government
show("#24 p80) Find the equation of the line through the points:")
show("#24 p80) (1991,1366.1), (1992,1381.7), (1993,1374.8), (1994,1392.8), (1995,1407.8), (1996,1412), (1997,1414), (1998,1441)")
show("#24 p80) extrpolate f(9) and f(20) for the years 1999 and 2000. [x]=year, [y]=billion $ spent by the federal government")
var('m,b')
l=[[1,1366.1], [2,1381.7], [3,1374.8], [4,1392.8], [5,1407.8], [6,1412], [7,1414], [8,1441]]
f(x)=m*x+b
q=find_fit(l,f,solution_dict=True)
show("m=",q[m])
show("b=",q[b])
show("y=",f(m=q[m],b=q[b]))
show("y(9)=",f(m=q[m],b=q[b],x=9))
show("y(20)=",f(m=q[m],b=q[b],x=20))
points(l,color='blue')+plot(f(m=q[m],b=q[b]),0,10,color='red')