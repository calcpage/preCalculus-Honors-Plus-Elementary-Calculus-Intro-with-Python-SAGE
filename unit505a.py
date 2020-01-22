#MrG 2015.0501 Practice Programming Python Functions
#1) find the Discriminant of a quadratic equation: a+x^2+b*x+c==0
def disc(a,b,c):
    return b^2-4*a*c
show(disc(1,2,2))
show(disc(1,2,1))
show(disc(1,2,0))
show(disc(1,2,-1))
#2) find the "real part" of the roots of a+x^2+b*x+c==0 when disc(a,b,c)<0
def real(a,b):
    return -b/(2*a)
show(real(1,2))
#3) find the "imaginary part" of the roots of a+x^2+b*x+c==0 when disc(a,b,c)<0
def imag(a,d):
    return sqrt(d)/(2*a)
show(imag(1,disc(1,2,2)))
show(imag(1,disc(1,2,1)))
show(imag(1,disc(1,2,0)))
show(imag(1,disc(1,2,-1)))
#4) find root1 and root2!
def root1(a,b,c):
    return real(a,b)+imag(a,disc(a,b,c))
def root2(a,b,c):
    return real(a,b)-imag(a,disc(a,b,c))
show(root1(1,2,2))
show(root2(1,2,2))
show(root1(1,2,1))
show(root2(1,2,1))
show(root1(1,2,0))
show(root2(1,2,0))
show(root1(1,2,-1))
show(root2(1,2,-1))