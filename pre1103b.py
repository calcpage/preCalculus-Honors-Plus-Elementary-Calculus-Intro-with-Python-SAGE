#2) solve for (x,y): 2*x-y==2, 6*x+8*y==39
#2) new way!
a=matrix(QQ,2,2,[(2,-1),(6,8)]);show(a)
b=matrix(QQ,2,1,[2,39]);show(b)
c=a.augment(b,subdivide=True);show(c)
c.rescale_row(0,1/2);show(c)
c.add_multiple_of_row(1,0,-6);show(c)
c.rescale_row(1,1/11);show(c)
c.add_multiple_of_row(0,1,1/2);show(c)

