# Array Slicing

# Slicing in python means taking elements from one given index to another given index.
# We pass slice instead of index like this: [start:end].
# We can also define the step, like this: [start:end:step].
# If we don't pass start its considered 0
# If we don't pass end its considered length of array in that dimension
# If we don't pass step its considered 1

# Code Start's From Here

import numpy as np 

arr = np.array([1,2,3,4,5])
print(arr[1:4]) # Start: End
print(arr[:4])
print(arr[3:])
print(arr[-3:-1])


print(arr[0:4:2]) # Start : End : Step (Gap)
print(arr[::2]) 


# 2-D Array

arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr1[0, 1:3])     # First 0 is Array and second is Start : End
print(arr1[1, -1])      
print(arr1[0, 1:3:2])   # Array 1(0) start from 1(2) end in 3(3) step 2 out of box So it will print 2



arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2[0:2, 2])     #   It will take the 2 element from both Arrays 


arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr3[0:2, 1:4])


