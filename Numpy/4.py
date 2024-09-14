# COPY AND VIEW

# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

# NOTED
# As simply copy can change the data
# And View cannot change the data we can just see the data


# Code Start's From Here

import numpy as np

arr = np.array(["Muhammad", "Faheem" , 22 , 4])
x = arr.copy()
y = arr.view()
arr[1]  = "Shahid"

print(arr) # UPDATED ARRAY
print(x)   # COPIED ARRAY
print(y)   # VIEWED MEANS WE CAN JUST SEE THE ORIGNAL ARRAY


arr1 = np.array([1,2,3,4,56,7])
z = arr1.view() 
z[0] = 20  

print(arr1) # And View Can Change the value of both Arrays
print(z)


# Base Keyword

arr2 = np.array([1,2,3,4,56,7,8])

a = arr2.copy()
b = arr2.view()

# The copy returns None.
# The view returns the original array.

print(a.base)      # DOES NOT OWN THE DATA OF ARRAY
print(b.base)   # OWNS THE DATA OF ARRAY


# Array Shape

# The shape of an array is the number of elements in each dimension.


arr3 = np.array([1,2,3,45,67,8])
print(arr3.shape)
print(arr3.reshape(2,3))


# 2-D Array 

arr4 = np.array([[1,2,3,4,5],[6,7,8,9,10]]) # output is (2,5) 2 is Array 5 is Array Elements
print(arr4.shape)
print(arr4.reshape(2,3))



arr5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr1 = arr5.reshape(4, 3)
print(newarr1)



arr6 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr2 = arr6.reshape(2, 3, 2)
print(newarr2)





