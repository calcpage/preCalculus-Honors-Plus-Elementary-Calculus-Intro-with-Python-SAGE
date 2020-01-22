#MrG 2015.0505 LRTE
f="x**2"
a=1
b=5
n=4000

def lSum(f,a,b,n):
    h=(b-a)/n
    return sum([f(a+i*h)*h for i in range(n)])
#show(lSum(lambda x: eval(f),a,b,n).n(digits=40))

def rSum(f,a,b,n):
    h=(b-a)/n
    return lSum(f,a,b,n)-f(a)*h+f(b)*h
#show(rSum(lambda x: eval(f),a,b,n).n(digits=40))

def tSum(f,a,b,n):
    return (rSum(f,a,b,n)+lSum(f,a,b,n))/2
#show(tSum(lambda x: eval(f),a,b,n).n(digits=40))

def tError(f,a,b,n):
    return (rSum(f,a,b,n)-lSum(f,a,b,n))/2
#show(tError(lambda x: eval(f),a,b,n).n(digits=40))

l=lSum(lambda x: eval(f),a,b,n).n(digits=6)
r=rSum(lambda x: eval(f),a,b,n).n(digits=6)
t=tSum(lambda x: eval(f),a,b,n).n(digits=6)
e=tError(lambda x: eval(f),a,b,n).n(digits=6)

print "n\tl\t\tr\t\tt\t\te"
print n,"\t",l,"\t",r,"\t",t,"\t",e