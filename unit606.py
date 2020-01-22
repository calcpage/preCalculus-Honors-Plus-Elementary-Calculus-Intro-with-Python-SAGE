#MrG 2015.1118 Known Cross Sections
#Let the base of a solid be the region bound by sqrt(x)+sqrt(y)=3, the x-axis and the y-axis
#Find the volume of the solid if cross sections perpendicular to the x-axis are squares.
show(expand((3-sqrt(x))^4))
show(integrate((3-sqrt(x))^4,x))
show(integrate((3-sqrt(x))^4,x,0,9))
show(integrate((3-sqrt(x))^4,x,0,9).n())