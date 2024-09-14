# Numpy Tutorial Starts From Here

# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
# NumPy stands for Numerical Python.


# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
# Arrays are very frequently used in data science, where speed and resources are very important.

# Data Science: is a branch of computer science where we study how to store, use and analyze 
# data for deriving information from it.

# stpes of data Science
# collect , analyze , process

# Code



import numpy as np 

arr = np.array([1,2,3,4,5])

print(arr)
print(type(arr))
print(np.__version__)


# Using tuple for array

arr1 = np.array((1,2,8,4,6,2))

print(arr1)
print(type(arr1))
print(len(arr1))


# 0-D Array

arr2 = np.array(45)
print(arr2)

# 1-D Array

arr3 = np.array((1,2,5,5))
print(arr3)

# 2-D Array

arr4 = np.array([[1,2,3],[6,8,9]])
print(arr4)

# 3-D Array

arr5 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr5)


# Checking Dimensions

array0 = np.array(56)
array1 = np.array([1,2,3])
array2 = np.array([[1,2,3],[4,5,6]])
array3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print(array0.ndim)  # ndim will check the dimension of array and tell us about the dimension 
print(array1.ndim)  # whether it was 0-d array to 3-d array
print(array2.ndim)
print(array3.ndim)


# We can also write the dimensions as we wish
# It was a 2-d array and we are going to add dimension using ndim

array4 = np.array([[1,2,3],[4,5,6]] , ndmin = 5)
print(array4)
print(array4.ndim)
print("Total Dimension Of Array are: " , array4.ndim)



# Indexing or Slicing Of Array

arr6 = np.array([1,2,3])
print(arr6[0])
print(arr6[1])
print(arr6[2])
print(arr6)


# Array Sum

res = arr6[0] + arr6[2]
print(res) 


# 2-D Array

arr7 = np.array([[1,2,3,4,5],[6,5,4,1,2]])
print(arr7)
print(arr7[0, 2]) # It will show the 3nd element of 1st Array
print(arr7[1, 0]) # It will show the 1nd element of 2nd Array



arr8 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr8)
print(arr8[0,0,1]) # 0 represent the array [[1,2,3],[4,5,6]] and second represent the array [1,2,3] and third get the value which is 1 = 2


arr9 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr9[1, -1])           # It will print 10 from second dimension
print('Second Last element from 1nd dim: ', arr9[0, -2])    # It will print the second last of First dimension




