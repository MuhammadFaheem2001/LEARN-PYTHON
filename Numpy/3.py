# DATA TYPES 

# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j

# Code Start's From Here:

# Checking the Data Type using keyword dtype():

import numpy as np 

arr = np.array([1,2,3,4,5,6])
arr1 = np.array([True , False , True])
arr2 = np.array([1.1, 3.3, 3.25 ,4.5])
arr3 = np.array([3j , 5j , "Faheem"])
print(arr.dtype)
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)


# We can also define the type of element or variable

arr4 = np.array([1,2,3,4,5] , dtype = "S2")
print(arr4.dtype)

arr5 = np.array([1,2,3,4,5,5])
newarr = arr5.astype(float)
print(newarr.dtype)