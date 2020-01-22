#13) p682: Graph 5*x^2+6*x*y+5*y^2-8==0 using polar mode!
var('r,t')
print(solve(5*(r*cos(t))^2+6*r*cos(t)*r*sin(t)+5*(r*sin(t))^2-8==0,r))
polar_plot(-2*sqrt(2)*sqrt(1/(5*cos(t)^2 + 6*cos(t)*sin(t) + 5*sin(t)^2)),(t,0,2*pi),color='red',thickness=4)