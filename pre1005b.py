#18) p682: Graph x^2+4*x*y+4*y^2+5*sqrt(5)*y+5==0
var('theta')
a=(cos(theta))^2+4*cos(theta)*sin(theta)+4*(sin(theta))^2
b=5*sqrt(5)*sin(theta)
c=5
polar_plot((-b+sqrt(b^2-4*a*c))/(2*a),0,2*pi)