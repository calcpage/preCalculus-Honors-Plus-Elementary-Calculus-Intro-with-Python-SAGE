show("MrG 2019.0205 Parametrics")
var('t')
show("#1) graph x(t)=3*t^2, y(t)=2*t")
show(parametric_plot([3*t^2,2*t],(t,0,2)))

show("#2) graph x(t)=3*cos(t), y(t)=4*sin(t)")
show(parametric_plot([3*cos(t),4*sin(t)],(t,0,2*pi)))

show("#3) graph in polar")
r(t)=cos(5*t);show("r(t) = ",r(t))
show(parametric_plot([r(t)*cos(t),r(t)*sin(t)],(t,0,2*pi)))

show("#27) p701:")
x(t)=20*sqrt(2)*t
y(t)=-4.9*t^2+20*sqrt(2)*t+300
show("x(t) = ",x(t))
show("y(t) = ",y(t))
a=solve(y(t)==0,t)[1].rhs().n()
show("tg = ",a," seconds")
show("x(tg) = ",x(a).n()," meters")
show("y(tg) = ",y(a).n()," meters")
b=-20*sqrt(2)/-9.8;show("tz = ",b.n()," seconds")
show("x(tz) = ",x(b).n()," meters")
show("y(tz) = ",y(b).n()," meters")
parametric_plot([x(t),y(t)],(t,0,12))