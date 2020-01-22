#MrG 2018.1023 pre1202b Some Algebra?
show("#52) p829")
show("#how many rows in a stadium with 2040 seats")
show("#and 10 seats in the first row, 14 seats in the next row...?")
show("#{10,14,18,22,...,4n+10} find n, n+1 is the number of rows!")
f(x)=2040
g(x)=(x+1)*(10+(4*x+10))/2
show(f(x))
show(g(x))
equ=f(x)==g(x)
show(equ)
equ=equ-2040
show(equ)
equ=expand(equ)
show(equ)
show(factor(equ.rhs()))
show(solve(equ,x))
plot([f(x),g(x)],-40,40)