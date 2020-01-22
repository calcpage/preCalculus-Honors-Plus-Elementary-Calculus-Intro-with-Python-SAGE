#MrG 2018.1023 UNIT502 What Is A Differential Equation?
show("#84AB1a)")
a(t)=6*t+6
show(integrate(a(t),t))
var('A')
v(t)=3*t^2+6*t+A
show(solve(-9==v(0),A))
show("#84AB1c)")
v(t)=3*t^2+6*t-9
show(integrate(v(t),t))
var('B')
x(t)=t^3+3*t^2-9*t+B
show(solve(-27==x(0),B))