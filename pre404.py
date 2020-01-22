#MrG 2018.0924 pre404 What Is An InEquality?
show("#1) Solve inequality for x: x^2 <= 4*x+12")
show(solve(x^2==4*x+12,x))
show(plot([x^2,4*x+12],-10,10))
show(plot([x^2-4*x-12],-10,10))
show("")

show("#2) Solve inequality for x: x^4 > x")
show(solve(x^4==x,x))
show(plot([x^4,x],-1,2))
show(plot([x^4-x],-1,2))
show("")

show("#3) Solve inequality for x: (4*x+5)/(x+2) >= 3")
show(solve((4*x+5)/(x+2)==3,x))
show(plot([(4*x+5)/(x+2),3],xmin=-3,xmax=3,ymin=0,ymax=4))
show(plot([(4*x+5)/(x+2)-3],xmin=-3,xmax=3,ymin=0,ymax=4))