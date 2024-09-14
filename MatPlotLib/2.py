# LINES

# lineStyle = "dotted" "dashed" "Solid" "None" 
# as alias we can use linestyle = ls 
# Linecolor = color = "r,g,b,c,b,w"

import numpy as np
import matplotlib.pyplot as mt

# xaxis = np.arange(8)
xaxis = np.array([1,5,9,12,15,30])

mt.plot(xaxis , mec = "r" , mfc = "r" , marker="o", linestyle="dotted" , ls=':') # linestyle and ls both are same
mt.show()


xaxis1 = np.array([1,5,9,12,15,30])

mt.plot(xaxis1 , color="hotpink", linestyle="solid", linewidth=10)
mt.show()



x= np.array([1,2,3,8,4,1])
y= np.array([2,3,4,5,8,9])

mt.plot(x)
mt.plot(y)

mt.show()



x1= np.array([1,2,3,8,4,1])
y1= np.array([2,3,4,5,8,9])

x2 = np.array([10,9,8,7,6])
y2 = np.array([5,4,3,2,1])


mt.plot(x1,y1, x2,y2)
mt.show()



x = np.array([1,8,9,2,5])
y = np.array([0,2,3,4,8])

mt.plot(x,y)

mt.title("Random_Chart" ,loc="right")
mt.xlabel("Random1")
mt.ylabel("Random2")

mt.show()





x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

mt.title("Sports Watch Data", fontdict = font1)
mt.xlabel("Average Pulse", fontdict = font2)
mt.ylabel("Calorie Burnage", fontdict = font2)

mt.plot(x, y)
mt.show()
