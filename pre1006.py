#1) r=a*cos(t) circle with horizontal symmetry
var('t')
polar_plot([cos(t),2*cos(t),3*cos(t)],0,2*pi)
#2) r=a*sin(t) circle with vertical symmetry
var('t')
polar_plot([sin(t),2*sin(t),3*sin(t)],0,2*pi)
#3) r=cos(a*t) roses with horizontal symmetry
polar_plot(cos(5*t),0,2*pi,color='red',thickness=3)
#4) r=sin(a*t) circle with vertical symmetry
polar_plot(sin(5*t),0,3*pi,color='magenta',thickness=3)
#5) r=a+b*cos(t) cardiods with horizontal symmetry
polar_plot(3+4*cos(t),0,2*pi)
#6) r=a+b*sin(t) cardiods with vertical symmetry
polar_plot(5+6*sin(t),0,2*pi,color='cyan',thickness=2)