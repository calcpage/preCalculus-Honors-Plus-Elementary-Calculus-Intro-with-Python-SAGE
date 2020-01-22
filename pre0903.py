# CONVERSIONS!
# find r=sqrt(x^2+y^2) given z=x+y*i=1+sqrt(3)*i
show(abs(1+sqrt(3)*i).n())
# find theta=arctan(y/x) in degrees given z=x+y*i=1+sqrt(3)*i
show((arg(1+sqrt(3)*i)*180/pi).n())
# find x=r*cos(theta) given z=r*cis(theta)=2*cis(60), theta is in degrees
show(2*cos(60*pi/180))
# find y=r*sin(theta) given z=r*cis(theta)=2*cis(60), theta is in degrees
show(2*sin(60*pi/180))

# PLOTTING ON THE COMPLEX PLANE!
#This function returns a plot of x+y*i as the endpoints of vectors on the complex plane!
def complex_endpoint_plot(pts): 
    """ 
    A function that returns a plot of a list of complex points. 
    Arguments: pts (a list of complex numbers) 
    Outputs: A list plot of the imaginary numbers 
    """ 
    return list_plot([(real(i), imag(i)) for i in pts], axes_labels = ['Re($z$)', 'Im($z$)'], size=30,aspect_ratio=1) 
show(complex_endpoint_plot([1+sqrt(3)*i,2+2*i,e^(i*pi), 3*e^(i*-pi/2), 4-4*i]))
#note: r*cis(theta)=r*e^(i*theta)
pts = [e^(i*theta) for theta in srange(0, 2*pi, pi/4)] 
complex_endpoint_plot(pts) 
