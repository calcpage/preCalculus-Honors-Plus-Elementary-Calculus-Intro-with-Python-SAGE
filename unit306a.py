#MrG 2018.0509 UNIT306: What Is Implicit Differentiation?
show("#1) Find dy/dx if (x-1)^2+(y-1)^2==13 aka (x-1)^2+(y-1)^2-13==0")
show("Find dy/dx if (x-1)^2+(y-1)^2-13==0")
y=function('y')(x)
show(diff((x-1)^2+(y-1)^2-13,x))
show("")

show("#2) Implicitly differentiate x^2+y^2==15^2 aka x^2+y^2-225==0 wrt time")
show("Implicitly differentiate x^2+y^2-225==0 wrt time")
var('t')
x=function('x')(t)
y=function('y')(t)
show(diff(x^2+y^2-225,t))