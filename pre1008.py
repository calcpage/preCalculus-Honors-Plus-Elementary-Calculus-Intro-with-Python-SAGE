#MrG 2018.0323 1008 Review Ellipses & Hyperbolas!
#69) p660
show("Finding Planet Orbits")
var('a,b,p,y')
c=23.2
ap=507
show(solve(ap==a+c,a))
show(solve(ap==a+c,a)[0].rhs().n())
a=solve(ap==a+c,a)[0].rhs()
show(solve(a==(ap+p)/2,p))
show(solve(a==(ap+p)/2,p)[0].rhs().n())
show(solve(b^2+c^2==a^2,b))
show(solve(b^2+c^2==a^2,b)[1].rhs().n())
b=solve(b^2+c^2==a^2,b)[1].rhs()
print(solve(x^2/a^2+y^2/b^2==1,y))
show(plot([-91/2419*sqrt(-705*x^2 + 825070101/5),91/2419*sqrt(-705*x^2 + 825070101/5)],-a,a,aspect_ratio=1))
show("")

#57) p674
show("LORAN: LOng RAnge Navigation")
var('a,b')
t=0.00038
c=186000
d=t*c
show(d)
show(solve(2*a==d,a))
show(solve(2*a==d,a)[0].rhs().n())
a=solve(2*a==d,a)[0].rhs()
c=100
show(solve(a^2+b^2==c^2,b))
show(solve(a^2+b^2==c^2,b)[1].rhs().n())
b=solve(a^2+b^2==c^2,b)[1].rhs()
print(solve(x^2/a^2-y^2/b^2==1,y))
f(x)=1/88350*sqrt(54694277500*x^2 - 68308536400479)
show(f(50))
show(f(50).n())
p1=plot([-1/88350*sqrt(54694277500*x^2 - 68308536400479),1/88350*sqrt(54694277500*x^2 - 68308536400479)],-2*a,-a)
p2=plot([-1/88350*sqrt(54694277500*x^2 - 68308536400479),1/88350*sqrt(54694277500*x^2 - 68308536400479)],a,2*a)
show(p1+p2,aspect_ratio=1)