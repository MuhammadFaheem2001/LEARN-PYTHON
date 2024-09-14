# Array Spliting

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
res  = np.array_split(arr , 3)

print(res)



arr1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
res1 = np.array_split(arr1, 5)
print(res1)
print(res1[0])
print(res1[1])
print(res1[2])
print(res1[3])
print(res1[4])


# 2-D Array

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)



# Searching Array

sear = np.array([1,5,62,4,8])
search = np.where(sear == 62)
print(search)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)


arr3 = np.array([1,2,3,45,6,7,89,9])
y = np.searchsorted(arr3 , 3)
print(y)


arr4 = np.array([1,2,37,74,6,7])
y1 = np.sort(arr4)
print(y1)



arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))



arr = np.array([True, False, True])
print(np.sort(arr))



arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))



arra = np.array([1,66,88,44,1,2,5,7])       # Those value are signed as True will print else removed.
arra1 = [True , False, True, False, False , False, False, False]
res = arra[arra1]
print(res)



arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)




