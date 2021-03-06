#MrG 2014.0924 Solve: x+y-z=1,4x-3y+2z=16,2x-2y-3z=5
var('y,z')
show(solve([x+y-z==-1,4*x-3*y+2*z==16,2*x-2*y-3*z==5],x,y,z))
show(solve(x+y-z==-1,z))
show(solve(4*x-3*y+2*z==16,z))
show(solve(2*x-2*y-3*z==5,z))
p1=plot3d(x+y+1,(x,-4,4),(y,-4,4),color='red')
p2=plot3d(-2*x+3*y/2+8,(x,-4,4),(y,-4,4),color='green')
p3=plot3d(2*x/3-2*y/3-5/3,(x,-4,4),(y,-4,4),color='brown')
(p1+p2+p3).show(viewer='tachyon')