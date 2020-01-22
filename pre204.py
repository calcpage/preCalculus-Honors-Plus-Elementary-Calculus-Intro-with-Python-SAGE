#MrG 2018.0823 pre204 Transformations
#1) Compare f(x) to f(x)+1,f(x)-1,f(x)+2,f(x)-2.
show("#1) Compare f(x) to f(x)+1,f(x)-1,f(x)+2,f(x)-2.")
f(x)=x^2
plot([f(x),f(x)+1,f(x)-1,f(x)+2,f(x)-2])
show("")

#2) Compare f(x) to f(x+1),f(x-2),f(x+3),f(x-4).
show("#2) Compare f(x) to f(x+1),f(x-2),f(x+3),f(x-4).")
f(x)=x^3
plot([f(x),f(x+1),f(x-2),f(x+3),f(x-4)],xmin=-5,xmax=5,ymin=-10,ymax=10)
show("")

#3) Compare f(x) to f(x)*2,f(x)/2,f(x)*3,f(x)/3.
show("#3) Compare f(x) to f(x)*2,f(x)/2,f(x)*3,f(x)/3.")
f(x)=abs(x)
plot([f(x),f(x)*2,f(x)/2,f(x)*3,f(x)/3])
show("")

#4) Compare f(x) to f(2*x),f(x/2),f(3*x),f(x/3).
show("#4) Compare f(x) to f(2*x),f(x/2),f(3*x),f(x/3).")
f(x)=abs(x)
plot([f(x),f(2*x),f(x/2),f(3*x),f(x/3)])
show("")

#5) graph f(x)=(x+3)^2-5
show("#5) graph f(x)=(x+3)^2-5")
plot((x+3)^2-5,-6,6)
show("")

#6) graph f(x)=3/(x-2)+1
show("#6) graph f(x)=3/(x-2)+1")
plot(3/(x-2)+1,xmin=-6,xmax=6,ymin=-10,ymax=10)
show("")

#7) graph f(x)=sqrt(1-x)+2
show("#7) graph f(x)=sqrt(1-x)+2")
plot(sqrt(1-x)+2,-4,1)