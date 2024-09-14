# NORMAL DISTRIBUTION

# The Normal Distribution is one of the most important distributions.

# It has three parameters:
# loc - (Mean) where the peak of the bell exists.
# scale - (Standard Deviation) how flat the graph distribution should be.
# size - The shape of the returned array.


from numpy import random
import matplotlib.pyplot as mt
import seaborn as sb

arr = random.normal(size=(2,3))      # It will print the random 2x3 array
print(arr)


arr1 = random.normal(loc=1 , scale=5 , size=(2,3))
print(arr1)


sb.distplot(random.normal(size=(1000)), hist=False)
mt.show()





# Binomial Distribution is a Discrete Distribution.

# It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
# It has three parameters:
# n - number of trials.
# p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.




from numpy import random
import matplotlib.pyplot as mt
import seaborn as sb

x = random.binomial(n=10, p=0.5, size=10)
print(x)


sb.distplot(random.binomial(n=10, p=0.5, size=1000), hist=False, kde=False)
sb.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
sb.distplot(random.normal(loc=50 , scale=5 , size=1000), hist=False , label='Normall')
sb.distplot(random.binomial(n=100 , p=0.5, size=1000) , hist=False , label='Bionomial')
mt.show()




# Poisson Distribution

# Poisson Distribution is a Discrete Distribution.
# It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

# It has two parameters:

# lam - rate or known number of occurrences e.g. 2 for above problem.
# size - The shape of the returned array.


from numpy import random
import matplotlib.pyplot as mt
import seaborn as sb

x =random.poisson(lam=2 , size=10)
print(x)


sb.distplot(random.poisson(lam=2, size=1000), kde=False , label='Possion Graph')
sb.distplot(random.normal(loc=50 , scale=7 , size=1000), hist=False , label='Normal')
sb.distplot(random.poisson(lam=50, size=1000), hist=False , label='Poission')
mt.show()




sb.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sb.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

mt.show()


