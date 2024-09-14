# Product 
import numpy as np

arr = [1,2,3,4,8]
res = np.prod(arr)
print(res)


arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
res1 = np.prod([arr1, arr2], axis=1)
print(res1)


arr3 = [9,8,7,6,5]
arr4 = [5,4,3,2,1]
res2 = np.cumprod([arr3, arr4])
print(res2)


arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)



# Differences
print("Differences")


arr5 = [1,2,3,4,8]
arr6 = [7,5,6,1,2]
res3 = np.diff(arr5)
res4 = np.diff([arr6, arr5], n=2)

print(res3)
print(res4)


# LCM
print("LCM")

val1 = 56
val2 = 6
res5 = np.lcm(val1, val2)
print(res5)


val3 = np.array([1,2,3,4,5])
res6 = np.lcm.reduce(val3)
print(res6)


arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)



# GCD 
print("GCD")


num1 = 5
num2 = 155
res7 = np.gcd(num1,num2)

print(res7)


num3 = np.array([1,2,3,4,7])
res8 = np.gcd.reduce(num3)
print(res8)




# Trigonometric Functions
print("Trigonometric Functions")


import numpy as np

base = 3
perp = 4

x = np.hypot(base, perp)
print(x)



arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)


# Radian to Degree


arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)


arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)



x = np.sin(np.pi/2)
print(x)