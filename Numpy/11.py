# Uniform Distribution

# Used to describe probability where every event has equal chances of occuring.

# E.g. Generation of random numbers.

# It has three parameters:

# a - lower bound - default 0 .0.
# b - upper bound - default 1.0.
# size - The shape of the returned array.



from numpy import random
import matplotlib.pyplot as mt
import seaborn as sb

x = random.uniform(size=(2,3))
print(x)


sb.distplot(random.uniform(size=1000), hist=False)
mt.show()



# Logistic Distribution is used to describe growth.

# Used extensively in machine learning in logistic regression, neural networks etc.

# It has three parameters:

# loc - mean, where the peak is. Default 0.
# scale - standard deviation, the flatness of distribution. Default 1.
# size - The shape of the returned array.


sb.distplot(random.logistic(size=1000), hist=False)

sb.displot(random.logistic(loc=50 , scale=7 , size=1000))
mt.show()



sb.distplot(random.normal(loc=100 , scale=0.5, size=1000), hist=False , label='Normal', color='red')
sb.distplot(random.logistic(size=1000),hist=False, label='Logistics', color='black')

mt.show()



