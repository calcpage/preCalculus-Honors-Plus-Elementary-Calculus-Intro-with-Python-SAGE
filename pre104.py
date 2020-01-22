#MrG 2018.0823 pre104 Modeling with Equations
#15 p45) The perimeter of a rectangle is 60 feet. 
#15 p45) If the length is 8 feet longer than the width, calculate the length and width.
show("#15 p45) The perimeter of a rectangle is 60 feet.")
show("#15 p45) If the length is 8 feet longer than the width, calculate the length and width.")
show(solve(2*x+2*(x+8)==60,x))
show("")

#19 p45) You have test grades: 86,80,84,90. The final counts 2/3 of your average.
#19 p45) What must you score on the final to get a 90 average?
show("#19 p45) You have test grades: 86,80,84,90. The final counts 2/3 of your average.")
show("#19 p45) What must you score on the final to get a 90 average?")
show(solve((86+80+84+90+8*x)/12==90,x)[0].rhs().n())
show("")

#23 p45) You have $50000 to invest. Bond A has a 15% return, Bond B has a 7% return per year.
#23 p45) How much should you invest in each Bond in order to get $6000 return per year?
show("#23 p45) You have $50000 to invest. Bond A has a 15% return, Bond B has a 7% return per year.")
show("#23 p45) How much should you invest in each Bond in order to get $6000 return per year?")
show(solve(0.15*x+0.07*(50000-x)==6000,x))
show("")

#29 p45) You sell peanuts at $1.50/lb and pashews at $4/lb.
#29 p45) You want to mix 60 pounds of peanuts with x pounds of cashews and sell the mix at $2.50/lb.
#29 p45) How many pounds x of cashews do you need?
show("#29 p45) You sell peanuts at $1.50/lb and pashews at $4/lb.")
show("#29 p45) You want to mix 60 pounds of peanuts with x pounds of cashews and sell the mix at $2.50/lb.")
show("#29 p45) How many pounds x of cashews do you need?")
show(solve(1.5*60+4*x==(60+x)*2.5,x))
show("")

#33 p45) Train A leaves the station at 12 noon. Train B leaves the station at 2pm traveling 50 mph faster.
#33 p45) The trains collide at 4pm. How fast were the trains traveling given they were traveling in the same direction?
show("#33 p45) Train A leaves the station at 12 noon. Train B leaves the station at 2pm traveling 50 mph faster.")
show("#33 p45) The trains collide at 4pm. How fast were the trains traveling given they were traveling in the same direction?")
show(solve(4*x==2*(x+50),x))
show("")