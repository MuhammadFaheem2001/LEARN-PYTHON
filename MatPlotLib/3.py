# MATPLOTLIB GRID VIEW

import matplotlib.pyplot as mt
import numpy as np

x = np.array([1,2,6,4,8])
y = np.array([6,8,4,2,3])

mt.title("Grid View", loc="left")
mt.xlabel("Random_1")
mt.ylabel("Random_2")

mt.plot(x,y, "o:r")
mt.grid()           # This grid keyword show the grid view
mt.show()



x1 = np.array([1,2,6,4,8])
y1 = np.array([6,8,4,2,3])

mt.title("Grid View")
mt.xlabel("Random_1")
mt.ylabel("Random_2")

mt.plot(x1,y1, "o:r")
# mt.grid(axis="y")
mt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
mt.show()



