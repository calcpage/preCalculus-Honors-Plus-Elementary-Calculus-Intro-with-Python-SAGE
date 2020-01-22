#MrG 2018.1022 pre1201b What Is Recusrsion?
show("1) Fibonacci")
def fib(n):
    if(n==1 or n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)

N=range(1,20)
F=[fib(n) for n in N]
FN=zip(N,F)
show(N)
show(F)
show(FN)
show(plot(point(FN)))
[fib(n) for n in range(1,20)]