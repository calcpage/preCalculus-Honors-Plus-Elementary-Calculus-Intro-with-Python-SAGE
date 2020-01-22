#MrG 2015.0324 UNIT 204: Difference Quotients
show("#1) trig identities")
var('h')
show(cos(x+h).simplify_trig())
show(sin(x+h).simplify_trig())
show("")

show("#2) check your limits")
show(lim((cos(h)-1)/h,h=0))
show(lim(sin(h)/h,h=0))
show(lim((sin(x+h)-sin(x))/h,h=0))
show(lim((cos(x+h)-cos(x))/h,h=0))
show(lim((sqrt(x+h)-sqrt(x))/h,h=0))
