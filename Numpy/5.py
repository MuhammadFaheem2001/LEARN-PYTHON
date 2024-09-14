# Array Iterating


# Iterating means going through elements one by one.
# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
# If we iterate on a 1-D array it will go through each element one by one.


# CODE


import numpy as np

arr = np.array([1,2,2,3,4,5,6])

for x in arr:
    print(x)



arr1 = np.array([[1,2,3,4,5,6],[10,11,12,13,14,15]])

for x in arr1:
    print(x)



arr2 = np.array([[1,2,3,4,5,6],[10,11,12,13,14,15]])

for x in arr2:
    for y in x:
        print(y)

        


arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])

for z in arr3:
    print(z)
    print(z.ndim)



arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr4:
  print(x)



arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr5:
  for y in x:
    for z in y:
      print(z)




arr6 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in np.nditer(arr6):
   print(x)




arr7 = np.array([1,2,3])

for n in np.nditer(arr7, flags=["buffered"], op_dtypes="S"):
   print(n)




arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)