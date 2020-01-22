#MrG 2018.0924 pre403: How To Find Complex Roots
show("#1) Find a polynomial equation of degree 5 with roots {1,5i,1+i,?,?}")
#1) ANS: roots are {1,5i,1+i,-5i,1-i}
#1) ANS: factors are (x-1)*(x-5*i)*(x-(1+i))*(x+5*i)*(x-(1-i))
show(expand((x-5*i)*(x+5*i)))
show(expand((x-(1+i))*(x-(1-i))))
show(expand((x-1)*(x^2+25)))
show(expand((x^2-2*x+2)*(x^3-x^2+25*x-25)))
show(factor(x^5-3*x^4+29*x^3-77*x^2+100*x-50))
show(solve(x^5-3*x^4+29*x^3-77*x^2+100*x-50,x))
plot(x^5-3*x^4+29*x^3-77*x^2+100*x-50,-2,2)
