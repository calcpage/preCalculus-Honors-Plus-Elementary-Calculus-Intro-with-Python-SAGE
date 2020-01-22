#to prove: 1+2+3+...+n=n*(1+n)/2
#you must show: n+1=(n+1)*(n+2)/2-n*(1+n)/2
var('n')
show((n+1)*(n+2)/2-n*(1+n)/2)
show(expand((n+1)*(n+2)/2-n*(1+n)/2))
show(bool(n+1==(n+1)*(n+2)/2-n*(1+n)/2))
#to prove: 3+5+7+...+2*n+1=n*(3+2*n+1)/2
#you must show: 2*n+3=(n+1)*(2*n+6)/2-n*(2*n+4)/2
var('n')
show((n+1)*(2*n+6)/2-n*(2*n+4)/2)
show(((n+1)*(2*n+6)/2-n*(2*n+4)/2).simplify_rational())
show(bool(2*n+3==(n+1)*(2*n+6)/2-n*(2*n+4)/2))