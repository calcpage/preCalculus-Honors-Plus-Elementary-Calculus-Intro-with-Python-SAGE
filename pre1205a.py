#Binomial Expansion Theorem!
show(expand((x+1)^0))
show(expand((x+1)^1))
show(expand((x+1)^2))
show(expand((x+1)^3))
show(expand((x+1)^4))
show(expand((x+1)^5))
show(expand((x+1)^6))
show(expand((x+1)^7))
#short hand!
show([expand((x+1)^n) for n in range(8)])
#long hand
for n in range(8):
    show(expand((x+1)^n))