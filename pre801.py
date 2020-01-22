#MrG  2015.1001  SOHCAHTOA
#29) solve the right triangle:
#29) C=90 degrees, B=20 degrees, b=5
#29) Find a
show(solve(tan(20)==5/x,x))
show(solve(tan(20)==5/x,x)[0])
show(solve(tan(20)==5/x,x)[0].rhs())
show(solve(tan(20*pi/180)==5/x,x)[0].rhs().n())
#35) solve the right triangle
#35) C=90 degrees, a=5, b=3
#35) Find B, A and c
show((arctan(3/5)*180/pi).n())
show(90-(arctan(3/5)*180/pi).n())
show(sqrt(5^2+3^2))
show(sqrt(5^2+3^2).n())