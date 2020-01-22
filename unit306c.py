#MrG 2018.0510 UNIT306c: What Are Related Rates?
#21a) p256: Find x' given z^2=x^2+36 the moment z=10ft and z'=-2ft/s
#21a) p256: Given a right triangle with hypotenuse z and base x. The height y=6ft is constant.
show("Find x' given z^2=x^2+36 the moment z=10ft and z'=-2ft/s")
show('Given a right triangle with hypotenuse z and base x. The height y=6ft is constant.')
var('t,xp')
x=function('x')(t)
z=function('z')(t)
show(diff(z^2-x^2-36,t))
show(solve(-2*8*xp+2*10*-2==0,xp))
show("")