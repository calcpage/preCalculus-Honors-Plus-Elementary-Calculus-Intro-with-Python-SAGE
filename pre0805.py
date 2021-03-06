#2015.1013 MrG Harmonic Motion
#1 p549) bob pulled down a=5"
#1 p549) period of oscillation is P=2 sec
f(t)=-5*cos(pi*t)
show(f(t))
show(plot(f(t),0,2))
#9 p549) d=5*sin(3*t)
g(t)=5*sin(3*t)
show(g(t))
show(plot(g(t),0,2*pi/3))
#15 p549) d=6+2*cos(2*pi*t)
h(t)=6+2*cos(2*pi*t)
show(h(t))
show(plot(h(t),0,1))
#31 p549) v(t)=e^(-1.9*t)*cos(pi*t)
v(t)=e^(-1.9*t)*cos(pi*t)
show(v(t))
p1=plot([-e^(-1.9*t),e^(-1.9*t)],0,4,color='red')
p2=plot(v(t),0,4,color='green')
show(p1+p2)
