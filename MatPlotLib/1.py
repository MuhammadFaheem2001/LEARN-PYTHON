# MATPLOTLIB

# Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
# Matplotlib was created by John D. Hunter.
# Matplotlib is open source and we can use it freely.

# Matplotlib is mostly written in python, a few segments are written in C, 
# Objective-C and Javascript for Platform compatibility.


import matplotlib.pyplot as mt
import numpy as np


xaxis = np.array([1,15])
yaxis = np.array([0,8])

mt.plot(xaxis, yaxis)
mt.show()




xaxis1 = np.array([1,15])
yaxis2 = np.array([0,8])

mt.plot(xaxis1, yaxis2, "o")        # O Represent the ring shape instead showing us the line from 0-8
mt.show()



xaxis3 = np.array([1, 2, 6, 8])
yaxis4 = np.array([3, 8, 1, 10])

mt.plot(xaxis3, yaxis4)
mt.show()



xaxis5 = np.array([1, 2, 6, 8,5,8,9])


mt.plot(xaxis5)     # If we dont specify the yaxis array then it will take random array
mt.show()


# MARKER



xaxis6 = np.array([1, 2, 6, 8,5,8,9])


mt.plot(xaxis6, marker="o")      # with marker value it will make o sign at the borders of Ploting.
mt.show()



# Marker	Description
# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline


# fmt format string marker|line|color

xaxis7 = np.array([1, 2, 6, 8,5,8,9])


mt.plot(xaxis7, "o:r", ms=10)      # we can change color and ploting sign like that o:color or van change marker size as ms=10
mt.show()

# marker size = ms=10 as you wish
# marker color = mec="r" red , green , blue , cyan, black , white
# marker face color = mfc = "g"



