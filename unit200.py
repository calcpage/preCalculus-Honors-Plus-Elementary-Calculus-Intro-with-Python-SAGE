#1)Pythagorean Trig Identities
f(x)=sin(x)^2+cos(x)^2
show(f(x))
show(f(x).simplify_trig())
show(plot(f(x)))
g(x)=f(x)/cos(x)^2
show(g(x))
show(g(x).simplify_trig())
show(plot(g(x)))
h(x)=f(x)/sin(x)^2
show(h(x))
show(h(x).simplify_trig())
show(plot(h(x)))
#2)Sum and Diff of 2 Angles Trig Identities
var('y')
f(x)=sin(x+y)
show(f(x))
show(f(x).simplify_trig())
show(plot3d(f(x),(x,-1,1),(y,-1,1), frame=True, color='red', opacity=0.8))
f(x)=sin(x-y)
show(f(x))
show(f(x).simplify_trig())
show(plot3d(f(x),(x,-1,1),(y,-1,1), frame=True, color='green', opacity=0.8))
f(x)=cos(x+y)
show(f(x))
show(f(x).simplify_trig())
show(plot3d(f(x),(x,-1,1),(y,-1,1), frame=True, color='purple', opacity=0.8))
f(x)=cos(x-y)
show(f(x))
show(f(x).simplify_trig())
show(plot3d(f(x),(x,-1,1),(y,-1,1), frame=True, color='blue', opacity=0.8))
#3)Double Angle Trig Identities
f(x)=(1+cos(2*x))/2
show(f(x))
show(f(x).simplify_trig())
show(plot(f(x)))
f(x)=(1-cos(2*x))/2
show(f(x))
show(f(x).simplify_trig())
show(plot(f(x)))