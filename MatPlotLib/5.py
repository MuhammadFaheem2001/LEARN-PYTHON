# Scatters

import numpy as np
import matplotlib.pyplot as mt

x = np.array([2,1,3,5,7])
y = np.array([3,5,8,9,2])

mt.title("Scatters")
mt.xlabel("X-AXIS")
mt.ylabel("Y-AXIS")
mt.scatter(x,y)     # in scatter we get the dotted signs
mt.plot(x,y)        # in plot we get the proper lines a-b-c-d
mt.show()




#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
mt.scatter(x, y, color="c")

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
mt.scatter(x, y, color="r")

mt.show()



x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

mt.scatter(x, y, c=colors)
mt.show()





x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

mt.scatter(x, y, c=colors, cmap='viridis')
mt.colorbar()
mt.show()





x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

mt.scatter(x, y, s=sizes, alpha=1.5)
mt.show()



x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

mt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
mt.colorbar()
mt.show()





