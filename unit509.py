#MrG 2015.0514 509 Definite vs InDefinite Integrals!
#1) FRQ 1988AB6 Given: f'(x)=a*x^2+b*x, 
#1) FRQ 1988AB6 Given: f'(1)=6, f"(1)=18,
#1) FRQ 1988AB6 Given: integrate(f(x),x,1,2=18)
#1) FRQ 1988AB6 Find f(x)!
show("FRQ 1988AB6")
var('a,b')
fp(x)=a*x^2+b*x
fpp(x)=diff(fp(x),x)
show(fp(x))
show(fpp(x))
show(fp(1))
show(fpp(1))
show(solve([fp(1)==6,fpp(1)==18],(a,b)))
show(fp(x,a=12,b=-6))
f(x)=integrate(fp(x,a=12,b=-6),x)
var('C')
show(f(x)+C)
show(integrate(f(x)+C,x))
show(integrate(f(x)+C,x,1,2))
show(solve(C+8==18,C))
show(f(x)+10)
show("")

#2) (Trig Identity) T/F: integrate(cos(x)^2,x)==integrate(1/2+cos(2*x)/2,x)
show("(Trig Identity) T/F: integrate(cos(x)^2,x)==integrate(1/2+cos(2*x)/2,x)")
show(integrate(cos(x)^2,x))
show(integrate(1/2+cos(2*x)/2,x))
show(bool(integrate(cos(x)^2,x)==integrate(1/2+cos(2*x)/2,x)))
show("")

#3) (Trig Identity) T/F: integrate(sin(x)^2,x)==integrate(1/2-cos(2*x)/2,x)
show("(Trig Identity) T/F: integrate(sin(x)^2,x)==integrate(1/2-cos(2*x)/2,x)")
show(integrate(sin(x)^2,x))
show(integrate(1/2-cos(2*x)/2,x))
show(bool(integrate(sin(x)^2,x)==integrate(1/2-cos(2*x)/2,x)))
show("")

#4a) (MCQ choice A) T/F: integrate(x*cos(x),x)==x*sin(x)+C
show("(MCQ choice A) T/F: integrate(x*cos(x),x)==x*sin(x)+C")
show(integrate(x*cos(x),x))
show(bool(integrate(x*cos(x),x)==x*sin(x)))
show("")

#4b) (MCQ choice B) T/F: integrate(x*cos(x),x)==x*cos(x)+C
show("(MCQ choice B) T/F: integrate(x*cos(x),x)==x*cos(x)+C")
show(integrate(x*cos(x),x))
show(bool(integrate(x*cos(x),x)==x*cos(x)))
show("")

#4c) (MCQ choice C) T/F: integrate(x*cos(x),x)==x*sin(x)-cos(x)+C
show("(MCQ choice C) T/F: integrate(x*cos(x),x)==x*sin(x)-cos(x)+C")
show(integrate(x*cos(x),x))
show(bool(integrate(x*cos(x),x)==x*sin(x)-cos(x)))
show("")

#4d) (MCQ choice D) T/F: integrate(x*cos(x),x)==x*sin(x)+cos(x)+C
show("(MCQ choice D) T/F: integrate(x*cos(x),x)==x*sin(x)+cos(x)+C")
show(integrate(x*cos(x),x))
show(bool(integrate(x*cos(x),x)==x*sin(x)+cos(x)))