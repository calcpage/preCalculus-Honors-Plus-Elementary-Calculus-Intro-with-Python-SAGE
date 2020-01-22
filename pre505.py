#MrG 2018.1015 pre505 Solving Equations!
show("#1) solve for x: 2*log5(x)==log5(9)")
show(solve(2*log(x)/log(5)==log(9)/log(5),x)[0].rhs().canonicalize_radical())
show(plot([2*log(x)/log(5),log(9)/log(5)],0.1,5))
show("#2) solve for x: log4(x+3)+log4(2-x)==1")
show(solve(log(x+3)/log(4)+log(2-x)/log(4)==1,x))
show(plot([log((x+3)*(2-x)),log(4)],-3,2))
show("#3) solve for x: 4^x-2^x-12==0")
equ=4^x-2^x-12==0
show(equ)
equ=equ.canonicalize_radical()
show(equ)
equ=factor(equ)
show(solve(equ,x)[1].rhs().canonicalize_radical())