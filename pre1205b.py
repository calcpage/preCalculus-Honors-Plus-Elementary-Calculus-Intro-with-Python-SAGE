#factorial
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
print "n\tn!"
for n in range(7):
    print n,"\t",fact(n)
#pascal
def pascal(n,r):
    return fact(n)/fact(r)/fact(n-r)
for n in range(13):
    show([pascal(n,r) for r in range(n+1)])