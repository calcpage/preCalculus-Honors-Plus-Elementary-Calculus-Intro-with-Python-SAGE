#MrG 2018.1023 pre1202a What's An Arithmetic Sequence?
show("#1) a(n)=100-2*n")
a(n)=100-2*n
show([a(n) for n in range(30)])
show(sum([a(n) for n in range(30)]))
N=range(30)
A=[a(n) for n in range(30)]
show(N)
show(A)
AN=zip(N,A)
show(AN)
plot(point(AN))
