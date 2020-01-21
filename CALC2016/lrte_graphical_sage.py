#MrG 2015.0507 LRTE + Graphics
f="1/x"
a=1
b=2
n=10

def lSum(f,a,b,n):
    p=Graphics()
    h=(b-a)/n
    for i in range(n):
        x=a+i*h
        y=f(a+i*h)
        p+=polygon([(x,0),(x,y),(x+h,y),(x+h,0)],fill=False)
    p+=plot(f,a,b,color='red',fill=True)
    p.show(aspect_ratio=1)
    return sum([f(a+i*h)*h for i in range(n)])

def rSum(f,a,b,n):
    p=Graphics()
    h=(b-a)/n
    for i in range(n):
        x=a+i*h
        y=f(a+i*h+h)
        p+=polygon([(x,0),(x,y),(x+h,y),(x+h,0)],fill=False)
    p+=plot(f,a,b,color='red',fill=True)
    p.show(aspect_ratio=1)
    return sum([f(a+i*h)*h for i in range(n)])-f(a)*h+f(b)*h

def tSum(f,a,b,n):
    p=Graphics()
    h=(b-a)/n
    for i in range(n):
        x=a+i*h
        y1=f(a+i*h)
        y2=f(a+i*h+h)
        p+=polygon([(x,0),(x,y1),(x+h,y2),(x+h,0)],fill=False)
    p+=plot(f,a,b,color='red',fill=True)
    p.show(aspect_ratio=1)
    l=sum([f(a+i*h)*h for i in range(n)]).n(digits=6)
    r=sum([f(a+i*h)*h for i in range(n)])-f(a)*h+f(b)*h
    return [(r+l)/2,(r-l)/2]

print "l=",lSum(lambda x:eval(f),a,b,n).n(digits=6)
print "r=",rSum(lambda x:eval(f),a,b,n).n(digits=6)
print "[t,e]=",tSum(lambda x:eval(f),a,b,n)
