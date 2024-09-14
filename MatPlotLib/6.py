# GRAPH BARS

import matplotlib.pyplot as mt
import numpy as np

x=np.array([1,2,5,8,5,4])
y=np.array([9,8,41,12,8,7])

mt.bar(x,y)
mt.show()



x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

mt.bar(x,y)
mt.show()




x = np.array(["A","B","C","D","E"])
y = np.array([40,100,60,5,20])

# mt.barh(x,y)
mt.bar(x,y, color="r", width=1.5, height=0.1)
mt.show()



# Histogram


x = np.random.normal(100, 10 , 250)    # first row , second column , third values
# print(x)

mt.hist(x)
mt.show()



# Pie Chart


x = np.array([1,2,3,8,7,5,2,2,1,7,55])
mt.pie(x)
mt.show() 



x = np.array([10,30,55])
mylabel= np.array(["Apple", "Banana", "Mangoes"])


mt.pie(x, labels=mylabel , startangle=45)
mt.show() 




x = np.array([10,30,55])
mylabel= np.array(["Apple", "Banana", "Mangoes"])
myexplode = np.array([0.2,0.5,0.9])
micolor  = np.array([55,22,66])

mt.pie(x, c=micolor ,labels=mylabel , startangle=45 , explode=myexplode , shadow=True)
mt.show() 



y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

mt.pie(y, labels = mylabels)
mt.legend()
mt.show() 



y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]


mt.pie(y, labels = mylabels)
mt.legend(title = "Four Fruits:")
mt.show()








