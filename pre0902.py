var('t')
#cardioids with vertical symmetry
show(polar_plot(1-1*sin(t),0,2*pi))
show(polar_plot(1-2*sin(t),0,2*pi))
show(polar_plot(2-1*sin(t),0,2*pi))
#cardioids with horizontal symmetry
show(polar_plot(1-1*cos(t),0,2*pi))
show(polar_plot(1-2*cos(t),0,2*pi))
show(polar_plot(2-1*cos(t),0,2*pi))
#roses with 1, 4 and 3 petals
show(polar_plot(2*sin(t),0,2*pi,color='red'))
show(polar_plot(2*sin(2*t),0,2*pi,color='red'))
show(polar_plot(2*sin(3*t),0,2*pi,color='red'))
#lemniscates
show(polar_plot(sqrt(2*sin(t)),0,2*pi,color='green'))
show(polar_plot(sqrt(2*sin(2*t)),0,2*pi,color='green'))
show(polar_plot(sqrt(2*sin(3*t)),0,2*pi,color='green'))
