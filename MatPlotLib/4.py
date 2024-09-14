# SUBPLOT

# With the subplot() function you can draw multiple plots in one figure:


import matplotlib.pyplot as mt
import numpy as np

x = np.array([1,2,6,4,8])
y = np.array([6,8,4,2,3])

mt.subplot(1,2,1)   #1 is row, 2 is column , 3rd (1) is graph 1

mt.title("Graph_1")
mt.xlabel("X-AXIS")
mt.ylabel("Y-AXIS")
mt.grid()
mt.plot(x,y)

# PLOT GRAPH 2 

x1 = np.array([1,6,8,4,2])
y1 = np.array([3,2,1,8,2])

mt.subplot(1,2,2)   # if we want to change position left-right to top-bottom we change row=2 and column=1

mt.title("Graph_2")
mt.xlabel("X1_AXIS")
mt.ylabel("Y1_AXIS")
mt.plot(x1,y1)

mt.grid()
mt.show()




# PLOT 6 GRAPH IN ONE PAGE

import matplotlib.pyplot as mt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

mt.subplot(2, 3, 1)
mt.plot(x,y)
mt.title("Shape")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

mt.subplot(2, 3, 2)
mt.plot(x,y)
mt.title("Wrong")

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

mt.subplot(2, 3, 3)
mt.plot(x,y)
mt.title("Right")


x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

mt.subplot(2, 3, 4)
mt.plot(x,y)
mt.title("TOP")

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

mt.subplot(2, 3, 5)
mt.plot(x,y)
mt.title("Left")

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

mt.subplot(2, 3, 6)
mt.plot(x,y)
mt.title("Bottom")

mt.show()


