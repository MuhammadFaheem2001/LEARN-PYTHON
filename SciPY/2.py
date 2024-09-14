# OPTIMIZER


# Optimizers are a set of procedures defined in SciPy that either find the minimum value of a function, 
# or the root of an equation.



# This function takes two required arguments:

# fun - a function representing an equation.
# x0 - an initial guess for the root.


from scipy.optimize import root
from math import cos


def equ(x):
    return x + cos(x)

myroot = root(equ, 5)
print(myroot.x)
print(myroot)

from scipy.optimize._minimize import minimize

def eqn(x):
    return x**2 + x + 1

mymin = minimize(eqn, 2, method="BFGS")
print(mymin)



# SPARSE

# Sparse data is data that has mostly unused elements (elements that don't carry any information ).
# It can be an array like this one:
# [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]
# Sparse Data: is a data set where most of the item values are zero.
# Dense Array: is the opposite of a sparse array: most of the values are not zero.


from scipy.sparse import csr_matrix
from scipy.sparse import csc_matrix
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])
print(csr_matrix(arr))


arr1 = np.array([0,0,0,0,2,3,4,0,0,7,1,0,0])
print(csr_matrix(arr1))


arr2 = np.array([0,0,0,0,0,0,0,2,2,2,2,3,3,3,3])
print(csc_matrix(arr2)) # both will count the non-zeros values and give their path



arr3 = np.array([[0,0,0,0,1,2],[1,2,3,0,0,0],[1,0,2,0,0,5]])
print(csr_matrix(arr3).data)
print(csr_matrix(arr3).count_nonzero())




arr4 = np.array([[0,0,0,0,1,2],[1,2,3,0,0,0],[1,0,2,0,0,5]])
var1 = csr_matrix(arr4)
# var1.eliminate_zeros()
var1.sum_duplicates()
print(var1)



arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newarr = csr_matrix(arr).tocsc()        # convert the csr to csc 
print(newarr)


