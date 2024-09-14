# NUMPY UFUNC

# ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.


# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.
# ufuncs also take additional arguments, like:
# where boolean array or condition defining where the operations should take place.
# dtype defining the return type of elements.
# out output array where the return value should be copied.

import numpy as np

# Without Numpy ufunc we use zip() method

x = [1,2,3,4,5,8]
y = [1,6,7,8,9,5]
z = []

for i,j in zip(x,y):
    z.append(i+j)

print(z)


# With numpy ufunc

a = [1,2,3,4,5,8]
b = [1,7,8,9,4,1]
c =  np.add(a,b)

print(c)


def myadd(d,c):
  return d+c

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(np.add))



if type(np.add)  == np.ufunc:
   print("Yes It was ufunc")
else:
   print("no")



# Arithmetic Operations in Numpy's Ufunc

e = [1,2,3,4,8]
f = [7,4,1,2,5]
g = np.add(e,f)
h = np.subtract(e,f)
i = np.multiply(e,f)
j = np.divide(e,f)
k = np.remainder(e,f)

print(g)
print(h)
print(i)
print(j)
print(k)


# Rounding Decimal
print("Rounding Decimal")

l = np.trunc(e)
m = np.round(f)
n = np.fix(f) 
o = np.floor(e)
p = np.ceil(e)

print(l)
print(m)
print(n)
print(o)
print(p)


# LOGS
print("LOGS")


q = np.arange(1,10)
r = np.arange(11,20)
s = np.arange(21,30)
t = np.arange(31,40)
u = np.arange(41,50)

print(np.log2(q))
print(np.log2(r))
print(np.log10(s))
print(np.log10(t))
print(np.log(u))


from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))


# Summation
print("Summation")

arr =  [1,2,3,4,5]
arr1 = [6,5,4,7,8]
res = np.add(arr, arr1)
res1 = np.sum([arr, arr1],axis=1)
print(res)
print(res1)




arr2 = np.array([1, 2, 3])
newarr = np.cumsum(arr2)
print(newarr)




