#MrG 2018.1022 pre1201a Intro To Sequences
show("#1) finite sequence")
a(n)=(n-1)/n
show(a(n))
print "n\ta(n)\ta(n).n()"
for n in range(1,9):
    print n,"\t",a(n),"\t",a(n).n()
show("")
show("#2) infinite series")
show(sum([a(n).n() for n in range(1,5)]))
show(sum([a(n).n() for n in range(1,50)]))
show(sum([a(n).n() for n in range(1,500)]))
show(sum([a(n).n() for n in range(1,5000)]))
show(sum([a(n).n() for n in range(1,50000)]))
show("")
show("#3) graph of the sequence")
N=range(1,100)
A=[a(n) for n in N]
NA=zip(N,A)
plot(point(NA))