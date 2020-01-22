#MrG  2015.1001  Law of Sines
#1) solve the AAS triangle:
#1) A=40 degrees, B=60 degrees, a=4
#1) Find b
show(solve(sin(40)/4==sin(60)/x,x))
show(solve(sin(40)/4==sin(60)/x,x)[0])
show(solve(sin(40)/4==sin(60)/x,x)[0].rhs())
show(solve(sin(40*pi/180)/4==sin(60*pi/180)/x,x)[0].rhs().n())
#2) solve the ASS triangle:
#2) A=35 degrees, a=6, b=8 (ambiguous case)
#2) Find B
show(solve(sin(35)/6==sin(x)/8,x))
show((arcsin(4*sin(35*pi/180)/3)*180/pi).n())