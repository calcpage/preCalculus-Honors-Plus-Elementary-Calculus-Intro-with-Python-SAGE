#1) vector [2,3]
v=vector([2,3])
show(v)
show(plot(v))
#2) vector [3,-4]
w=vector([3,-4])
show(w)
show(plot(w))
#3) v+w
s=v+w
show(s)
show(plot(s))
#4) v-w
d=v-w
show(d)
show(plot(d))
#5) plot together
pv=plot(v)
pw=plot(w)
ps=plot(s,color='red')
pd=plot(d,color='green')
show(pv+pw+ps+pd,aspect_ratio=1)
#6)
u=3*v
pu=plot(u)
show(pv+pu)
show(abs(v))
show(abs(u))