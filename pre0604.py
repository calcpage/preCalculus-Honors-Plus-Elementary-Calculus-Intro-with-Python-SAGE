#1) graph Sin(x) and Cos(x)
p1=plot(sin(x),0,2*pi,color='red')
p2=plot(cos(x),0,2*pi,color='green')
show(p1+p2)
#2) graph dilations - vertical stretch
p1=plot(2*sin(x),0,2*pi,color='red')
p2=plot(3*cos(x),0,2*pi,color='green')
show(p1+p2)
#3) graph dilations - horizontal shrink
p1=plot(sin(2*x),0,2*pi,color='red')
p2=plot(cos(3*x),0,2*pi,color='green')
show(p1+p2)
#4) graph translations - vertical and horizontal
p1=plot(sin(x-pi/2),0,2*pi,color='red')
p2=plot(cos(x)+1,0,2*pi,color='green')
show(p1+p2)
#5) graph reflections - vertical and horizontal
p1=plot(-sin(x),0,2*pi,color='red')
p2=plot(cos(-x),0,2*pi,color='green')
show(p1+p2)
