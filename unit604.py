#MrG 2015.1118 Washer Method
#81AB2: Find the volume formed when the region bound by y=4-x^2, y=3*x and the y-axis is revolved about the x-axis
show(expand((4-x^2)^2-(3*x)^2))
show(integrate((4-x^2)^2-(3*x)^2,x))
show(pi*integrate((4-x^2)^2-(3*x)^2,x,0,1))
show((pi*integrate((4-x^2)^2-(3*x)^2,x,0,1)).n())
#91AB2: Find the volume formed when the region bound by y=x^2, y=1-sin(pi*x) and the y-axis is revolved about the x-axis
show(expand((1-sin(pi*x))^2-(x^2)^2))
show(integrate((1-sin(pi*x))^2-(x^2)^2),x)
show(pi*integrate((1-sin(pi*x))^2-(x^2)^2,x,0,1))
show((pi*integrate((1-sin(pi*x))^2-(x^2)^2,x,0,1)).n())
