# Module

import MyModule
# from MyModule import person1
import MyModule as MM

a = MyModule.person1["country"]
b = MM.person1
print(a)
print(b)


# Date and Time


import datetime as date

dt = date.datetime.now()
print(dt)



# MATH MODULE


import math

a = min(10, 15 , 50)
b = max(25, -5, 60)
c = abs(80)
d = math.factorial(10)
e = math.cos(45)
g = math.pow(5, 2)
f = math.sqrt(64)
h = math.pi

print(a , b , c , d , e , g, f , h)



