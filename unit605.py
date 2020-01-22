#MrG 2015.1118 Shell Method!
#71AB5: Find the volume formed when the region bound by y=2*x-x^2 and the x-axis in QI is revolved about the y-axis
show(expand(x*(2*x-x^2)))
show(integrate(x*(2*x-x^2),x))
show(2*pi*integrate(x*(2*x-x^2),x,0,2))