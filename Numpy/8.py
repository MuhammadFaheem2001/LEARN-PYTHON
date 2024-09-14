# Numpy Ramdom Library

# Random number does NOT mean a different number every time. Random means something that can not be predicted logically.


from numpy import random

x = random.randint(100)
print(x)

y = random.rand()
print(y)


a = random.randint(100, size=5)
print(a)


b = random.randint(100, size=(4,3))
print(b)


c = random.rand(10)
print(c)


d = random.rand(4,3)
print(d)


e = random.choice([1,5,8,9,4,10])
print(e)


f = random.choice([10,1,2,5,97,42,5], size=(3,2))
print(f)


g = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(g)


h = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(h)


# A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
# The NumPy Random module provides two methods for this: shuffle() and permutation().


from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5,6])
random.shuffle(arr)

print(arr)



arr1 = np.array([1,2,3,7,5,9,7])
print(random.permutation(arr1))

