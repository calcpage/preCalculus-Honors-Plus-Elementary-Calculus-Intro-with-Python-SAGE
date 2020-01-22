#MrG 2018.1012 UNIT407 What Is Newton's Method?
show("#1) write newton's method program to find roots of x^2-2==0")
f(x)=x^2-2
guess=1
def newt(guess):
    g(x)=diff(f(x),x)
    return guess-f(guess)/g(guess)
for i in range(6):
    guess = newt(guess)
    show(guess.n())
