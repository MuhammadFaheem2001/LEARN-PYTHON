# MATLAB

# The savemat() function allows us to export data in Matlab format.

# The method takes the following parameters:

# filename - the file name for saving data.
# mdict - a dictionary containing the data.
# do_compression - a boolean value that specifies whether to compress the result or not. Default False.


import numpy as np
from scipy import io

arr = np.arange(10)
io.savemat('arr.mat', {"vec": arr})

data = io.loadmat("arr.mat")
print(data)
print(data["vec"])  # to print array





# What is Interpolation?

# Interpolation is a method for generating points between given points.
# For example: for points 1 and 2, we may interpolate and find points 1.33 and 1.66.


import numpy as np 
from scipy.interpolate import interp1d

xs = np.arange(10)
ys = 2*xs + 1

func = interp1d(xs, ys)
newarr = func(np.arange(2.5,6.5,8.5))
print(newarr)



# Significance Test

import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)



import numpy as np
from scipy.stats import kstest

v = np.random.normal(size=100)

res = kstest(v, 'norm')

print(res)


import numpy as np
from scipy.stats import describe

v = np.random.normal(size=100)
res = describe(v)

print(res)



import numpy as np
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))



