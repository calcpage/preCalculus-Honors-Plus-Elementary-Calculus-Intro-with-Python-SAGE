#1) MRG 2015.0511 LRTE with GUI input! 
@interact 
def lrte(f=x^2,a=1,b=5,n=slider(1,1000,1,4),method=selector(['Left','Right','Trap']),fillIt=('fill',False)): 
    p=Graphics() 
    h=(b-a)/n 
    if method=='Left': 
        l=sum([f(a+i*h)*h for i in range(n)]) 
        for i in range(n): 
            x=a+i*h 
            y=f(a+i*h) 
            p+=polygon([(x,0),(x,y),(x+h,y),(x+h,0)],fill=fillIt) 
        p+=plot(f,a,b,color='red',fill=True) 
        p.show() 
        print "l=" 
        print l.n(digits=6) 
    if method=='Right': 
        l=sum([f(a+i*h)*h for i in range(n)]) 
        r=l-f(a)*h+f(b)*h 
        for i in range(n): 
            x=a+i*h 
            y=f(a+(i+1)*h) 
            p+=polygon([(x,0),(x,y),(x+h,y),(x+h,0)],fill=fillIt) 
        p+=plot(f,a,b,color='red',fill=True) 
        p.show() 
        print "[l,r]=" 
        print [l.n(digits=6),r.n(digits=6)] 
    if method=='Trap': 
        l=sum([f(a+i*h)*h for i in range(n)]) 
        r=sum([f(a+i*h)*h for i in range(n)])-f(a)*h+f(b)*h 
        t=(r+l)/2 
        e=(r-l)/2 
        for i in range(n): 
            x=a+i*h 
            y1=f(a+i*h) 
            y2=f(a+(i+1)*h) 
            p+=polygon([(x,0),(x,y1),(x+h,y2),(x+h,0)],fill=fillIt) 
        p+=plot(f,a,b,color='red',fill=True) 
        p.show() 
        print "[l,r,t,e]=" 
        print [l.n(digits=6),r.n(digits=6),t.n(digits=6),e.n(digits=6)] 