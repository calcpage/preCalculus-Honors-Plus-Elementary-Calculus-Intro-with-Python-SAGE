#MrG 2018.1009 UNIT405 What Is Newton's Method?
show("#1) use Newton's Method to find a better guess:")
show("#1) f(x) = x^2 - 2, first guess is x=2, next guess?")
f(x) = x^2 - 2
g(x)=diff(f(x),x)
show(f(x))
show(g(x))
show(f(2))
show(g(2))
show(solve(4*(x-2)+2==0,x))
show(plot([f(x),4*(x-2)+2],0,4))
