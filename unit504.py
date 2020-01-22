#MrG 2018.0516 504 Proof By Induction?
show("504 Proof By Induction?")
show("#1) show: 1+2+3+...+n = n(n+1)/2")
#1) show: 1+2+3+...+n = n(n+1)/2
#1) let:  1+2+3+...+n = a*n^2+b*n+c
#1) if n=0: 0 == c
#1) if n=1: 1 == a+b+c
#1) if n=2: 3 == 4*a+2*b+c
var('a,b,c')
show(solve([0 == c,1 == a+b+c,3 == 4*a+2*b+c],(a,b,c)))
var('y')
show(solve(1==x+y,y))
show(solve(3==4*x+2*y,y))
show(plot([-x+1,-2*x+3/2]))
show("")

show("#2) show: 1^2+2^2+3^2+...+n^2 = n(n+1)(2n+1)/6")
#2) show: 1^2+2^2+3^2+...+n^2 = n(n+1)(2n+1)/6
#2) let:  1^2+2^2+3^2+...+n^2 = a*n^3+b*n^2+c*n+d
#2) if n=0: 0==d
#2) if n=1: 1==a+b+c+d
#2) if n=2: 5==8*a+4*b+2*c+d
#2) if n=3: 14==27*a+9*b+3*c+d
var('n,d')
show(solve([0==d,1==a+b+c+d,5==8*a+4*b+2*c+d,14==27*a+9*b+3*c+d],(a,b,c,d)))
show(factor(n^3/3+n^2/2+n/6))
var('z')
show(solve(1==x+y+z,z))
show(solve(5==8*x+4*y+2*z,z))
show(solve(14==27*x+9*y+3*z,z))
p1=plot3d(-x-y+1,(x,0,1),(y,0,1),color='red')
p2=plot3d(-4*x-2*y+5/2,(x,0,1),(y,0,1))
p3=plot3d(-9*x-3*y+14/3,(x,0,1),(y,0,1),color='green')
(p1+p2+p3).show(viewer='jmol')
#use jmol if youhave JRE installed in your browser:
#jmol is the default viewer, so you could just evaluate:
#(p1+p2+p3).show(viewer='tachyon')