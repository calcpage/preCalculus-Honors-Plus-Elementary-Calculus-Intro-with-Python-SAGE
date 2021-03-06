#9) p623 from (0,0,0) to (4,1,2)
v=vector([4,1,2])
show(v)
vp=plot(v)
show(vp, viewer='tachyon', aspect_ratio=1)
#23) p623 from (3,2,-1) to (5,6,0)
w=vector([2,4,1])
show(w)
wp=plot(w)
show(wp, viewer='tachyon', aspect_ratio=1)
#27) p623 magnitude of <3,-6,-2>
u=vector([3,-6,-2])
show(abs(u))
#33) p623 find 2*v+3*w if v=<3,-5,2> and w=<-2,3,2>
v=vector([3,-5,2])
w=vector([-2,3,2])
show(2*v)
show(3*w)
show(2*v+3*w)
vp=plot(2*v,color='red')
wp=plot(3*w,color='green')
sump=plot(2*v+3*w)
show(vp+wp+sump, viewer='tachyon', aspect_ratio=1)
#45) p6233 v.dot_product(w)==abs(v)*abs(w)*cos(t)
#45) p623 find t if v=<1,-1,0> and w=<1,1,1>
v=vector([1,-1,0])
w=vector([1,1,1])
d=v.dot_product(w)
show(d)
show(abs(v))
show(abs(w))
show(d/abs(v)/abs(w))
show(arccos(d/abs(v)/abs(w)))
show(arccos(d/abs(v)/abs(w))*180/pi)
vp=plot(v,color='red')
wp=plot(w,color='green')
show(vp+wp, viewer='tachyon', aspect_ratio=1)
