#MrG 2018.1017 pre506 Compound Interest
show("#1) P=$1000, r=10%, t=1yr find simple interest")
I=1000*.10*1
show(I)
show("#2) P=$1000, r=10%, t=1yr find interest compounded twice in one year")
I1=(1000)*(.10)*(1/2)
I2=(1000+I1)*(.10)*1/2
show(I1)
show(I2)
show(I1+I2)
show("#3) P=$1000, r=10%, t=1yr find interest compounded 4 times in one year")
I1=(1000)*(.10)*(1/4)
I2=(1000+I1)*(.10)*1/4
I3=(1000+I1+I2)*(.10)*1/4
I4=(1000+I1+I2+I3)*(.10)*1/4
show(I1)
show(I2)
show(I3)
show(I4)
show(I1+I2+I3+I4)
show("#4) Limit?")
show(1000*(1+.1/1)^1)
show(1000*(1+.1/2)^2)
show(1000*(1+.1/3)^3)
show(1000*(1+.1/4)^4)
show(1000*(1+.1/12)^12)
show(1000*(1+.1/360)^360)
show(1000*(1+.1/36000)^36000)
show(1000*e^(.1))
show("#11 p336) Discretely Compounded")
var('p')
show(solve(100==p*(1+.06/12)^24,p)[0].rhs().n(digits=4))
show("#9 p336) Continuously Compounded")
show(100*e^(.1*2.25).n(digits=5))
show("#29a) Doubling Time")
show((ln(2)/12/ln(1+.08/12)).n(digits=4))
show("#29b) Doubling Time")
show((ln(2)/.08).n(digits=4))
show("#21 p336)")
show((1+.0525/4)^4-1)
show(100*((1+.0525/4)^4-1))
