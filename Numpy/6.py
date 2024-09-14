# Array Concatenation

# Joining means putting contents of two or more arrays in a single array.


import numpy as np

arr0 = np.array([1,2,3])
arr1 = np.array([4,5,6])
res = np.concatenate((arr0, arr1))

print(res)




arr3 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr3, arr2), axis=1)

print(arr)



arr4 = np.array([1,2,3])
arr5 = np.array([4,5,6])
res1 = np.stack((arr4, arr5), axis=1)

print(res1)

# Stacking Along Rows
# Prints the values in row

arr6 = np.array([1,2,3])
arr7 = np.array([7,8,9])
res2 = np.hstack((arr6, arr7), axis = 1)

print(res2)

# Stacking Along Columns
# vstack prints in columns

arr8 = np.array([1,2,3])
arr9 = np.array([9,8,7])
res3 = np.vstack((arr8, arr9), axis = 1)

print(res3)

# Stacking Along Height (depth):
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.


arr10 = np.array([1,2,3])
arr11 = np.array([9,8,7])
res4 = np.dstack((arr10, arr11), axis = 1)

print(res4)



