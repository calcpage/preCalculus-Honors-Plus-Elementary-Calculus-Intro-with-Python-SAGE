#MrG 2015.1118 Horizontal Strips!
#1) find the volume formed when the region bound by y=sqrt(x), y=0 and y=4 is revolved about the y-axis
var('y')
show(integrate(16,y)-integrate(y^4,y))
show(pi*integrate(16,y,0,2)-pi*integrate(y^4,y,0,2))