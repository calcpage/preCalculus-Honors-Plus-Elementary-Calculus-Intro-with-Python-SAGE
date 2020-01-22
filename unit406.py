#MrG 2018.1010 UNIT406 How To Program The Quadratic Formula?
show("#1) solve a*x^2+b*x+c==0")
var('a,b,c,x')
show(solve(a*x^2+b*x+c==0,x))
show("")
show("#2) write a function disc() to calculate the discriminant: x^2+2*x+2==0")
def disc(a,b,c):
    return b^2-4*a*c
show(disc(1,2,2))
show("")
show("#3) write a function re() to calculate the real part of the root: x^2+2*x+2==0")
def re(a,b):
    return -b/(2*a)
show(re(1,2))
show("")
show("#4) write a function im() to calculate the imaginary part of the root: x^2+2*x+2==0")
def im(a,d):
    return sqrt(d)/(2*a)
show(im(1,disc(1,2,2)))
show("")
show("#5) write a function quad() to calculate noth roots: x^2+2*x+2==0")
def quad(a,b,c):
    return [re(1,2)+im(1,disc(1,2,2)),re(1,2)-im(1,disc(1,2,2))]
show(quad(1,2,2))